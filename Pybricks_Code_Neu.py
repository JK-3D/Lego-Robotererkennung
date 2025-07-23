import csv
import datetime
from math import atan2, degrees, sqrt

# ---- Konfigurierbare Toleranzen ----
DIST_TOLERANCE_CM = 2
HEADING_TOLERANCE_DEG = 5
DIST_THRESHOLD_CM = 1
WAIT_THRESHOLD_SEC = 0.5

# ---- Hilfsfunktionen ----
def distance(p1, p2):
    return sqrt((p2["x_cm"] - p1["x_cm"])**2 + (p2["y_cm"] - p1["y_cm"])**2)

def heading_between(p1, p2):
    angle = degrees(atan2(p2["y_cm"] - p1["y_cm"], p2["x_cm"] - p1["x_cm"]))
    return angle % 360

def time_diff(p1, p2):
    return (p2["timestamp"] - p1["timestamp"]).total_seconds()

def parse_csv(filename):
    points = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            points.append({
                "timestamp": datetime.datetime.fromisoformat(row["timestamp"]),
                "x_cm": float(row["x_cm"]),
                "y_cm": float(row["y_cm"]),
                "rotation_deg": float(row["rotation_deg"])
            })
    return points

# ---- Hauptanalyse ----
def generate_movements(points):
    commands = []
    i = 0
    while i < len(points) - 1:
        p1 = points[i]
        p2 = points[i + 1]
        dist = distance(p1, p2)
        dt = time_diff(p1, p2)

        print(f"→ Von Punkt {i} zu {i+1}:")
        print(f"   Pos1: ({p1['x_cm']:.2f}, {p1['y_cm']:.2f}), Rot: {p1['rotation_deg']:.1f}")
        print(f"   Pos2: ({p2['x_cm']:.2f}, {p2['y_cm']:.2f}), Rot: {p2['rotation_deg']:.1f}")
        print(f"   Distanz: {dist:.2f} cm, Zeitdifferenz: {dt:.2f} s")
        print(f"   Bewegung: Richtung {heading_between(p1, p2):.1f}°, Drehdelta: {(p2['rotation_deg'] - p1['rotation_deg']):.1f}")

        if dist < DIST_THRESHOLD_CM and dt >= WAIT_THRESHOLD_SEC:
            commands.append(f"wait({round(dt, 2)})  # Warten")
        else:
            angle = heading_between(p1, p2)
            rotation_delta = (angle - p1["rotation_deg"] + 180) % 360 - 180

            if abs(rotation_delta) > HEADING_TOLERANCE_DEG:
                commands.append(f"turn({round(rotation_delta, 1)})  # Drehen")
            else:
                if abs(p2["rotation_deg"] - p1["rotation_deg"]) > HEADING_TOLERANCE_DEG:
                    commands.append(f"curve({round(dist, 1)}, {round(p2['rotation_deg'] - p1['rotation_deg'], 1)})")
                else:
                    commands.append(f"straight({round(dist, 1)})")
        i += 1
    return commands

# ---- Pybricks Code-Generator ----
def generate_pybricks_code(commands):
    header = [
        "from pybricks.hubs import PrimeHub",
        "from pybricks.pupdevices import Motor",
        "from pybricks.parameters import Port, Direction",
        "from pybricks.robotics import DriveBase",
        "from pybricks.tools import wait",
        "",
        "hub = PrimeHub()",
        "left_motor = Motor(Port.A)",
        "right_motor = Motor(Port.B)",
        "robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)",
        ""
    ]
    pybricks_commands = []
    for cmd in commands:
        if cmd.startswith("straight"):
            dist = float(cmd.split("(")[1].split(")")[0])
            pybricks_commands.append(f"robot.straight({int(dist)})")
        elif cmd.startswith("turn"):
            angle = float(cmd.split("(")[1].split(")")[0])
            pybricks_commands.append(f"robot.turn({int(angle)})")
        elif cmd.startswith("curve"):
            parts = cmd[6:-1].split(",")
            dist, delta_angle = float(parts[0]), float(parts[1])
            pybricks_commands.append(f"# Approx curve: robot.straight({int(dist)}); robot.turn({int(delta_angle)})")
        elif cmd.startswith("wait"):
            t = float(cmd.split("(")[1].split(")")[0])
            pybricks_commands.append(f"wait({int(t * 1000)})")
        else:
            pybricks_commands.append(f"# {cmd}  # nicht erkannt")

    return "\n".join(header + pybricks_commands)

# ---- Datei schreiben ----
def save_code_to_file(code, output_filename=datetime.datetime.now().strftime("PybricksCode\Pybricks_%Y-%m-%d_%H-%M-%S.py")):
    with open(output_filename, "w") as f:
        f.write(code)
    print(f"[✔] Pybricks-Code wurde in '{output_filename}' gespeichert.")

# ---- Ausführung ----
if __name__ == "__main__":
    filename = "Live_Positionen\Live_Position_2025-07-12_16-18-41.csv"  # Deine CSV-Datei
    points = parse_csv(filename)
    commands = generate_movements(points)
    code = generate_pybricks_code(commands)
    save_code_to_file(code)
