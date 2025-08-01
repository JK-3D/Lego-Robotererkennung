import math
import datetime

# Direkte Eingabe deiner CSV-Daten
raw_data = """
2025-07-30T15:33:46.302101,141.71,55.76,2.56
2025-07-30T15:33:46.528920,139.98,59.35,1.36
2025-07-30T15:33:46.751202,136.81,60.91,1.25
2025-07-30T15:33:46.984623,136.26,68.87,0.28
2025-07-30T15:33:47.205136,138.31,69.42,0.66
2025-07-30T15:33:47.422107,140.03,68.41,0.85
2025-07-30T15:33:47.635869,137.44,72.01,0.37
2025-07-30T15:33:47.850130,135.39,79.49,-0.23
2025-07-30T15:33:48.072194,134.40,83.45,-0.25
2025-07-30T15:33:48.294113,133.63,93.28,-0.93
2025-07-30T15:33:48.511155,133.96,103.73,-1.83
2025-07-30T15:33:48.725553,133.10,109.60,-1.84
2025-07-30T15:33:48.952280,133.07,121.16,-2.63
2025-07-30T15:33:49.167236,133.22,127.23,-3.49
2025-07-30T15:33:49.386412,132.63,135.71,-4.10
2025-07-30T15:33:49.608634,132.00,142.40,-3.46
2025-07-30T15:33:49.827509,132.40,143.70,-3.43
2025-07-30T15:33:50.037218,133.08,144.28,-2.16
2025-07-30T15:33:50.256183,132.36,141.34,2.56
2025-07-30T15:33:50.475598,132.92,139.78,6.16
2025-07-30T15:33:50.703916,133.23,132.23,17.33
2025-07-30T15:33:50.915290,134.34,129.38,22.07
2025-07-30T15:33:51.127589,137.30,126.19,25.85
2025-07-30T15:33:51.330198,139.32,126.24,26.34
2025-07-30T15:33:51.546274,140.72,125.55,26.69
2025-07-30T15:33:51.755283,146.77,119.83,27.07
2025-07-30T15:33:51.958393,151.21,114.47,26.95
2025-07-30T15:33:52.170030,162.87,100.74,28.90
2025-07-30T15:33:52.385824,168.37,95.00,29.62
2025-07-30T15:33:52.603250,182.14,83.33,31.68
2025-07-30T15:33:52.813458,191.99,74.43,32.31
2025-07-30T15:33:53.071149,195.08,69.98,32.96
2025-07-30T15:33:53.316290,197.80,62.43,34.11
2025-07-30T15:33:53.558130,197.13,61.74,33.71
2025-07-30T15:33:53.777340,195.03,65.51,31.45
2025-07-30T15:33:53.992982,196.71,65.27,31.58
2025-07-30T15:33:54.215571,197.98,68.88,31.26
2025-07-30T15:33:54.441598,193.51,69.53,31.57
""".strip()

# Parsing der CSV
data = []
for line in raw_data.splitlines():
    timestamp_str, x, y, rotation = line.split(",")
    timestamp = datetime.datetime.fromisoformat(timestamp_str)
    data.append((timestamp, float(x), float(y), float(rotation)))

# Zeitabstände berechnen
base_time = data[0][0]
data = [( (t - base_time).total_seconds(), x, y, rot ) for t, x, y, rot in data]

# Hilfsfunktionen
def distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

def angle_diff(a1, a2):
    """Kleinste Winkeländerung (Grad)"""
    diff = (a2 - a1 + 180) % 360 - 180
    return diff

def average_rotation(rotations):
    sin_sum = sum(math.sin(math.radians(r)) for r in rotations)
    cos_sum = sum(math.cos(math.radians(r)) for r in rotations)
    return math.degrees(math.atan2(sin_sum, cos_sum)) % 360

# Verarbeitung in Segmente
MIN_DIST = 5  # mm
commands = []

i = 0
while i < len(data) - 1:
    start = data[i]
    segment = [start]
    j = i + 1
    while j < len(data):
        segment.append(data[j])
        dist = distance((start[1], start[2]), (data[j][1], data[j][2]))
        if dist > 20:
            break
        j += 1
    end = segment[-1]
    i = j

    dist = distance((start[1], start[2]), (end[1], end[2]))
    d_angle = angle_diff(start[3], end[3])
    duration = end[0] - start[0]

    if dist < MIN_DIST and abs(d_angle) < 5:
        commands.append(f"# Warte {duration:.2f}s")
        commands.append(f"wait({int(duration * 1000)})")
    elif abs(d_angle) > 10 and dist < 15:
        commands.append(f"# Drehe um {d_angle:.1f}°")
        commands.append(f"drive_base.turn({int(d_angle)})")
    elif abs(d_angle) < 5:
        commands.append(f"# Fahre geradeaus {dist:.1f} mm")
        commands.append(f"drive_base.straight({int(dist)})")
    else:
        turn_radius = dist / math.radians(abs(d_angle)) if abs(d_angle) > 0 else 0
        commands.append(f"# Kurve: Radius ~{int(turn_radius)} mm, Distanz {int(dist)} mm, Richtung {'links' if d_angle < 0 else 'rechts'}")
        curve_val = int(turn_radius) if d_angle > 0 else -int(turn_radius)
        commands.append(f"drive_base.curve({curve_val}, {int(dist)})")

# Pybricks-Code generieren
with open(datetime.datetime.now().strftime("PybricksCode\Pybricks_%Y-%m-%d_%H-%M-%S.py"), "w") as f:
    f.write('''from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.parameters import Port

hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)

# Anpassen an deinen Roboter
wheel_diameter = 56  # mm
axle_track = 114     # mm

drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

''')
    for cmd in commands:
        f.write(cmd + "\n")

print("✅ Pybricks-Code erfolgreich in 'lego_fahrt.py' gespeichert.")
