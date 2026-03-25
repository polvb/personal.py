import random as r

def createPK(l):
    PK = ""
    i = 0
    while (i < l):
        rn = r.randint(0, 1)
        rl = chr(rng[rn][r.randint(0, len(rng[rn])-1)])
        PK += rl
        i += 1
    return PK

rng = [list(range(48, 58)), list(range(65, 91))]
users = []
while(True):
    sn = input("Do you want to be an user? s/n: ")
    if (sn == 's'):
        PK = createPK(4)
        while(PK in users):
            PK = createPK(4);
        print(PK)
        users.append(PK)
    else:
        print(users)
        break
