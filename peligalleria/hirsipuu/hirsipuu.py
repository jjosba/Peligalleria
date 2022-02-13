import random

def hirsipuu():
    #ukkeli + sanojen lataaminen
    ukkeli = ['(','ô','_','ô',')\n','<.','|','.>\n',' |',' |']

    with open ("hirsipuusanat.txt", "r", encoding='utf8' ) as tiedosto:
        sanat = {'helppo':[], 'haastava':[], 'vaikea':[]}
        for rivi in tiedosto:
            sana = rivi[:len(rivi)-1]
            if len(sana) <= 6:
                sanat['helppo'].append(sana)
            elif len(sana) >= 7 and len(sana) <= 15:
                sanat['haastava'].append(sana)
            else:
                sanat['vaikea'].append(sana)
            
    def peli():
        sananpituus = "-" * len(sana)
        yritys = 10
        arvatut = []
        arvattuoikein = []
        print("Sanan pituus on", len(sana), "kirjainta.")
        while True:
            arvattu = False
            print()
            arvaus = input("Ehdota kirjainta tai sanaa: ")
            if arvaus.isalpha():
                if len(arvaus) == 1:
                    if arvaus in arvatut or arvaus in arvattuoikein:
                        print("Olet jo arvannut tämän kirjaimen. ")
                    else:
                        if arvaus in sana:
                            arvattuoikein.append(arvaus)
                            kirjaimet = list(sananpituus)
                            m = [i for i, x in enumerate(sana) if x == arvaus]
                            for n in m:
                                kirjaimet[n] = arvaus
                            sananpituus = "".join(kirjaimet)
                        elif arvaus not in sana:
                            print(arvaus, "ei ole sanassa.")
                            yritys = yritys - 1
                            arvatut.append(arvaus)
                        else:
                            print("Anteeksi, en ymmärtänyt. ")
                elif len(arvaus) > 1:
                    if arvaus in arvatut:
                        print("Olet jo arvannut tämän sanan. ")
                    else:
                        if arvaus == sana:
                            print(f"Hienoa, arvasit sanan oikein! Se oli {sana}. Olet voittanut pelin!")
                            break
                        elif arvaus != sana:
                            print(arvaus, "ei ole oikea sana. ")
                            yritys = yritys - 1
                        else:
                            print("Anteeksi, en ymmärtänyt.")
            else:
                print("Ehdotuksesi ei ole kirjain. ")
            for i in ukkeli[:10-yritys]:
                print(i, end="")
            print()
            print(sananpituus)
            print()
            print(arvatut)
            if yritys == 0:
                print()
                print("Kuvio on piirretty kokonaan. Olet hävinnyt pelin.")
                break
            else:
                pass
            if "-" not in sananpituus:
                print(f"Hienoa, arvasit sanan oikein! Se oli {sana}. Olet voittanut pelin!")
                break
            else:
                pass

    while True:
        jooei = input("Haluatko lukea hirsipuun ohjeet ennen pelaamisen aloittamista? y = kyllä, n = ei ")
        if jooei == "y" :
            print('''Hirsipuun ohjeet:
Vaikeustason valittuasi ruudulle ilmestyy alaviivoja (_), jotka kuvastavat arvattavan
sanan kirjainten lukumäärää.Vaikeustasot helppo, haastava ja vaikea määrittyvät sanan
kirjainmäärän mukaan: helpoissa sanoissa on alle 7 kirjainta, haastavissa on 7-15 kirjainta
ja vaikeissa yli 15 kirjainta. Pelaaja ehdottaa kirjaimia, jotka saattavat esiintyä
sanassa. Jos pelaajan ehdottama kirjain esiintyy sanassa, kirjain ilmestyy niihin kohtiin,
joissa se sanassa esiintyy. Jos ehdotettu kirjain ei ole sanassa, ruudulle tulevaan kuvioon
lisätään elementti. Peli päättyy, kun pelaaja saa sanan valmiiksi, eli kun pelaaja arvaa
joko kaikki sanassa esiintyvät kirjaimet tai koko sanan oikein, jolloin pelaaja voittaa
tai koko kuvio ollaan saatu piirrettyä (10 elementtiä), jolloin pelaaja häviää.
Nyt voimme aloittaa pelin!
''')
            break
        if jooei == "n":
            print("Hienoa. Aloitetaan peli!")
            break
        else:
            print("Et vastannut, haluatko lukea ohjeet.")

    #vaikeustason valinta, ei jostain syystä suostunut toimimaan metodina
    while True:
        taso = int(input("Minkä vaikeustason haluat valita: 1 = helppo, 2 = haastava vai 3 = vaikea? "))
        if taso == 1:
            sana = random.choice(sanat['helppo'])
            for i in range(len(sana)):
                print("-", end = '')
            break
        elif taso == 2:
            sana = random.choice(sanat['haastava'])
            for i in range(len(sana)):
                print("-", end = '')
            break
        elif taso == 3:
            sana = random.choice(sanat['vaikea'])
            for i in range(len(sana)):
                print("-", end = '')
            break
        else:
            print("Et valinnut vaikeustasoa. Valitse vaikeustaso uudelleen: ")

    print()
    print(sana) #testisyistä

    peli()

'''
print('Hyvin pelattu!')
while True:
    uusi = input("Haluatko pelata uudelleen? y = Kyllä, n = Ei. ")
        if uusi == "y":
        import hirsipuu
    elif uusi == "n":
        print("Selvä! Palataan takaisin peliaulaan. ")
    else:
        print("Anteeksi, en ymmärtänyt.")
'''
hirsipuu()
