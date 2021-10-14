from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

robotArm.speed = 2

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()

robotArm.wait()