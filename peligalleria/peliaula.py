##PELIAULA

import json
import re
from operator import itemgetter
import random

def hirsipuu(peli):
    #ukkeli + sanojen lataaminen
    ukkeli = ['(','ô','_','ô',')\n','<.','|','.>\n',' |',' |']

    #sanat netistä, siirretty txt-tiedostoon
    with open ("hirsipuusanat.txt", "r", encoding='utf8' ) as tiedosto:
        sanat = {'helppo':[], 'haastava':[], 'vaikea':[]}
        for rivi in tiedosto:
            sana = rivi[:len(rivi)-1]
            if len(sana) <= 7:
                sanat['helppo'].append(sana)
            elif len(sana) >= 8 and len(sana) <= 15:
                sanat['haastava'].append(sana)
            else:
                sanat['vaikea'].append(sana)

    #itse peli, käyttää vaikeustason valinnassa valittua sanaa
    def pelataan():
        sananpituus = "-" * len(sana)
        yritys = 10 #tarvitaan hahmon kokoamiseen
        arvatut = []
        arvattuoikein = []
        print("Sanan pituus on", len(sana), "kirjainta.") #jos pitkä sana, hyvä laskea valmiiksi
        while True:
            print()
            arvaus = input("Ehdota kirjainta tai sanaa: ")
            if arvaus.isalpha():
                if len(arvaus) == 1:
                    if arvaus in arvatut or arvaus in arvattuoikein:
                        print("Olet jo arvannut tämän kirjaimen. ")
                    else:
                        if arvaus in sana:
                            arvattuoikein.append(arvaus)
                            kirjaimet = list(sananpituus) #tästä alkaa viivojen korvaaminen kirjaimilla
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
                            print()
                            print(f"Hienoa, arvasit sanan oikein! Se oli {sana}. Olet voittanut pelin!")
                            break
                        elif arvaus != sana:
                            print(arvaus, "ei ole oikea sana. ")
                            arvatut.append(arvaus)
                            yritys = yritys - 1
                        else:
                            print("Anteeksi, en ymmärtänyt.")
            else:
                print("Ehdotuksesi ei ole kirjain. ")
            if 10-yritys != 0: #tämä laitettiin, että tulee hyvä määrä välejä kaikissa tilanteissa
                print()
                for i in ukkeli[:10-yritys]: #listasta piirretään väärien vastausten (menneiden yritysten) mukaan kuviota
                    print(i, end="")
                print()
                print()
            else:
                print()
            print(sananpituus)
            print()
            print(arvatut) #näyttää pelaajalle väärin arvatut kirjaimet ja sanat
            if yritys == 0:
                print()
                print(f"Kuvio on piirretty kokonaan. Oikea sana oli {sana}. Olet hävinnyt pelin.")
                peli['voittaja'] = 'häviö' #tarvitaan scoreboardin pisteytykseen
                print(peli)
                break
            else:
                pass
            if "-" not in sananpituus:
                print()
                print(f"Hienoa, arvasit sanan oikein! Se oli {sana}. Olet voittanut pelin!")
                peli['voittaja'] = peli['pelaajat'] 
                print(peli)
                break
            else:
                pass
            
	#ohjeet
    while True:
        jooei = input("Haluatko lukea hirsipuun ohjeet ennen pelaamisen aloittamista? kyllä/ei ")
        if jooei == "kyllä" :
            print('''
Hirsipuun ohjeet:

Vaikeustason valittuasi ruudulle ilmestyy alaviivoja (_),
jotka kuvastavat arvattavan sanan kirjainten lukumäärää.
Vaikeustasot helppo, haastava ja vaikea määrittyvät sanan
kirjainmäärän mukaan: helpoissa sanoissa on alle 8 kirjainta,
haastavissa on 8-15 kirjainta ja vaikeissa yli 15 kirjainta.
Pelaaja ehdottaa kirjaimia, jotka saattavat esiintyä sanassa.
Jos pelaajan ehdottama kirjain esiintyy sanassa, kirjain ilmestyy niihin
kohtiin, joissa se sanassa esiintyy. Jos ehdotettu kirjain ei ole sanassa,
ruudulle tulevaan kuvioon lisätään elementti.

Peli päättyy, kun pelaaja saa sanan valmiiksi, eli kun pelaaja arvaa
joko kaikki sanassa esiintyvät kirjaimet tai koko sanan oikein,
jolloin pelaaja voittaa tai koko kuvio ollaan saatu piirrettyä
(10 elementtiä), jolloin pelaaja häviää.

Nyt voimme aloittaa pelin!
''')
            break
        if jooei == "ei":
            print("\nHienoa. Aloitetaan peli!\n")
            break
        else:
            print("Et vastannut, haluatko lukea ohjeet.")

    #vaikeustason valinta
    #ensimmäisten viivojen printtaus, pelin edetessä viivat printataan pelataan()-metodista
    while True:
        try:
            taso = int(input("Minkä vaikeustason haluat valita: 1 = helppo, 2 = haastava vai 3 = vaikea? "))
            print('')
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
        except ValueError: #jos sattuu laittamaan erikoismerkin, testatessa huomasin että tämä kannattaa olla
            print("Et valinnut vaikeustasoa. Valitse vaikeustaso uudelleen: ")

    print('')
    print('')
#    print(sana) #testisyistä

    pelataan()

    return peli


def ristinolla(peli):
    mallilauta =[
      ["1|","2|","3"],
      ["4|","5|","6"],
      ["7|","8|","9"]
    ]
    pelilauta = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]

    user = True # kun true on x vuoro, false o vuoro
    turns = 0

    print("\nOhjeet: pelaajat vuorotellen asettavat joko ristin tai ympyrän.")
    print("Tavoitteena saada 3 peräkkäin, joko vaaka-, pysty- tai vinosuuntaan.")
    print('')
    print(peli['pelaajat'][0],'sinä aloitat pelimerkillä "x".')
    
    def print_ohjeet(mallilauta):
        print('')
        for row in mallilauta:
            for slot in row:
                print(f"{slot}", end="") 
            print()

    def print_pelilauta(pelilauta):
        for row in pelilauta:
            for slot in row:
                print(f"{slot} ", end="") 
            print()
            
    def lopettaminen(user_input):
        if user_input == "q":
            print("Play you later!")
            return True
        else: return False

    def paikan_tarkistus(user_input):
        #tarkista onko syöte numero
        if not numero(user_input): return False
        user_input = int(user_input)
        #onko numero 1-9
        if not alue(user_input):return False 
        
        return True  

    def numero(user_input):
        if not user_input.isnumeric():
            print("Tämä ei ole numero.")
            return False
        else: return True

    def alue(user_input):
        if user_input > 9 or user_input < 1:
            print("Tämä numero ei käy.")
            return False
        else: return True

    def varattu(coords, pelilauta):
        row = coords[0]
        col = coords[1]
        if pelilauta[row][col] != "-":
            print("Tämä paikka on varattu.")
            return True
        else: return False
        
    def koordinaattit(user_input):
        row = int(user_input / 3)
        col = user_input
        if col > 2: col = int(col % 3)
        return(row, col)

    def lisää_pelilautaan(coords, pelilauta, active_user):
        row = coords[0]
        col = coords[1]
        pelilauta[row][col] = active_user
        
    def current_user(user):
      if user: return "x"
      else: return "o"

    def voitto(user, board):
      if vaaka_voitto(user, pelilauta):
          return True
      elif pysty_voitto(user, pelilauta):
          return True
      elif vino_voitto(user, pelilauta):
          return True
      else:
          return False

    def vaaka_voitto(user, pelilauta):
      for row in pelilauta:
        complete_row = True
        for slot in row:
          if slot != user:
            complete_row = False
            break
        if complete_row: return True
      return False 


    def pysty_voitto(user, pelilauta):
      for col in range(3):
        complete_col = True
        for row in range(3):
          if pelilauta[row][col] != user:
            complete_col = False
            break
        if complete_col:
            return True
      return False

    def vino_voitto(user, pelilauta):
      if pelilauta[0][0] == user and pelilauta[1][1] == user and pelilauta[2][2] == user:
          return True
      elif pelilauta[0][2] == user and pelilauta[1][1] == user and pelilauta[2][0] == user:
          return True
      else:
          return False

    while turns < 9:
        active_user = current_user(user)
        print_ohjeet(mallilauta)
        print("-----------")
        print_pelilauta(pelilauta)
        user_input = input("\nValitse paikka 1-9 tai paina \"q\" lopettaaksesi: ")
        if lopettaminen(user_input):
            break
        if not paikan_tarkistus(user_input):
            print("Kokeile uudestaan.")
            continue
        user_input = int(user_input) - 1
        coords = koordinaattit(user_input)
        if varattu(coords, pelilauta):
            print("Kokeile uudestaan.")
            continue
        lisää_pelilautaan(coords, pelilauta, active_user)
        if voitto(active_user, pelilauta):
            if active_user == 'x':
                peli['voittaja'] = peli['pelaajat'][0]
            elif active_user == 'o':
                peli['voittaja'] = peli['pelaajat'][1]

            print('')
            print_pelilauta(pelilauta)
            print("\nHei nyt on syytä juhlaan, "f"{active_user.upper()} voitti!\n")

            break

        turns += 1
        if turns == 9:
            print('')
            print_pelilauta(pelilauta)
            print("\nOnnittelut tasapelistä!")
            peli['voittaja'] = 'tasapeli'
        user = not user

    return peli


def neljansuora(peli):

    def pelinAloitus():

        ## Löytyykö pelilaudalta 4 pelimerkin suora
        ## Jos löytyy palautetaan voittaja, muuten None
        def tilanteenTarkistus(pelintila,pelaaja):
            lauta = pelintila['lauta']
            with open("suorat.json", "r") as f:
                data = json.load(f)
                reg = str(pelintila['pelaajat'][pelaaja])*4
                for suora,lista in data.items():
                    mjono = ''
                    for koordinaatit in lista:
                        mjono += lauta[koordinaatit[0]][koordinaatit[1]]
                        if mjono.find(reg) != -1:
                            voittaja = pelaaja
                            return voittaja
                                    
    
        def siirrot(pelintila):
            pelaaja = vuorot(pelintila)
            jatkuu = True
            sarake = []
        
            lauta = pelintila['lauta']

            ## Tarkistetaan, että laudalla on tilaa
            taynna = 0
            for rivi in lauta:
                if 'o' not in rivi:
                    taynna += 1
            if taynna == 6:
                jatkuu = False
                print('')
                print('Pelilauta tuli täyteen, ja peli päättyi tasapeliin!\n')
                print('Lopputilanne:')
                pelintila['voittaja'] = 'tasapeli'
                peli['voittaja'] = 'tasapeli'
                
            lauta.reverse()

            ## Kysytään pelaajan siirto, ja asetetaan se 'alimpaan' kohtaan, jossa tyhjää
            ## Kysytään siirtoa, kunnes löytyy tyhjä sarake
            while jatkuu:
                y = (int(input(pelaaja+', mihin sarakkeeseen haluat pudottaa merkkisi? (1-7) '))) - 1
                if y > 7:
                    print('')
                    print('Tarkistathan, että syöttämäsi sarake on pelilaudalla. (1-7)')
                    print('')
                else:
                    for x, rivi in enumerate(lauta):
                        sarake.append(lauta[x][y])
                        if rivi[y] == 'o':
                            lauta[x][y] = pelintila['pelaajat'][pelaaja]
                            jatkuu = False
                            break
                    if 'o' not in sarake:
                        print('')
                        print('Tämä sarake on jo täynnä. Kokeile toista saraketta.')
                        print('')

            lauta.reverse()

            ## Päivitetään pelilauta
            pelintila['lauta'] = lauta
        
            ## Tarkistetaan, onko voittaja
            voittaja = tilanteenTarkistus(pelintila,pelaaja)
            if voittaja != None:
                pelintila['voittaja'] = pelaaja
                peli['voittaja'] = pelaaja
                print('')
                print('ONNEA,',voittaja+'! Voitit tämän pelin!\n')
                print('Lopputilanne:')

            return lauta

        ## Vuorot vaihtuvat vuoro-muuttujan parillisuuden mukaan.
        def vuorot(pelintila):
            if pelintila['vuoro']%2 != 0:
                pelaaja = pelaaja1
            else:
                pelaaja = pelaaja2
            return pelaaja

        def tulostaLauta(lauta):
            sarakkeet = [' 1',' 2',' 3',' 4',' 5',' 6',' 7']
            print('')
            for num in sarakkeet:
                print(num, end='')
            for rivi in lauta:
                print('')
                for item in rivi:
                    print('|'+item, end='')
                print('|', end='')
            print('\n')

        ## Luetaan pelin aloituksen tila tiedostosta
        with open("pelintila.json","r") as tiedosto:
            pelintila = json.load(tiedosto)

        
        pelaaja1 = peli['pelaajat'][0]
        pelaaja2 = peli['pelaajat'][1]
        
        pelintila['pelaajat'] = {pelaaja1:'v', pelaaja2:'m'}

        ##Pelin ohjeistus
        print('\n\n\nPELI ALKAA\n\n\n')
        print(pelaaja1+', pelimerkkisi on "v".')
        print(pelaaja2+', pelimerkkisi on "m".')
        print('')
        print("""
Neljänsuoran ohjeet:

Pelilaudan koko on 7x6. Pelaajat sijoittavat pelimerkkinsä
vuorotellen "pudottamalla" merkkinsä täyttämättömiin sarakkeisiin,
jolloin kiekko varaa itselleen tyhjästä kohdasta sijansa.
Voittaakseen pelin täytyy pelaajan asettaa omia pelimerkkejään niin,
että muodostuu joko pystysuorassa, vaakasuorassa tai
poikittain neljän merkin suora.
Jos pelilauta täyttyy ilman voittajaa, syntyy tasapeli.

Pelilauta:""")
        tulostaLauta(pelintila['lauta'])
        pelataan = True
        while pelataan:
            pelintila['lauta'] = siirrot(pelintila)
            tulostaLauta(pelintila['lauta'])
            ## Pelintila['voittaja'] päivittyy != None vain silloin, jos löytyy voittaja
            ## tai peli päättyy tasapeliin
            if pelintila['voittaja'] != None:
                pelataan = False
            else:
                pelintila['vuoro'] += 1

    pelinAloitus()
    print(peli['voittaja'])

    return peli

def pelinvalinta():
    if len(peli['pelaajat']) == 1:
        peli['lautapeli'] = 'hirsipuu'
        print('\nPelataan hirsipuuta!\n')
        hirsipuu(peli)
           

    elif len(peli['pelaajat']) == 2:
        valinta = True
        while valinta:
            pelinvalinta = input('\nPelataanko 1 = ristinollaa vai 2 = neljänsuoraa? ')       
            if pelinvalinta == '1':
                peli['lautapeli'] = 'ristinolla'
                ristinolla(peli)
                valinta = False
            elif pelinvalinta == '2':
                peli['lautapeli'] = 'neljänsuora'
                neljansuora(peli)
                valinta = False
            else:
                print('Syötteesi oli hämärä, katoppa uusiks.')

    if len(peli['pelaajat']) == 2:
        if peli['voittaja'] == 'tasapeli':
            tulos = [[pelaaja1, 1],[pelaaja2, 1]]
        elif peli['voittaja'] == pelaaja1:
            tulos = [pelaaja1, 3]
        elif peli['voittaja'] == pelaaja2:
            tulos = [pelaaja2, 3]
    else:        
        if peli['voittaja'] == 'häviö':
            tulos = 0
        else:
            tulos = [peli['pelaajat'][0], 3]



    with open("scoreboard.json", "r", encoding='utf8') as f:
        data = json.load(f)
        hashmap = data[peli['lautapeli']]
        if tulos != 0 and type(tulos[0]) == list:
            for player in tulos:
                if player[0] in hashmap:
                    hashmap[player[0]] += player[1]
                else:
                    hashmap[player[0]] = player[1]
        elif tulos != 0 and type(tulos[0]) != list:
            if tulos[0] in hashmap:
                hashmap[tulos[0]] += tulos[1]
            else:
                hashmap[tulos[0]] = tulos[1]

    with open("scoreboard.json","w") as file:
        json.dump(data, file)



    tulokset = input('\nHaluatko nähdä pelitulokset? kyllä/ei ')
    if tulokset == 'kyllä':
        print('\n'+peli['lautapeli']+'n top 5:')
        print('\nNIMIM\tTULOS')
        with open("scoreboard.json", "r") as f:
            data = json.load(f)
            sor = sorted(hashmap.items(), key=itemgetter(1), reverse=True)

        for pelaaja in sor[:5]:
            print(pelaaja[0]+'\t'+str(pelaaja[1]))

    else:
        print('Tuloksia ei printattu.')



print('Tervetuloa pelaamaan!\n')
print('''Pelejämme ovat:
1. Ristinolla (2 pelaajaa)
2. Neljänsuora (2 pelaajaa)
3. Hirsipuu (1 pelaaja)\n''')

tervetuloa = True


peli = {'voittaja':None}

while tervetuloa:
    pelaajamaara = int(input('Montako pelaajaa on? (1 tai 2) '))

    if pelaajamaara == 2:
        pelaaja1 = input('Pelaaja 1, mikä on nimimerkkisi? ')
        pelaaja2 = input('Pelaaja 2, entäpä sinun? ')
        if pelaaja1 == pelaaja2:
            pelaaja2 = pelaaja2 + '2'
            print("""\nHUOM!\nPelaajilla ei voi olla samaa nimimerkkiä.
Pelaaja 2, nimimerkkisi on:""", pelaaja2)
        peli['pelaajat'] = [pelaaja1, pelaaja2]
        tervetuloa = False

    elif pelaajamaara == 1:
        pelaaja1 = input('Pelaaja, mikä on nimimerkkisi? ')
        peli['pelaajat'] = [pelaaja1]
        tervetuloa = False

    else:
        print('Olihan pelaajia varmasti yksi tai kaksi?')

halutaanPelata = True

while halutaanPelata:
    typo = True
    pelinvalinta()
    while typo:
        pelataanko = input('\nUusi peli? kyllä/ei: ')
        if pelataanko == 'kyllä':
            print('\nUusi peli kehiin!')
            typo = False
            halutaanPelata = True
        elif pelataanko == 'ei':
            print('\nKiitos pelaamisesta! Moikka!\n')
            halutaanPelata = False
            typo = False
        else:
            print('\nKirjoitithan oikein?\n')
            typo = True

