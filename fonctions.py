from dictionnaire import ville

distancetotal = 0
distance = 0
vitesse = 0
tempstrajet = 0
tempstotal = 0
heure = 0
minute = 0

def infoville():
    global villedep, villearr
    villedep = input("ville de départ : ")
    villearr = input("ville d'arrivée : ")
    return villedep, villearr

def distanceville():
    global distancetotal, distance
    distance = ville[villedep][villearr]
    distancetotal = distance
    

def acceleration():
    global vitesse, tempstrajet, tempstotal, distance
    while vitesse < 90:
        vitesse += 10
        tempstrajet += 1
        tempstotal += 1
        distance -= 7.5

def freinage():
    global vitesse, tempstrajet, tempstotal, distance
    while vitesse != 0:
        vitesse -= 10
        tempstrajet += 1
        tempstotal += 1
        distance -= 7.5

def pause():
    global tempstotal
    if tempstrajet%120 == 0:
        freinage()
        tempstotal += 15
        acceleration()

if __name__ == '__main__':
    infoville()
    distanceville()
    acceleration()
    while distance > 7.5:
        tempstrajet += 1
        tempstotal += 1
        distance -= 1.5
        pause()
    freinage()
    heure = tempstotal // 60
    minute = tempstotal % 60
    print(f"""
--------------------------------------
Ville de départ : |{villedep}
--------------------------------------
Ville d'arrivée : |{villearr}
--------------------------------------
Distance totale : |{distancetotal}/km
--------------------------------------
Temps:            |{heure} : {minute}
--------------------------------------
    """)