import cv2
import numpy as np

# Bilder laden
img_scene = cv2.imread('foto_2025-07-11_21-12-13.jpg', cv2.IMREAD_GRAYSCALE)  # Szene
img_object = cv2.imread('vergleichsbild.jpg', cv2.IMREAD_GRAYSCALE)       # Handy-Referenz

# Merkmalsdetektor erstellen
sift = cv2.SIFT_create()  # Alternativ: cv2.ORB_create()

# Merkmale und Deskriptoren berechnen
kp1, des1 = sift.detectAndCompute(img_object, None)
kp2, des2 = sift.detectAndCompute(img_scene, None)

# Feature-Matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Lowe's Ratio Test
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

MIN_MATCH_COUNT = 4
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # Homographie berechnen
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Handy-Umriss auf Szene übertragen
    h, w = img_object.shape
    pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)

    img_scene_color = cv2.imread('großes_bild.jpg')  # Farbe für Anzeige
    result = cv2.polylines(img_scene_color, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Ergebnis', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nicht genügend Übereinstimmungen gefunden - %d/%d" % (len(good), MIN_MATCH_COUNT))
