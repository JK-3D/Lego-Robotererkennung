import cv2
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import numpy as np

# ---- Vergleichsbild laden ----
template_path = "vergleichsbild.jpg"
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError("Vergleichsbild nicht gefunden!")

# SIFT vorbereiten
sift = cv2.SIFT_create()
template_kp, template_des = sift.detectAndCompute(template, None)

# Matcher für SIFT
bf = cv2.BFMatcher()

# ---- GUI vorbereiten ----
window = tk.Tk()
window.title("SIFT-Erkennung Live + Foto")

# Kamera starten
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Vorschau-Label
label = tk.Label(window)
label.pack()

# ---- Funktion: Bild speichern + SIFT-Vergleich ----
def capture_image():
    ret, frame = cap.read()
    if ret:
        filename = datetime.datetime.now().strftime("foto_%Y-%m-%d_%H-%M-%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"Foto gespeichert als {filename}")

        gray_scene = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        scene_kp, scene_des = sift.detectAndCompute(gray_scene, None)

        if scene_des is not None and template_des is not None:
            matches = bf.knnMatch(template_des, scene_des, k=2)

            # Lowe's Ratio Test
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append(m)

            if len(good) > 10:
                src_pts = np.float32([template_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([scene_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                if M is not None:
                    h, w = template.shape
                    pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, M)
                    result_img = cv2.polylines(frame.copy(), [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)

                    cv2.imshow("SIFT-Ergebnis (Foto)", result_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("Homographie fehlgeschlagen.")
            else:
                print("Nicht genügend Übereinstimmungen gefunden - %d" % len(good))
        else:
            print("Deskriptoren nicht berechnet.")

# Foto-Button
tk.Button(window, text="Foto machen", command=capture_image).pack()

# Beenden-Button
def quit_program():
    cap.release()
    window.destroy()

tk.Button(window, text="Beenden", command=quit_program).pack()

# Codeeingabe (optional)
tk.Label(window, text="Python-Code hier einfügen:").pack()
code_input = tk.Text(window, height=10, width=50)
code_input.pack()

def save_code():
    user_code = code_input.get("1.0", tk.END).strip()
    global gespeicherter_code
    gespeicherter_code = user_code
    print("Code gespeichert.")

tk.Button(window, text="Code speichern", command=save_code).pack()

# ---- Live-Vorschau mit SIFT-Erkennung ----
def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame, des_frame = sift.detectAndCompute(gray, None)

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

    # Frame in tkinter anzeigen
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    window.after(10, update_frame)

update_frame()
window.mainloop()

cap.release()
cv2.destroyAllWindows()
