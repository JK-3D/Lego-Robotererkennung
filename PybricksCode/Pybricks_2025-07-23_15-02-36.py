from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

robot.turn(-11)
robot.turn(-176)
robot.turn(-176)
robot.turn(-171)
robot.turn(135)
robot.turn(-62)
robot.turn(-113)
robot.turn(-54)
robot.turn(-40)
robot.turn(-76)
robot.turn(-75)
robot.turn(-78)
robot.turn(-75)
robot.turn(-71)
robot.turn(-35)
robot.turn(-29)
robot.turn(-37)
robot.turn(5)
robot.straight(2)
robot.straight(3)
robot.turn(14)
robot.straight(8)
robot.turn(32)
robot.straight(3)
robot.straight(1)
robot.turn(-9)
robot.turn(22)
robot.turn(69)