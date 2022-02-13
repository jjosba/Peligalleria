
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

def print_ohjeet(mallilauta):
    print("ohjeet: pelaajat vuorotellen asettavat joko ristin tai ympyrän.")
    print("Tavoitteena saada 3 peräkkäin, joko vaaka, pysty tai vino suuntaan")
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
        print("play you later!")
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
        print("Tämä ei ole numero")
        return False
    else: return True

def alue(user_input):
    if user_input > 9 or user_input < 1:
        print("tämä numero ei käy")
        return False
    else: return True

def varattu(coords, pelilauta):
    row = coords[0]
    col = coords[1]
    if pelilauta[row][col] != "-":
        print("tämä paikka on varattu")
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
  if vaaka_voitto(user, pelilauta): return True
  if pysty_voitto(user, pelilauta): return True
  if vino_voitto(user, pelilauta): return True
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
    if complete_col: return True
  return False

def vino_voitto(user, pelilauta):
  if pelilauta[0][0] == user and pelilauta[1][1] == user and pelilauta[2][2] == user: return True
  elif pelilauta[0][2] == user and pelilauta[1][1] == user and pelilauta[2][0] == user: return True
  else: return False

while turns < 9:
    active_user = current_user(user)
    print_ohjeet(mallilauta)
    print("-----------")
    print_pelilauta(pelilauta)
    user_input = input("valitse paikka 1-9 tai paina \"q\"lopettaaksesi:")
    if lopettaminen(user_input): break
    if not paikan_tarkistus(user_input):
        print("kokeileppa uudestaan")
        continue
    user_input = int(user_input) - 1
    coords = koordinaattit(user_input)
    if varattu(coords, pelilauta):
        print("Kokeileppa uudestaan")
        continue
    lisää_pelilautaan(coords, pelilauta, active_user)
    if voitto(active_user, pelilauta):
        print("Hei nyt on syytä juhlaan "f"{active_user.upper()} voitti!")
        break

    turns += 1
    if turns == 9: print("Onnittelut saavutitte tasapelin!")
    user = not user


