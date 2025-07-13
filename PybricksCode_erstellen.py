import csv
import math
import datetime

def generate_pybricks_code(csv_filename, output_filename=datetime.datetime.now().strftime("PybricksCode\Pybricks_%Y-%m-%d_%H-%M-%S.py")):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Initialisierung des Codes
    pybricks_code = [
        "from pybricks.hubs import EV3Brick",
        "from pybricks.ev3devices import Motor",
        "from pybricks.parameters import Port, Stop, Direction",
        "from pybricks.tools import wait",
        "from pybricks.robotics import DriveBase",
        "",
        "ev3 = EV3Brick()",
        "left_motor = Motor(Port.B)",
        "right_motor = Motor(Port.C)",
        "robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)",
        "",
        "# Starte Bewegung"
    ]

    last_x = None
    last_y = None
    last_rot = None

    for row in data:
        x = float(row["x_cm"])
        y = float(row["y_cm"])
        rot = float(row["rotation_deg"])

        if last_x is None:
            # Anfangsposition, setze nur die Orientierung
            pybricks_code.append(f"# Starte bei ({x:.2f}, {y:.2f}), Richtung {rot:.2f}°")
            pybricks_code.append(f"robot.turn({rot:.2f})  # Anfangsdrehung")
        else:
            dx = x - last_x
            dy = y - last_y
            distance = math.hypot(dx, dy)
            angle_to_target = math.degrees(math.atan2(dy, dx))
            delta_angle = angle_to_target - last_rot

            # Normalisiere Winkel auf [-180, 180]
            delta_angle = (delta_angle + 180) % 360 - 180
            final_heading_change = rot - angle_to_target
            final_heading_change = (final_heading_change + 180) % 360 - 180

            pybricks_code.append("")
            pybricks_code.append(f"# Fahre von ({last_x:.2f}, {last_y:.2f}) nach ({x:.2f}, {y:.2f})")
            pybricks_code.append(f"robot.turn({delta_angle:.2f})  # Drehe in Richtung Ziel")
            pybricks_code.append(f"robot.straight({distance:.2f})  # Fahre geradeaus")
            pybricks_code.append(f"robot.turn({final_heading_change:.2f})  # Endausrichtung")

        last_x = x
        last_y = y
        last_rot = rot

    with open(output_filename, "w") as f:
        f.write("\n".join(pybricks_code))

    print(f"Pybricks-Code wurde generiert in: {output_filename}")

# Beispielaufruf
generate_pybricks_code("Live_Positionen\Live_Position_2025-07-12_17-29-33.csv")
