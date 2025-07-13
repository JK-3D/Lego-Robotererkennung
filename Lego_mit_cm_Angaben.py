import cv2
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import numpy as np
import math
import csv
import os

# Kamera-Sichtfeld in Zentimetern
CAMERA_WIDTH_CM = 237.1
CAMERA_HEIGHT_CM = 115.2

# CSV-Datei vorbereiten
csv_filename = datetime.datetime.now().strftime("Live_Positionen\Live_Position_%Y-%m-%d_%H-%M-%S.csv")
if not os.path.exists(csv_filename):
    with open(csv_filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "x_cm", "y_cm", "rotation_deg"])

# --- Vorlage laden ---
template_path = "vergleichsbild.jpg"
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError("Vergleichsbild nicht gefunden!")

sift = cv2.SIFT_create()
template_kp, template_des = sift.detectAndCompute(template, None)
bf = cv2.BFMatcher()

# --- GUI Setup ---
window = tk.Tk()
window.title("Live-Tracking mit Zentimeter & CSV-Logging")

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Setze Kamera-Auflösung für bekannte Umrechnung (z. B. 1280x720)
FRAME_WIDTH_PX = 1280
FRAME_HEIGHT_PX = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH_PX)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT_PX)

# Berechne Pixel-zu-cm-Faktoren
cm_per_px_x = CAMERA_WIDTH_CM / FRAME_WIDTH_PX
cm_per_px_y = CAMERA_HEIGHT_CM / FRAME_HEIGHT_PX

# Vorschau-Label
label = tk.Label(window)
label.pack()

# Positionstext
position_label = tk.Label(window, text="")
position_label.pack()

# ----- Foto aufnehmen -----
def capture_image():
    ret, frame = cap.read()
    if ret:
        filename = datetime.datetime.now().strftime("foto_%Y-%m-%d_%H-%M-%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"Foto gespeichert als {filename}")

tk.Button(window, text="Foto machen", command=capture_image).pack()

def quit_program():
    cap.release()
    window.destroy()

tk.Button(window, text="Beenden", command=quit_program).pack()


# ----- Frame aktualisieren -----
def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    frame = frame[0:FRAME_HEIGHT_PX, 0:FRAME_WIDTH_PX]

    # Bils skalieren ohne zuzuschneiden
    scale_percent = 125
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # Bild zuschneiden
    #frame = frame[50:height-500, 50:width-500]

    # Bild drehen
    #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Bild kippen
    # # Breite und Höhe des Videos
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Transformation definieren
    # Quellpunkte (ganze Fläche)
    src_pts = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1],
        [width - 1, height - 1]
    ])

    # Zielpunkte (oben näher zusammen, unten weiter auseinander)
    margin = 100  # wie stark gestaucht wird
    dst_pts = np.float32([
        [margin, 0],              # oben links näher zur Mitte
        [width - margin, 0],      # oben rechts näher zur Mitte
        [0, height - 1],          # unten links bleibt gleich
        [width - 1, height - 1]   # unten rechts bleibt gleich
    ])

    # Perspektivmatrix berechnen
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)

    # Transformation anwenden
    #frame = cv2.warpPerspective(frame, M, (width, height))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame, des_frame = sift.detectAndCompute(gray, None)

    position_output = "Nicht erkannt"

    if des_frame is not None and template_des is not None:
        matches = bf.knnMatch(template_des, des_frame, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append(m)

        if len(good) > 10:
            src_pts = np.float32([template_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if M is not None:
                h, w = template.shape
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)

                frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3)

                # Linke untere Ecke
                bottom_left = dst[1][0]
                x_px, y_px = bottom_left

                x_cm = x_px * cm_per_px_x
                y_cm = y_px * cm_per_px_y

                # Rotation
                pt1 = dst[1][0]
                pt2 = dst[2][0]
                dx = pt2[0] - pt1[0]
                dy = pt2[1] - pt1[1]
                angle_rad = math.atan2(dy, dx)
                angle_deg = math.degrees(angle_rad)

                # Ausgabe
                position_output = f"Position: ({x_cm:.1f} cm, {y_cm:.1f} cm), Drehung: {angle_deg:.1f}°"

                # Log in CSV-Datei
                timestamp = datetime.datetime.now().isoformat()
                with open(csv_filename, mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, f"{x_cm:.2f}", f"{y_cm:.2f}", f"{angle_deg:.2f}"])

    # Tkinter Bild anzeigen
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    position_label.config(text=position_output)

    window.after(20, update_frame)

update_frame()
window.mainloop()

cap.release()
cv2.destroyAllWindows()
