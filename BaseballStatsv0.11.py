#baseball-stats-2018
#Hitters only rn
PORB = str(input("Welcome to Karl Gausman's lazy baseball stats calculator version 1.00, would you like to calculate a Pitcher's or batter's stats? "))
if PORB == "Batter" or "batter":
#   base stats
    # Implement single line input later
    AB = int(input("Please input the number of At-Bats the player had"))
    PA = int(input("PLease input the number of Plate Appearances"))
    BB = int(input("Please input the number of Walks"))
    K = int(input("Please input the number of stirkeouts"))
    IBB = int(input("Please input the number of Intentional Walks"))
    SF = int(input("Please input the number of Sac-Flys"))
    HBP = int(input("Please input the number of Hit by Pitches"))
    HITS = int(input("Please input the number of hits the batter had"))
    sing = int(input("Please input the number of singles"))
    doub = int(input("Please input the number of doubles"))
    trip = int(input("Please input the number of triples"))
    HR = int(input("Please input the number of Home Runs the player hit"))
#   Adv Stats
    BA = HITS / AB
    BBper = BB / PA
    Kper = K/PA
    SLG = ((trip * 3)+(doub * 2)+ sing) / AB
    ISO = SLG - BA
    BABIP = (HITS - HR)/(AB + BB + HBP + SF)
    WRC = ((wOBA - .315)/1.226) + (.117/PA)*PA
    wOBA = (.69 * BB + .722 * HBP + .888 * sing + 1.271 * doub + 1.616 * trip + 2.101 * HR)/(AB + BB - IBB + SF + HBP)
    #Graphic should be included
if PORB != "Batter" or "batter": print("That is not implemented yet")
# Pitchers to be added later 

