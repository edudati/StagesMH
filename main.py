""" This is the creation of a sequence of falls for MoveHero game - offline version -
It's look like the online version and you can see how it works in www.movehero.com.br

Developed at the School of Arts Sciences and Humanities of the University of São Paulo (EACH-USP). The game presents balls that fall, in four imaginary columns on the computer screen, within limits of interval between the falls and distribution between the columns predetermined by the researcher. The task is not to let balls fall. However, the balls can only be touched when they reach four circles placed parallel (in two height levels), two to the left and two to the right of the participant
(0 0 \o/ 0 0). Named targets 1, 2, 3 and 4, as viewed from left to right. The game captures the participant's movements through a webcam, not requiring physical contact to perform the task,

Later, when the configuration is approved by the researcher, the last line will be used to create a json file, in the format that the offline game reads
"""

""" --------- THE MAIN VARIABLES ---------
timeGame =      Time of game in seconds
minInt =        Minimun interval between balls in seconds
maxInt =        Maximum interval between balls in seconds
collumns[] =    DO NOT CHANGE. Are the collumns of the game
wights[] =      Estimated % of distribution of balls per collumns (the sum of 4 collumns must be 100%)
canRepeat = False:  No more than 2 balls falling in same collumn in sequence.
            True:   The balls can repeat falling in same collumn in sequence.
delayRepeated = If the ball will fall in the same collumn of the previus,
                the time interval will be multiplied per 'delayRepeated'
                eg.: if the interval time of the repeated ball is 1.35 sec and delayRepeated is 0.8. 
                    The real interval will be 1.08 sec (1.35 * 0.8) that is, the ball will take less time to fall.
delayOposite =  If the ball will fall in the oposite corner of the previus (col 1 and 5) (col 5 and 1), 
                the time interval can be multiplied per 'delayOposite'
                eg.: if interval time of the ball falling in the oposite corner is 1.35 se and delayOposite is 1.6. 
                The real interval will be 2.16 sec (1.35 * 1.6) that is, the ball will take more time to fall.
"""

import random

timeGame = int(180)
minInt = float(1.12)
maxInt = float(1.93)
collumns = [1, 2, 3, 4]
weights = [15, 35, 35, 15]
canRepeat = False
delayRepeated = 1
delayOposite = 1

totalBalls = int(timeGame / ((maxInt + minInt) / 2))

"""Populate sequence of balls"""
ballsSequence = random.choices(collumns, weights, k=totalBalls)

"""Discard collumn with 0% of falls"""
validPositions = []
for i in range(len(weights)):
    if weights[i] != 0:
        validPositions.append(collumns[i])

"""Change sequence of falls for repeated balls"""
if not canRepeat:
    for i in range(2, len(ballsSequence)):
        while True:
            if ballsSequence[i] == ballsSequence[i - 1] == ballsSequence[i - 2]:
                ballsSequence[i] = validPositions[random.randint(0, len(validPositions) - 1)]
            else:
                break

timeNow = 0
timesP1 = []
timesP2 = []
timesP3 = []
timesP4 = []

"""Insert times for each collumn"""
for ball in range(len(ballsSequence)):
    """Apply a randon value between min and max permited intervals"""
    addTime = round(random.uniform(minInt, maxInt), 2)

    if ball > 0:
        """Apply delay or antecipation for repeated balls"""
        if ballsSequence[ball] == ballsSequence[ball - 1]:
            addTime = addTime * delayRepeated

        """Apply delay or antecipation for oposite balls"""
        if (ballsSequence[ball] == 1 and ballsSequence[ball -1] == 5) \
                or (ballsSequence[ball] == 5 and ballsSequence[ball -1] == 1):
            addTime = addTime * delayOposite
    timeNow = round(timeNow + addTime, 2)

    """Populate the sequence of each collumn"""
    if ballsSequence[ball] == 1:
        timesP1.append(timeNow)
    elif ballsSequence[ball] == 2:
        timesP2.append(timeNow)
    elif ballsSequence[ball] == 3:
        timesP3.append(timeNow)
    else:
        timesP4.append(timeNow)

"""Create variables for report totals and % """
totalBalls = len(ballsSequence)
totalP1 = totalP2 = totalP3 = totalP4 = 0
# populate total per position
for ball in ballsSequence:
    if ball == 1:
        totalP1 += 1
    elif ball == 2:
        totalP2 += 1
    elif ball == 3:
        totalP3 += 1
    else:
        totalP4 += 1

timeGame = timeNow

internalBalls = totalP2 + totalP3
externalBalls = totalP1 + totalP4
leftBalls = totalP1 + totalP2
rightBalls = totalP3 + totalP4

percP1 = totalP1 / totalBalls
percP2 = totalP2 / totalBalls
percP3 = totalP3 / totalBalls
percP4 = totalP4 / totalBalls

percInternalBalls = internalBalls / totalBalls
percExternalBalls = externalBalls / totalBalls
percLeftBalls = leftBalls / totalBalls
percRightBalls = rightBalls / totalBalls

"""REPORTS"""
print("Sequence of falls: ", ballsSequence)

print("\n=== TOTALS ===\n")
print("Time of game in seconds: ", round(timeNow))
print("Total of balls: {}\n".format(totalBalls))
print("Position 1:      {}".format(totalP1))
print("Position 2:      {}".format(totalP2))
print("Position 3:      {}".format(totalP3))
print("Position 4:      {}\n".format(totalP4))
print("Left side:       {}".format(leftBalls))
print("Right side:      {}\n".format(rightBalls))
print("Internal balls:  {}".format(internalBalls))
print("External balls:  {}".format(externalBalls))

print("\n===PERCENTAGES===\n")
print("% P1: {:.2f}".format(percP1 * 100))
print("% P2: {:.2f}".format(percP2 * 100))
print("% P3: {:.2f}".format(percP3 * 100))
print("% P4: {:.2f}\n".format(percP4 * 100))

print("Internal/External:   {:.2f}% / {:.2f}%".format((percInternalBalls * 100), (percExternalBalls * 100)))
print("Left/Right:          {:.2f}% / {:.2f}%\n".format((percLeftBalls * 100), (percRightBalls * 100)))

print("\nCopy below this line and paste it into the json file to build the notes:")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
print('["",{},\n{},\n{},\n{}]'.format(timesP1, timesP2, timesP3, timesP4))
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")



