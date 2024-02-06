from sr.robot3 import *

robot = Robot()
mts = robot.motor_board.motors
arduino = robot.arduino

while True:
    mts[0].power = 0.1
    mts[1].power = 0.1
    distance = arduino.command("e") # Uses 'e' command to read distance
    print(distance) # Prints cumulative distance
    robot.sleep(0.1)
