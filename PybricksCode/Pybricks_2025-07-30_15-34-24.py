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

# Fahre geradeaus 24.6 mm
drive_base.straight(24)
# Fahre geradeaus 24.3 mm
drive_base.straight(24)
# Fahre geradeaus 23.5 mm
drive_base.straight(23)
# Kurve: Radius ~41 mm, Distanz 22 mm, Richtung rechts
drive_base.curve(41, 22)
# Fahre geradeaus 26.0 mm
drive_base.straight(25)
# Fahre geradeaus 31.3 mm
drive_base.straight(31)
# Fahre geradeaus 5.1 mm
drive_base.straight(5)
