from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(0,7):
    robotArm.grab()
    for i in range(0,8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(0,8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()