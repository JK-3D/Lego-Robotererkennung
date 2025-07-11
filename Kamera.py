import cv2
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import numpy as np

# ---- Vergleichsbild laden (anpassen auf deinen Pfad) ----
template_image_path = "vergleichsbild.jpg"  # Das Bild, das gesucht werden soll
template = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError("Vergleichsbild nicht gefunden!")

# ORB-Detektor vorbereiten
orb = cv2.ORB_create()
template_kp, template_des = orb.detectAndCompute(template, None)

# Matcher vorbereiten
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# ---- GUI vorbereiten ----
window = tk.Tk()
window.title("Kamera mit Mustererkennung")

# Kamera starten
cap = cv2.VideoCapture(0)

# Vorschau-Label
label = tk.Label(window)
label.pack()

# Funktion zum Foto aufnehmen
def capture_image():
    ret, frame = cap.read()
    if ret:
        filename = datetime.datetime.now().strftime("foto_%Y-%m-%d_%H-%M-%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"Foto gespeichert als {filename}")

button = tk.Button(window, text="Foto machen", command=capture_image)
button.pack()

# Beenden-Button
def quit_program():
    cap.release()
    window.destroy()

button_quit = tk.Button(window, text="Beenden", command=quit_program)
button_quit.pack()

# Texteingabe für Python-Code
code_label = tk.Label(window, text="Python-Code hier einfügen:")
code_label.pack()

code_input = tk.Text(window, height=10, width=50)
code_input.pack()

def save_code():
    user_code = code_input.get("1.0", tk.END).strip()
    global gespeicherter_code
    gespeicherter_code = user_code
    print("Code gespeichert.")

button_save_code = tk.Button(window, text="Code speichern", command=save_code)
button_save_code.pack()

# ---- Kamerabild mit Mustererkennung aktualisieren ----
def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_kp, frame_des = orb.detectAndCompute(gray_frame, None)

    if frame_des is not None and template_des is not None:
        matches = bf.match(template_des, frame_des)
        matches = sorted(matches, key=lambda x: x.distance)

        # Genug gute Matches gefunden?
        if len(matches) > 10:
            src_pts = np.float32([template_kp[m.queryIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)
            dst_pts = np.float32([frame_kp[m.trainIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if M is not None:
                h, w = template.shape
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3)

    # Bild für tkinter vorbereiten
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    window.after(10, update_frame)

update_frame()
window.mainloop()

# Ressourcen freigeben
cap.release()
cv2.destroyAllWindows()
