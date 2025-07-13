from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Starte Bewegung
# Starte bei (113.35, 15.39), Richtung -141.44°
robot.turn(-141.44)  # Anfangsdrehung

# Fahre von (113.35, 15.39) nach (21.00, 96.70)
robot.turn(-79.92)  # Drehe in Richtung Ziel
robot.straight(123.04)  # Fahre geradeaus
robot.turn(121.86)  # Endausrichtung

# Fahre von (21.00, 96.70) nach (154.27, -22.96)
robot.turn(57.58)  # Drehe in Richtung Ziel
robot.straight(179.11)  # Fahre geradeaus
robot.turn(179.62)  # Endausrichtung

# Fahre von (154.27, -22.96) nach (199.17, -59.00)
robot.turn(-176.45)  # Drehe in Richtung Ziel
robot.straight(57.58)  # Fahre geradeaus
robot.turn(176.08)  # Endausrichtung

# Fahre von (199.17, -59.00) nach (29.63, 119.71)
robot.turn(-3.84)  # Drehe in Richtung Ziel
robot.straight(246.34)  # Fahre geradeaus
robot.turn(122.50)  # Endausrichtung

# Fahre von (29.63, 119.71) nach (69.52, 21.93)
robot.turn(36.20)  # Drehe in Richtung Ziel
robot.straight(105.60)  # Fahre geradeaus
robot.turn(49.07)  # Endausrichtung

# Fahre von (69.52, 21.93) nach (-6.01, 108.41)
robot.turn(149.87)  # Drehe in Richtung Ziel
robot.straight(114.82)  # Fahre geradeaus
robot.turn(-178.82)  # Endausrichtung

# Fahre von (-6.01, 108.41) nach (128.32, -11.22)
robot.turn(6.00)  # Drehe in Richtung Ziel
robot.straight(179.88)  # Fahre geradeaus
robot.turn(177.44)  # Endausrichtung

# Fahre von (128.32, -11.22) nach (223.07, 90.62)
robot.turn(-88.68)  # Drehe in Richtung Ziel
robot.straight(139.10)  # Fahre geradeaus
robot.turn(66.71)  # Endausrichtung

# Fahre von (223.07, 90.62) nach (184.14, 10.44)
robot.turn(130.32)  # Drehe in Richtung Ziel
robot.straight(89.13)  # Fahre geradeaus
robot.turn(175.98)  # Endausrichtung

# Fahre von (184.14, 10.44) nach (112.81, 106.62)
robot.turn(66.48)  # Drehe in Richtung Ziel
robot.straight(119.74)  # Fahre geradeaus
robot.turn(58.31)  # Endausrichtung

# Fahre von (112.81, 106.62) nach (101.41, 52.54)
robot.turn(73.23)  # Drehe in Richtung Ziel
robot.straight(55.27)  # Fahre geradeaus
robot.turn(161.46)  # Endausrichtung

# Fahre von (101.41, 52.54) nach (372.60, 241.43)
robot.turn(-24.70)  # Drehe in Richtung Ziel
robot.straight(330.49)  # Fahre geradeaus
robot.turn(179.91)  # Endausrichtung

# Fahre von (372.60, 241.43) nach (200.45, 63.41)
robot.turn(11.19)  # Drehe in Richtung Ziel
robot.straight(247.64)  # Fahre geradeaus
robot.turn(-29.18)  # Endausrichtung

# Fahre von (200.45, 63.41) nach (18958.92, 6924.26)
robot.turn(-176.69)  # Drehe in Richtung Ziel
robot.straight(19973.77)  # Fahre geradeaus
robot.turn(-177.52)  # Endausrichtung

# Fahre von (18958.92, 6924.26) nach (184.95, 114.66)
robot.turn(-2.63)  # Drehe in Richtung Ziel
robot.straight(19970.79)  # Fahre geradeaus
robot.turn(21.66)  # Endausrichtung

# Fahre von (184.95, 114.66) nach (362.79, 240.24)
robot.turn(173.63)  # Drehe in Richtung Ziel
robot.straight(217.71)  # Fahre geradeaus
robot.turn(-71.48)  # Endausrichtung