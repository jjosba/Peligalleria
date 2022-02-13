import json
import re

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

    
    pelaaja1 = input('Pelaaja 1, mikä on nimimerkkisi? ')
    pelaaja2 = input('Pelaaja 2, entäpä sinun? ')
    if pelaaja1 == pelaaja2:
        pelaaja2 = pelaaja2 + '2'
        print("""\nHUOM!\nPelaajilla ei voi olla samaa nimimerkkiä.
Pelaaja 2, nimimerkkisi on:""", pelaaja2)
    pelintila['pelaajat'] = {pelaaja1:'v', pelaaja2:'m'}

    ##Pelin ohjeistus
    print('')
    print(pelaaja1+', pelimerkkisi on "v".')
    print(pelaaja2+', pelimerkkisi on "m".')
    print('')
    print("""Pelilaudan koko on 7x6. Pelaajat sijoittavat pelimerkkinsä
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



halutaanPelata = True
typo = True

## Peliä toistetaan, kunnes halutaanPelata == 'ei'
while halutaanPelata:   
    pelinAloitus()
    while typo:
        pelataanko = input('Uusi peli? kyllä/ei: ')
        if pelataanko == 'kyllä':
            print('\nUusi peli kehiin!\n')
            typo = False
            halutaanPelata = True
        elif pelataanko == 'ei':
            print('\nKiitos pelaajille! Moikka!\n')
            halutaanPelata = False
            typo = False
        else:
            print('\nKirjoitithan oikein?\n')
            typo = True
        






