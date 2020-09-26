from sys import exit #exit bo daxstne le excute w derchwn
from sys import argv

script, naw = argv

print("Sllaw {} yaryeke dest pe dekat".format(naw))

def jwreke():
    print("Lem jwrewe destpedekeyt")
    print("Lerewe detwanyt bgeyt be Alltwneke")
    print("Detwanyt Dw Helbjarde bkey bo geyshtn be Alltwn")
    print("Jwry Rast & Jwry beramber")
    dyarykrdn = input("> ")
    if dyarykrdn == "Jwry Rast":
        Jwry_Rast()
    elif dyarykrdn == "Jwry beramber":
        Jwry_Beramber()
    else:
        print("Kes nazane to cht gerek? ")

def Jwry_Rast():
    print("Lere Shtek heLbjere le 0 bo 100 Kg")
    print("Chend kilot dewet?")
    dyarykrdn = input("> ")
    try:
        Chend = int(dyarykrdn)
    except ValueError:
        print("Jmare dabne kake gyan, Alttwn nawe?")

    if Chend > 50:
        print("Piroze To {} kilo Alltwnt brdewe bo mall".format(Chend))
    elif Chend < 50:
        print("Dysan pyroze {} Kilo alltwnt brdewe".format(Chend))
    else:
        print("Bexwa Shayeny hych nit, Dorryay")

def Jwry_Beramber():
    print("Hengaweky basht le peshe bo bedesthenany Alltwneke")
    print("Lere zor Wryabe")
    print("3 cor jwr heye kamyant dewe?")

    dyarykrdn = input("> ")
    try:
        kame = int(dyarykrdn)
    except ValueError:
        print("Tkaye jmare bnwse")
    if kame == 1:
        print("Jwrekey tr mawe le pesht, Alttwny zort dewe yan kem?")
        dyarykrdn = input("> ")
        # le if w elif dw shewazm bekarhenawa bo nardny value. herdwky debet.
        if dyarykrdn == "kem": 
            print("Pyroze ALttwneket brdewe, bLema zor nye xot bzane chende")
        elif "zor" in dyarykrdn:
            print("Pyroze brreky zor alltwnt bo derchw, Teqyt")
        else:
            exit(0)
    elif kame == 2: 
        print("To Shanseket bogene")
        mrdn("Yekser dechyte derewe w hych bedest naheneyt")
    
    elif kame == 3:
        print("Dw bjardet heye, tameaht zore yan temaht keme? ")
        dyarykrdn = input("> ")
        if "zore" in dyarykrdn or "zor" in dyarykrdn:
            print("Temaht zore boye hycht bo bedest nehat")
        elif "kem" in dyarykrdn or "keme" in dyarykrdn:
            mrdn("Temaht nye boye ewe hallte")
        else:
            exit(0) #Her katek else hy4 swdkey nebw karygery nebw leser kodeke detwany exit(0) dabney
    else:
        mrdn("brro bo chem")
        

def mrdn(bochy):
    print(bochy, "Serkewtw byt berrezm! Eger nemrdbety")
    exit(0)

def kotayi_yaryeke():
    print("Yaryeke kotayi hat berrez {} Detwanyt dwwbare hewll bdeytewe".format(naw))
jwreke()
kotayi_yaryeke()