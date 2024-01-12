# from random import *
#
# arv=randint(0,100)  #juhuslik raisarv vahemikust 0...100
# print(arv)
# if arv%2==0:
#     print(arv, "on paaris arv")
# else:
#     print(arv, "on paaritu arv")
# print()



# from random import *
# protsent=randint(-100, 500) #0-100   0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"
# print(protsent,"% on testi tulemus")
# if protsent<0 or protsent>100:
#     tulemus="Valed andmed"
# elif protsent>0 and protsent<60:
#     tulemus="hinne 2"
# elif protsent<=60 and protsent>75:
#     tulemus="hinne 3"
# elif protsent<=75 and protsent>90:
#     tulemus="hinne 4"
# elif protsent<=90 and protsent>=100:
#     tulemus="hinne 5"
# print(tulemus)

# print("tund on alanu")
# hilinemine=input("Kas õpilane on hilinenud?")
# # "JAH"-a.upper() ,"jah"-a.lower(), "Jah"-a.capitaliza(), jAH
# if hilinemine.upper()=="JAH":
#     print("Õpilane ootab 30 min")
# print("Õpilane astub klassi")

        #1
nimi = input("Mis on su nimi?").capitalize()
print("Tere,", nimi)
if nimi == "Juku":
    print("Lähme kinno")
    vanus=(input("Kui vana sa oled?"))
    vanus=int(vanus)
    if vanus<0 or vanus>100:
        pilet="Viga"
    elif vanus<=6:
        pilet="Tasuta"
    elif vanus<=14:
        pilet= "Lastepilet"
    elif vanus<65:
        pilet="taispilet"
    elif vanus<=100:
        pilet = "sooduspilet"
    print(pilet)
else:
    print("Ma ootan Jukut")
