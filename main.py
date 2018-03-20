from math import sqrt
import random
from decimal import Decimal
def luminanceDifference(color1,color2):
    #Formula: sqrt( 0.241*R^2 + 0.691*G^2 + 0.068*B^2 ) from http://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx
    r,g,b = color1[0],color1[1],color1[2]
    r2,g2,b2 = color2[0],color2[1],color2[2]
    luminanceC1 = Decimal(str(sqrt(0.241*(r**2)+.691*(g**2)+.068*(b**2))))
    luminanceC2 = Decimal(str(sqrt(0.241*(r2**2)+.691*(g2**2)+.068*(b2**2))))
    return int(abs(Decimal(luminanceC1-luminanceC2)/255)*100)
def checkForReadability(differential,readabilityTable):
    for key,value in readabilityTable.items():
        if differential >= value[0] and differential <= value[1]:
            return (key,value)


readabilityTable = {"Horrible":(0,10),"Very Bad":(11,20),"Pretty Bad":(21,30),"Bad":(31,44),"Mediocre":(45,54),
                    "Good":(55,65),"Very Good":(65,74),"Great":(75,89),"Near Perfect":(90,99),"Perfect":(100,100)}
while True:
    random.seed()
    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    random.seed()
    r2,g2,b2 = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    diff = luminanceDifference([r,g,b],[r2,g2,b2])
    print("------------------------------------------------------------------")
    print("First color: " + str(r) + "," + str(g) + "," + str(b))
    print("Second color: " + str(r2) + "," + str(g2) + "," + str(b2) + "\n")
    print("The colors have a "+str(diff)+"% weighted luminance differential.\n")
    readability = checkForReadability(diff,readabilityTable)
    print("This text has a readbility rating of '" + readability[0] + "'.")
    input("Enter to do it again!")
