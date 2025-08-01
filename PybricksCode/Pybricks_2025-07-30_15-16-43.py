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

# Fahre geradeaus 20.1 mm
drive_base.straight(20)
# Fahre geradeaus 23.2 mm
drive_base.straight(23)
