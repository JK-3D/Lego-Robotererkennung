from pybricks.hubs import PrimeHub
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

# Fahre geradeaus 23.6 mm
drive_base.straight(23)
# Fahre geradeaus 32.3 mm
drive_base.straight(32)
# Kurve: Radius ~40 mm, Distanz 23 mm, Richtung rechts
drive_base.curve(40, 23)
# Kurve: Radius ~71 mm, Distanz 23 mm, Richtung rechts
drive_base.curve(71, 23)
# Fahre geradeaus 24.0 mm
drive_base.straight(24)
# Warte 1.13s
wait(1131)
