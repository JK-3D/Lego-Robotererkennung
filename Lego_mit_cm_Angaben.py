import cv2
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import numpy as np
import math

# initialisiere Variablen
position_list = []
x_cm = 0
y_cm = 0
angel_deg = 0

# Kamera-Sichtfeld in Zentimetern
CAMERA_WIDTH_CM = 237.1
CAMERA_HEIGHT_CM = 115.2

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
window.title("Live-Tracking mit SIFT & Zentimeter-Ausgabe")

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Setze Kamera-Auflösung für bekannte Umrechnung (z.B. 1280x720)
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

# tk.Button(window, text="Foto machen", command=capture_image).pack()

def quit_program():
    cap.release()
    window.destroy()

tk.Button(window, text="Beenden", command=quit_program).pack()

def robotfollowing():
    position_list.append([x_cm, y_cm, angel_deg])
    robotfollowing()

tk.Button(window, text="Starte Roboterverfolgung", command=robotfollowing).pack()

# ----- Frame aktualisieren -----
def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    frame = frame[0:FRAME_HEIGHT_PX, 0:FRAME_WIDTH_PX]  # Zuschneiden falls nötig

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

                # Zeichnen
                frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3)

                # Linke untere Ecke: Punkt [1] im Uhrzeigersinn: [0]=oben links, [1]=unten links, ...
                bottom_left = dst[1][0]
                x_px, y_px = bottom_left

                # Umrechnung in Zentimeter
                x_cm = x_px * cm_per_px_x
                y_cm = y_px * cm_per_px_y

                # Rotation berechnen: Vektor von [1] (unten links) zu [2] (unten rechts)
                pt1 = dst[1][0]
                pt2 = dst[2][0]
                dx = pt2[0] - pt1[0]
                dy = pt2[1] - pt1[1]
                angle_rad = math.atan2(dy, dx)
                angle_deg = math.degrees(angle_rad)

                # Ausgabe
                position_output = f"Position: ({x_cm:.1f} cm, {y_cm:.1f} cm), Drehung: {angle_deg:.1f}°"

    # Tkinter Bild
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
print(position_list)
