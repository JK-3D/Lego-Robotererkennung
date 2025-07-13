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
# Starte bei (91.59, 93.20), Richtung 13.14°
robot.turn(13.14)  # Anfangsdrehung

# Fahre von (91.59, 93.20) nach (270.84, 129.88)
robot.turn(-1.58)  # Drehe in Richtung Ziel
robot.straight(182.96)  # Fahre geradeaus
robot.turn(168.77)  # Endausrichtung

# Fahre von (270.84, 129.88) nach (224.35, 67.93)
robot.turn(52.78)  # Drehe in Richtung Ziel
robot.straight(77.45)  # Fahre geradeaus
robot.turn(-157.38)  # Endausrichtung

# Fahre von (224.35, 67.93) nach (231.56, 108.67)
robot.turn(4.23)  # Drehe in Richtung Ziel
robot.straight(41.37)  # Fahre geradeaus
robot.turn(-45.31)  # Endausrichtung

# Fahre von (231.56, 108.67) nach (224.37, 59.15)
robot.turn(-132.91)  # Drehe in Richtung Ziel
robot.straight(50.04)  # Fahre geradeaus
robot.turn(90.04)  # Endausrichtung

# Fahre von (224.37, 59.15) nach (225.42, 58.67)
robot.turn(-16.35)  # Drehe in Richtung Ziel
robot.straight(1.15)  # Fahre geradeaus
robot.turn(6.89)  # Endausrichtung

# Fahre von (225.42, 58.67) nach (226.10, 46.90)
robot.turn(-69.01)  # Drehe in Richtung Ziel
robot.straight(11.79)  # Fahre geradeaus
robot.turn(-176.97)  # Endausrichtung

# Fahre von (226.10, 46.90) nach (118.97, 81.60)
robot.turn(65.71)  # Drehe in Richtung Ziel
robot.straight(112.61)  # Fahre geradeaus
robot.turn(3.41)  # Endausrichtung

# Fahre von (118.97, 81.60) nach (231.81, 120.21)
robot.turn(-146.57)  # Drehe in Richtung Ziel
robot.straight(119.26)  # Fahre geradeaus
robot.turn(-31.19)  # Endausrichtung

# Fahre von (231.81, 120.21) nach (225.43, 53.76)
robot.turn(-83.18)  # Drehe in Richtung Ziel
robot.straight(66.76)  # Fahre geradeaus
robot.turn(43.31)  # Endausrichtung

# Fahre von (225.43, 53.76) nach (228.50, 53.16)
robot.turn(41.11)  # Drehe in Richtung Ziel
robot.straight(3.13)  # Fahre geradeaus
robot.turn(179.10)  # Endausrichtung

# Fahre von (228.50, 53.16) nach (237.73, 55.09)
robot.turn(-156.23)  # Drehe in Richtung Ziel
robot.straight(9.43)  # Fahre geradeaus
robot.turn(166.60)  # Endausrichtung

# Fahre von (237.73, 55.09) nach (225.44, 57.88)
robot.turn(-11.20)  # Drehe in Richtung Ziel
robot.straight(12.60)  # Fahre geradeaus
robot.turn(-104.43)  # Endausrichtung

# Fahre von (225.44, 57.88) nach (197.52, 107.35)
robot.turn(56.66)  # Drehe in Richtung Ziel
robot.straight(56.80)  # Fahre geradeaus
robot.turn(-118.05)  # Endausrichtung

# Fahre von (197.52, 107.35) nach (192.35, 104.52)
robot.turn(-152.69)  # Drehe in Richtung Ziel
robot.straight(5.89)  # Fahre geradeaus
robot.turn(159.81)  # Endausrichtung

# Fahre von (192.35, 104.52) nach (184.14, 105.43)
robot.turn(165.17)  # Drehe in Richtung Ziel
robot.straight(8.26)  # Fahre geradeaus
robot.turn(-178.67)  # Endausrichtung

# Fahre von (184.14, 105.43) nach (179.29, 105.09)
robot.turn(-171.00)  # Drehe in Richtung Ziel
robot.straight(4.86)  # Fahre geradeaus
robot.turn(169.53)  # Endausrichtung

# Fahre von (179.29, 105.09) nach (178.03, 105.76)
robot.turn(158.46)  # Drehe in Richtung Ziel
robot.straight(1.43)  # Fahre geradeaus
robot.turn(-159.20)  # Endausrichtung

# Fahre von (178.03, 105.76) nach (177.31, 105.54)
robot.turn(-155.81)  # Drehe in Richtung Ziel
robot.straight(0.75)  # Fahre geradeaus
robot.turn(156.53)  # Endausrichtung

# Fahre von (177.31, 105.54) nach (176.81, 104.85)
robot.turn(-119.45)  # Drehe in Richtung Ziel
robot.straight(0.85)  # Fahre geradeaus
robot.turn(119.81)  # Endausrichtung

# Fahre von (176.81, 104.85) nach (176.87, 105.10)
robot.turn(82.62)  # Drehe in Richtung Ziel
robot.straight(0.26)  # Fahre geradeaus
robot.turn(-83.20)  # Endausrichtung

# Fahre von (176.87, 105.10) nach (174.67, 104.44)
robot.turn(-156.60)  # Drehe in Richtung Ziel
robot.straight(2.30)  # Fahre geradeaus
robot.turn(156.50)  # Endausrichtung

# Fahre von (174.67, 104.44) nach (171.18, 105.01)
robot.turn(177.52)  # Drehe in Richtung Ziel
robot.straight(3.54)  # Fahre geradeaus
robot.turn(-178.64)  # Endausrichtung

# Fahre von (171.18, 105.01) nach (166.36, 104.76)
robot.turn(-169.11)  # Drehe in Richtung Ziel
robot.straight(4.83)  # Fahre geradeaus
robot.turn(169.35)  # Endausrichtung

# Fahre von (166.36, 104.76) nach (162.53, 104.56)
robot.turn(-169.33)  # Drehe in Richtung Ziel
robot.straight(3.84)  # Fahre geradeaus
robot.turn(168.31)  # Endausrichtung

# Fahre von (162.53, 104.56) nach (159.94, 103.65)
robot.turn(-151.94)  # Drehe in Richtung Ziel
robot.straight(2.75)  # Fahre geradeaus
robot.turn(152.93)  # Endausrichtung

# Fahre von (159.94, 103.65) nach (158.87, 103.62)
robot.turn(-170.68)  # Drehe in Richtung Ziel
robot.straight(1.07)  # Fahre geradeaus
robot.turn(169.64)  # Endausrichtung

# Fahre von (158.87, 103.62) nach (158.29, 103.42)
robot.turn(-152.22)  # Drehe in Richtung Ziel
robot.straight(0.61)  # Fahre geradeaus
robot.turn(152.68)  # Endausrichtung

# Fahre von (158.29, 103.42) nach (157.84, 103.25)
robot.turn(-151.01)  # Drehe in Richtung Ziel
robot.straight(0.48)  # Fahre geradeaus
robot.turn(151.31)  # Endausrichtung

# Fahre von (157.84, 103.25) nach (157.50, 102.48)
robot.turn(-105.83)  # Drehe in Richtung Ziel
robot.straight(0.84)  # Fahre geradeaus
robot.turn(105.63)  # Endausrichtung

# Fahre von (157.50, 102.48) nach (156.18, 102.37)
robot.turn(-167.05)  # Drehe in Richtung Ziel
robot.straight(1.32)  # Fahre geradeaus
robot.turn(166.20)  # Endausrichtung

# Fahre von (156.18, 102.37) nach (155.58, 101.81)
robot.turn(-127.93)  # Drehe in Richtung Ziel
robot.straight(0.82)  # Fahre geradeaus
robot.turn(127.95)  # Endausrichtung

# Fahre von (155.58, 101.81) nach (155.06, 101.32)
robot.turn(-127.68)  # Drehe in Richtung Ziel
robot.straight(0.71)  # Fahre geradeaus
robot.turn(128.10)  # Endausrichtung

# Fahre von (155.06, 101.32) nach (154.06, 100.88)
robot.turn(-147.65)  # Drehe in Richtung Ziel
robot.straight(1.09)  # Fahre geradeaus
robot.turn(147.78)  # Endausrichtung

# Fahre von (154.06, 100.88) nach (152.75, 100.33)
robot.turn(-148.76)  # Drehe in Richtung Ziel
robot.straight(1.42)  # Fahre geradeaus
robot.turn(148.44)  # Endausrichtung

# Fahre von (152.75, 100.33) nach (152.54, 100.28)
robot.turn(-157.82)  # Drehe in Richtung Ziel
robot.straight(0.22)  # Fahre geradeaus
robot.turn(157.83)  # Endausrichtung

# Fahre von (152.54, 100.28) nach (152.69, 99.69)
robot.turn(-66.96)  # Drehe in Richtung Ziel
robot.straight(0.61)  # Fahre geradeaus
robot.turn(66.85)  # Endausrichtung

# Fahre von (152.69, 99.69) nach (152.74, 98.68)
robot.turn(-78.28)  # Drehe in Richtung Ziel
robot.straight(1.01)  # Fahre geradeaus
robot.turn(78.16)  # Endausrichtung

# Fahre von (152.74, 98.68) nach (152.61, 97.68)
robot.turn(-88.40)  # Drehe in Richtung Ziel
robot.straight(1.01)  # Fahre geradeaus
robot.turn(88.92)  # Endausrichtung

# Fahre von (152.61, 97.68) nach (151.97, 96.60)
robot.turn(-112.16)  # Drehe in Richtung Ziel
robot.straight(1.26)  # Fahre geradeaus
robot.turn(112.08)  # Endausrichtung

# Fahre von (151.97, 96.60) nach (151.01, 95.66)
robot.turn(-127.03)  # Drehe in Richtung Ziel
robot.straight(1.34)  # Fahre geradeaus
robot.turn(126.64)  # Endausrichtung

# Fahre von (151.01, 95.66) nach (150.54, 95.16)
robot.turn(-124.27)  # Drehe in Richtung Ziel
robot.straight(0.69)  # Fahre geradeaus
robot.turn(124.46)  # Endausrichtung

# Fahre von (150.54, 95.16) nach (150.03, 94.12)
robot.turn(-107.35)  # Drehe in Richtung Ziel
robot.straight(1.16)  # Fahre geradeaus
robot.turn(108.45)  # Endausrichtung

# Fahre von (150.03, 94.12) nach (148.17, 93.96)
robot.turn(-167.41)  # Drehe in Richtung Ziel
robot.straight(1.87)  # Fahre geradeaus
robot.turn(166.11)  # Endausrichtung

# Fahre von (148.17, 93.96) nach (147.00, 93.64)
robot.turn(-155.73)  # Drehe in Richtung Ziel
robot.straight(1.21)  # Fahre geradeaus
robot.turn(155.53)  # Endausrichtung

# Fahre von (147.00, 93.64) nach (146.63, 93.41)
robot.turn(-138.96)  # Drehe in Richtung Ziel
robot.straight(0.44)  # Fahre geradeaus
robot.turn(138.04)  # Endausrichtung

# Fahre von (146.63, 93.41) nach (147.78, 92.51)
robot.turn(-27.96)  # Drehe in Richtung Ziel
robot.straight(1.46)  # Fahre geradeaus
robot.turn(28.69)  # Endausrichtung

# Fahre von (147.78, 92.51) nach (151.30, 92.94)
robot.turn(16.32)  # Drehe in Richtung Ziel
robot.straight(3.55)  # Fahre geradeaus
robot.turn(-19.24)  # Endausrichtung

# Fahre von (151.30, 92.94) nach (155.57, 92.12)
robot.turn(1.41)  # Drehe in Richtung Ziel
robot.straight(4.35)  # Fahre geradeaus
robot.turn(1.03)  # Endausrichtung

# Fahre von (155.57, 92.12) nach (157.94, 92.87)
robot.turn(27.40)  # Drehe in Richtung Ziel
robot.straight(2.49)  # Fahre geradeaus
robot.turn(-30.42)  # Endausrichtung

# Fahre von (157.94, 92.87) nach (160.15, 92.87)
robot.turn(12.86)  # Drehe in Richtung Ziel
robot.straight(2.21)  # Fahre geradeaus
robot.turn(-13.55)  # Endausrichtung

# Fahre von (160.15, 92.87) nach (162.36, 93.00)
robot.turn(16.92)  # Drehe in Richtung Ziel
robot.straight(2.21)  # Fahre geradeaus
robot.turn(-16.80)  # Endausrichtung

# Fahre von (162.36, 93.00) nach (163.93, 93.05)
robot.turn(15.25)  # Drehe in Richtung Ziel
robot.straight(1.57)  # Fahre geradeaus
robot.turn(-13.63)  # Endausrichtung

# Fahre von (163.93, 93.05) nach (162.57, 94.50)
robot.turn(144.98)  # Drehe in Richtung Ziel
robot.straight(1.99)  # Fahre geradeaus
robot.turn(-145.51)  # Endausrichtung

# Fahre von (162.57, 94.50) nach (158.90, 95.83)
robot.turn(172.42)  # Drehe in Richtung Ziel
robot.straight(3.90)  # Fahre geradeaus
robot.turn(-171.10)  # Endausrichtung

# Fahre von (158.90, 95.83) nach (156.10, 96.53)
robot.turn(176.98)  # Drehe in Richtung Ziel
robot.straight(2.89)  # Fahre geradeaus
robot.turn(-176.32)  # Endausrichtung

# Fahre von (156.10, 96.53) nach (152.86, 97.30)
robot.turn(176.99)  # Drehe in Richtung Ziel
robot.straight(3.33)  # Fahre geradeaus
robot.turn(-177.84)  # Endausrichtung

# Fahre von (152.86, 97.30) nach (149.78, 97.90)
robot.turn(-179.81)  # Drehe in Richtung Ziel
robot.straight(3.14)  # Fahre geradeaus
robot.turn(179.31)  # Endausrichtung

# Fahre von (149.78, 97.90) nach (148.09, 98.36)
robot.turn(176.48)  # Drehe in Richtung Ziel
robot.straight(1.75)  # Fahre geradeaus
robot.turn(-175.39)  # Endausrichtung

# Fahre von (148.09, 98.36) nach (147.89, 99.03)
robot.turn(117.24)  # Drehe in Richtung Ziel
robot.straight(0.70)  # Fahre geradeaus
robot.turn(-117.89)  # Endausrichtung

# Fahre von (147.89, 99.03) nach (150.03, 100.30)
robot.turn(41.96)  # Drehe in Richtung Ziel
robot.straight(2.49)  # Fahre geradeaus
robot.turn(-47.90)  # Endausrichtung

# Fahre von (150.03, 100.30) nach (151.95, 100.84)
robot.turn(32.92)  # Drehe in Richtung Ziel
robot.straight(1.99)  # Fahre geradeaus
robot.turn(-34.39)  # Endausrichtung

# Fahre von (151.95, 100.84) nach (154.90, 101.59)
robot.turn(32.94)  # Drehe in Richtung Ziel
robot.straight(3.04)  # Fahre geradeaus
robot.turn(-37.61)  # Endausrichtung

# Fahre von (154.90, 101.59) nach (156.99, 102.01)
robot.turn(34.71)  # Drehe in Richtung Ziel
robot.straight(2.13)  # Fahre geradeaus
robot.turn(-38.18)  # Endausrichtung

# Fahre von (156.99, 102.01) nach (158.10, 102.61)
robot.turn(55.21)  # Drehe in Richtung Ziel
robot.straight(1.26)  # Fahre geradeaus
robot.turn(-55.96)  # Endausrichtung

# Fahre von (158.10, 102.61) nach (159.08, 103.08)
robot.turn(53.19)  # Drehe in Richtung Ziel
robot.straight(1.09)  # Fahre geradeaus
robot.turn(-48.05)  # Endausrichtung

# Fahre von (159.08, 103.08) nach (158.86, 103.84)
robot.turn(128.57)  # Drehe in Richtung Ziel
robot.straight(0.79)  # Fahre geradeaus
robot.turn(-121.87)  # Endausrichtung

# Fahre von (158.86, 103.84) nach (158.93, 105.01)
robot.turn(102.31)  # Drehe in Richtung Ziel
robot.straight(1.17)  # Fahre geradeaus
robot.turn(-98.79)  # Endausrichtung

# Fahre von (158.93, 105.01) nach (159.38, 106.12)
robot.turn(80.14)  # Drehe in Richtung Ziel
robot.straight(1.20)  # Fahre geradeaus
robot.turn(-77.24)  # Endausrichtung

# Fahre von (159.38, 106.12) nach (159.38, 108.20)
robot.turn(99.31)  # Drehe in Richtung Ziel
robot.straight(2.08)  # Fahre geradeaus
robot.turn(-98.68)  # Endausrichtung

# Fahre von (159.38, 108.20) nach (159.99, 109.94)
robot.turn(79.36)  # Drehe in Richtung Ziel
robot.straight(1.84)  # Fahre geradeaus
robot.turn(-79.43)  # Endausrichtung

# Fahre von (159.99, 109.94) nach (162.45, 110.37)
robot.turn(18.66)  # Drehe in Richtung Ziel
robot.straight(2.50)  # Fahre geradeaus
robot.turn(-18.85)  # Endausrichtung

# Fahre von (162.45, 110.37) nach (163.23, 110.28)
robot.turn(2.36)  # Drehe in Richtung Ziel
robot.straight(0.79)  # Fahre geradeaus
robot.turn(-2.61)  # Endausrichtung

# Fahre von (163.23, 110.28) nach (164.14, 109.08)
robot.turn(-43.64)  # Drehe in Richtung Ziel
robot.straight(1.51)  # Fahre geradeaus
robot.turn(43.56)  # Endausrichtung

# Fahre von (164.14, 109.08) nach (166.04, 107.15)
robot.turn(-36.18)  # Drehe in Richtung Ziel
robot.straight(2.71)  # Fahre geradeaus
robot.turn(35.91)  # Endausrichtung

# Fahre von (166.04, 107.15) nach (167.77, 105.93)
robot.turn(-25.65)  # Drehe in Richtung Ziel
robot.straight(2.12)  # Fahre geradeaus
robot.turn(25.01)  # Endausrichtung

# Fahre von (167.77, 105.93) nach (169.97, 105.51)
robot.turn(-0.63)  # Drehe in Richtung Ziel
robot.straight(2.24)  # Fahre geradeaus
robot.turn(0.21)  # Endausrichtung

# Fahre von (169.97, 105.51) nach (172.57, 105.64)
robot.turn(13.46)  # Drehe in Richtung Ziel
robot.straight(2.60)  # Fahre geradeaus
robot.turn(-13.92)  # Endausrichtung

# Fahre von (172.57, 105.64) nach (175.05, 106.04)
robot.turn(20.22)  # Drehe in Richtung Ziel
robot.straight(2.51)  # Fahre geradeaus
robot.turn(-21.17)  # Endausrichtung

# Fahre von (175.05, 106.04) nach (177.34, 105.71)
robot.turn(3.81)  # Drehe in Richtung Ziel
robot.straight(2.31)  # Fahre geradeaus
robot.turn(-4.38)  # Endausrichtung

# Fahre von (177.34, 105.71) nach (180.86, 105.81)
robot.turn(14.21)  # Drehe in Richtung Ziel
robot.straight(3.52)  # Fahre geradeaus
robot.turn(-15.37)  # Endausrichtung

# Fahre von (180.86, 105.81) nach (185.13, 106.60)
robot.turn(24.22)  # Drehe in Richtung Ziel
robot.straight(4.34)  # Fahre geradeaus
robot.turn(-22.62)  # Endausrichtung

# Fahre von (185.13, 106.60) nach (188.76, 106.88)
robot.turn(16.55)  # Drehe in Richtung Ziel
robot.straight(3.64)  # Fahre geradeaus
robot.turn(-15.22)  # Endausrichtung

# Fahre von (188.76, 106.88) nach (192.24, 107.71)
robot.turn(24.22)  # Drehe in Richtung Ziel
robot.straight(3.58)  # Fahre geradeaus
robot.turn(-26.77)  # Endausrichtung

# Fahre von (192.24, 107.71) nach (194.35, 107.67)
robot.turn(12.27)  # Drehe in Richtung Ziel
robot.straight(2.11)  # Fahre geradeaus
robot.turn(-11.32)  # Endausrichtung

# Fahre von (194.35, 107.67) nach (195.02, 109.28)
robot.turn(79.82)  # Drehe in Richtung Ziel
robot.straight(1.74)  # Fahre geradeaus
robot.turn(-75.73)  # Endausrichtung

# Fahre von (195.02, 109.28) nach (196.38, 107.79)
robot.turn(-39.29)  # Drehe in Richtung Ziel
robot.straight(2.02)  # Fahre geradeaus
robot.turn(42.89)  # Endausrichtung

# Fahre von (196.38, 107.79) nach (198.67, 107.42)
robot.turn(-4.46)  # Drehe in Richtung Ziel
robot.straight(2.32)  # Fahre geradeaus
robot.turn(6.08)  # Endausrichtung

# Fahre von (198.67, 107.42) nach (200.80, 107.60)
robot.turn(7.93)  # Drehe in Richtung Ziel
robot.straight(2.14)  # Fahre geradeaus
robot.turn(-6.28)  # Endausrichtung

# Fahre von (200.80, 107.60) nach (202.37, 108.12)
robot.turn(19.78)  # Drehe in Richtung Ziel
robot.straight(1.65)  # Fahre geradeaus
robot.turn(-18.75)  # Endausrichtung

# Fahre von (202.37, 108.12) nach (203.30, 107.27)
robot.turn(-42.01)  # Drehe in Richtung Ziel
robot.straight(1.26)  # Fahre geradeaus
robot.turn(44.11)  # Endausrichtung

# Fahre von (203.30, 107.27) nach (206.28, 107.36)
robot.turn(0.05)  # Drehe in Richtung Ziel
robot.straight(2.98)  # Fahre geradeaus
robot.turn(-3.15)  # Endausrichtung

# Fahre von (206.28, 107.36) nach (213.03, 106.26)
robot.turn(-7.84)  # Drehe in Richtung Ziel
robot.straight(6.84)  # Fahre geradeaus
robot.turn(5.93)  # Endausrichtung

# Fahre von (213.03, 106.26) nach (212.91, 107.85)
robot.turn(97.65)  # Drehe in Richtung Ziel
robot.straight(1.59)  # Fahre geradeaus
robot.turn(-97.09)  # Endausrichtung

# Fahre von (212.91, 107.85) nach (172.22, 111.81)
robot.turn(177.21)  # Drehe in Richtung Ziel
robot.straight(40.88)  # Fahre geradeaus
robot.turn(-177.67)  # Endausrichtung

# Fahre von (172.22, 111.81) nach (166.46, 113.37)
robot.turn(168.08)  # Drehe in Richtung Ziel
robot.straight(5.97)  # Fahre geradeaus
robot.turn(-168.70)  # Endausrichtung

# Fahre von (166.46, 113.37) nach (163.38, 114.81)
robot.turn(158.79)  # Drehe in Richtung Ziel
robot.straight(3.40)  # Fahre geradeaus
robot.turn(-157.70)  # Endausrichtung

# Fahre von (163.38, 114.81) nach (162.40, 115.24)
robot.turn(159.07)  # Drehe in Richtung Ziel
robot.straight(1.07)  # Fahre geradeaus
robot.turn(-158.66)  # Endausrichtung

# Fahre von (162.40, 115.24) nach (161.05, 114.27)
robot.turn(-141.95)  # Drehe in Richtung Ziel
robot.straight(1.66)  # Fahre geradeaus
robot.turn(141.29)  # Endausrichtung

# Fahre von (161.05, 114.27) nach (160.50, 113.19)
robot.turn(-113.98)  # Drehe in Richtung Ziel
robot.straight(1.21)  # Fahre geradeaus
robot.turn(112.96)  # Endausrichtung

# Fahre von (160.50, 113.19) nach (161.71, 111.78)
robot.turn(-45.34)  # Drehe in Richtung Ziel
robot.straight(1.86)  # Fahre geradeaus
robot.turn(45.78)  # Endausrichtung

# Fahre von (161.71, 111.78) nach (160.85, 111.22)
robot.turn(-143.34)  # Drehe in Richtung Ziel
robot.straight(1.03)  # Fahre geradeaus
robot.turn(144.00)  # Endausrichtung

# Fahre von (160.85, 111.22) nach (157.69, 111.76)
robot.turn(173.23)  # Drehe in Richtung Ziel
robot.straight(3.21)  # Fahre geradeaus
robot.turn(-174.86)  # Endausrichtung

# Fahre von (157.69, 111.76) nach (155.47, 111.86)
robot.turn(-178.02)  # Drehe in Richtung Ziel
robot.straight(2.22)  # Fahre geradeaus
robot.turn(178.75)  # Endausrichtung

# Fahre von (155.47, 111.86) nach (152.63, 112.11)
robot.turn(178.80)  # Drehe in Richtung Ziel
robot.straight(2.85)  # Fahre geradeaus
robot.turn(-179.29)  # Endausrichtung

# Fahre von (152.63, 112.11) nach (150.10, 112.00)
robot.turn(-173.19)  # Drehe in Richtung Ziel
robot.straight(2.53)  # Fahre geradeaus
robot.turn(172.56)  # Endausrichtung

# Fahre von (150.10, 112.00) nach (148.08, 113.09)
robot.turn(156.60)  # Drehe in Richtung Ziel
robot.straight(2.30)  # Fahre geradeaus
robot.turn(-155.55)  # Endausrichtung

# Fahre von (148.08, 113.09) nach (146.52, 113.94)
robot.turn(155.32)  # Drehe in Richtung Ziel
robot.straight(1.78)  # Fahre geradeaus
robot.turn(-156.41)  # Endausrichtung

# Fahre von (146.52, 113.94) nach (146.57, 110.52)
robot.turn(-84.17)  # Drehe in Richtung Ziel
robot.straight(3.42)  # Fahre geradeaus
robot.turn(83.69)  # Endausrichtung

# Fahre von (146.57, 110.52) nach (148.12, 106.75)
robot.turn(-62.18)  # Drehe in Richtung Ziel
robot.straight(4.08)  # Fahre geradeaus
robot.turn(61.07)  # Endausrichtung

# Fahre von (148.12, 106.75) nach (148.50, 105.02)
robot.turn(-71.03)  # Drehe in Richtung Ziel
robot.straight(1.77)  # Fahre geradeaus
robot.turn(70.76)  # Endausrichtung

# Fahre von (148.50, 105.02) nach (146.81, 102.79)
robot.turn(-120.31)  # Drehe in Richtung Ziel
robot.straight(2.80)  # Fahre geradeaus
robot.turn(120.51)  # Endausrichtung

# Fahre von (146.81, 102.79) nach (145.62, 100.94)
robot.turn(-116.10)  # Drehe in Richtung Ziel
robot.straight(2.20)  # Fahre geradeaus
robot.turn(114.72)  # Endausrichtung

# Fahre von (145.62, 100.94) nach (143.72, 99.62)
robot.turn(-137.18)  # Drehe in Richtung Ziel
robot.straight(2.31)  # Fahre geradeaus
robot.turn(137.99)  # Endausrichtung

# Fahre von (143.72, 99.62) nach (138.74, 99.49)
robot.turn(-171.28)  # Drehe in Richtung Ziel
robot.straight(4.98)  # Fahre geradeaus
robot.turn(171.41)  # Endausrichtung

# Fahre von (138.74, 99.49) nach (134.36, 98.98)
robot.turn(-166.27)  # Drehe in Richtung Ziel
robot.straight(4.41)  # Fahre geradeaus
robot.turn(166.55)  # Endausrichtung

# Fahre von (134.36, 98.98) nach (131.24, 99.53)
robot.turn(176.81)  # Drehe in Richtung Ziel
robot.straight(3.17)  # Fahre geradeaus
robot.turn(-177.26)  # Endausrichtung

# Fahre von (131.24, 99.53) nach (131.35, 99.99)
robot.turn(83.81)  # Drehe in Richtung Ziel
robot.straight(0.47)  # Fahre geradeaus
robot.turn(-84.03)  # Endausrichtung

# Fahre von (131.35, 99.99) nach (131.36, 100.23)
robot.turn(95.09)  # Drehe in Richtung Ziel
robot.straight(0.24)  # Fahre geradeaus
robot.turn(-95.57)  # Endausrichtung

# Fahre von (131.36, 100.23) nach (131.24, 100.01)
robot.turn(-110.65)  # Drehe in Richtung Ziel
robot.straight(0.25)  # Fahre geradeaus
robot.turn(111.42)  # Endausrichtung

# Fahre von (131.24, 100.01) nach (131.36, 100.11)
robot.turn(47.00)  # Drehe in Richtung Ziel
robot.straight(0.16)  # Fahre geradeaus
robot.turn(-47.22)  # Endausrichtung

# Fahre von (131.36, 100.11) nach (131.57, 100.34)
robot.turn(55.01)  # Drehe in Richtung Ziel
robot.straight(0.31)  # Fahre geradeaus
robot.turn(-55.07)  # Endausrichtung

# Fahre von (131.57, 100.34) nach (131.21, 100.43)
robot.turn(173.43)  # Drehe in Richtung Ziel
robot.straight(0.37)  # Fahre geradeaus
robot.turn(-173.79)  # Endausrichtung

# Fahre von (131.21, 100.43) nach (131.30, 100.00)
robot.turn(-70.35)  # Drehe in Richtung Ziel
robot.straight(0.44)  # Fahre geradeaus
robot.turn(71.23)  # Endausrichtung

# Fahre von (131.30, 100.00) nach (131.87, 99.44)
robot.turn(-37.54)  # Drehe in Richtung Ziel
robot.straight(0.80)  # Fahre geradeaus
robot.turn(39.95)  # Endausrichtung

# Fahre von (131.87, 99.44) nach (131.26, 100.37)
robot.turn(127.80)  # Drehe in Richtung Ziel
robot.straight(1.11)  # Fahre geradeaus
robot.turn(-129.56)  # Endausrichtung

# Fahre von (131.26, 100.37) nach (131.06, 100.49)
robot.turn(155.34)  # Drehe in Richtung Ziel
robot.straight(0.23)  # Fahre geradeaus
robot.turn(-155.80)  # Endausrichtung

# Fahre von (131.06, 100.49) nach (130.94, 100.52)
robot.turn(172.72)  # Drehe in Richtung Ziel
robot.straight(0.12)  # Fahre geradeaus
robot.turn(-172.61)  # Endausrichtung

# Fahre von (130.94, 100.52) nach (131.05, 101.40)
robot.turn(89.52)  # Drehe in Richtung Ziel
robot.straight(0.89)  # Fahre geradeaus
robot.turn(-90.72)  # Endausrichtung

# Fahre von (131.05, 101.40) nach (132.46, 101.88)
robot.turn(26.65)  # Drehe in Richtung Ziel
robot.straight(1.49)  # Fahre geradeaus
robot.turn(-29.34)  # Endausrichtung

# Fahre von (132.46, 101.88) nach (134.39, 100.32)
robot.turn(-28.41)  # Drehe in Richtung Ziel
robot.straight(2.48)  # Fahre geradeaus
robot.turn(27.66)  # Endausrichtung

# Fahre von (134.39, 100.32) nach (134.62, 100.73)
robot.turn(72.00)  # Drehe in Richtung Ziel
robot.straight(0.47)  # Fahre geradeaus
robot.turn(-69.86)  # Endausrichtung

# Fahre von (134.62, 100.73) nach (159.40, 73.04)
robot.turn(-39.02)  # Drehe in Richtung Ziel
robot.straight(37.16)  # Fahre geradeaus
robot.turn(-174.96)  # Endausrichtung

# Fahre von (159.40, 73.04) nach (134.81, 104.96)
robot.turn(-9.26)  # Drehe in Richtung Ziel
robot.straight(40.29)  # Fahre geradeaus
robot.turn(-144.40)  # Endausrichtung

# Fahre von (134.81, 104.96) nach (139.24, 61.68)
robot.turn(-67.37)  # Drehe in Richtung Ziel
robot.straight(43.51)  # Fahre geradeaus
robot.turn(-57.68)  # Endausrichtung

# Fahre von (139.24, 61.68) nach (137.30, 61.44)
robot.turn(-31.11)  # Drehe in Richtung Ziel
robot.straight(1.95)  # Fahre geradeaus
robot.turn(36.92)  # Endausrichtung

# Fahre von (137.30, 61.44) nach (148.51, 74.69)
robot.turn(-174.20)  # Drehe in Richtung Ziel
robot.straight(17.36)  # Fahre geradeaus
robot.turn(142.17)  # Endausrichtung

# Fahre von (148.51, 74.69) nach (128.62, 66.55)
robot.turn(10.32)  # Drehe in Richtung Ziel
robot.straight(21.49)  # Fahre geradeaus
robot.turn(142.41)  # Endausrichtung

# Fahre von (128.62, 66.55) nach (186.75, 3.23)
robot.turn(-32.12)  # Drehe in Richtung Ziel
robot.straight(85.96)  # Fahre geradeaus
robot.turn(-165.30)  # Endausrichtung

# Fahre von (186.75, 3.23) nach (163.44, 45.16)
robot.turn(-28.18)  # Drehe in Richtung Ziel
robot.straight(47.97)  # Fahre geradeaus
robot.turn(71.39)  # Endausrichtung