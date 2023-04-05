game_info = """                 მოგესალმებით!

ეს არის თამაში სახელად ჩაძირობანა!
თამაში ძალიან მარტივია, მოთამაშეების მიზანია განალაგონ თავიანთი
გემები სასურველ პოზიციებზე, ხოლო შემდეგ კი შეუტიონ ერთმანეთს
და გაანადგრუონ ერთმანეთი! იმარჯვებს უძლიერესი
და ამავდროულად უფრო იღბლიანიც :))

                    წესები

მოთამაშეებმა უნდა აირჩიონ პოზიციები, თუ სად განალაგებენ
თავიანთ გემებს საბრძოლო მოედანზე, მოთამაშემ უნდა აირჩიოს
თავისი პოზიცია ანბანისა და ნომრების მიხედვით,
ლათინური ანბანიდან A-დან H-მდე აქვს არჩევანი (ესეიგი: A, B, C, D, E, F, G, H),
ხოლო ციფრებიდან 1-დან 8-მდე (ესეიგი: 1, 2, 3, 4, 5, 6, 7, 8).
სიტყვაზე: ჩემი პირველი გემი მინდა რომ იყოს A6-ზე , მეორე B4-ზე, მესამე F1-ზე და ა.შ.
სულ მოთამაშე ანაწილებს 5 ცალ გემს, მოთამაშეებს რიგ-რიგობით აქვთ შეტევის უფლება,
ვინც გამოიცნობს, თუ რომელ პოზიციაზე უყენია მოწინააღმდეგეს გემი, მაშინ მოწინააღმდეგის გემი იძირება...
და ეს გრძელდება იქმადე, სანამ გამარჯვებული არ გამოვლინდება!
"""


print(game_info)


class Player:
    def __init__(self, name, shipPosition, victoryPhrase=None, wins=0):
        self.name = name
        self.shipPosition = shipPosition
        self.victoryPhrase = victoryPhrase
        self.wins = wins

    def __str__(self):
        if self.victoryPhrase is not None:
            return f"მოთამაშის სახელია {self.name}, მოთამაშის მოგებები: {self.wins}, მოთამაშის მოგების ფრაზაა {self.victoryPhrase}"
        return f"მოთამაშის სახელია {self.name}, მოთამაშის მოგებები: {self.wins}"


class Game:
    def __init__(self, map, playerOne, playerTwo):
        self.map = map
        self.playerOne = playerOne
        self.playerTwo = playerTwo

    def gameOn(self, playerOne_InGame, playerTwo_InGame):
        self.__playerOne = playerOne_InGame
        self.__playerTwo = playerTwo_InGame
        players = [playerOne_InGame, playerTwo_InGame]
        i = False
        while True:
            playerTurn = input(f'ესროლე მოწინააღმდეგეს {players[i].name}! შეიყვანე პოზიცია, რომელზეც გინდა, რომ შეტევა განახიორციელო: ').upper()
            if playerTurn in players[not i].shipPosition:
                print(f'მოწინააღმეგეს გემი {playerTurn} ჩაძირულია!!!')
                players[not i].shipPosition.remove(playerTurn)
                if not players[not i].shipPosition:
                    if players[i].victoryPhrase is not None:
                        print(f'გილოცავ {players[i].name} შენ მოიგე !!!!')
                        print(f'{players[i].name}-ის გამარჯვების ფრაზა:', players[i].victoryPhrase)
                    else:
                        print(f'გილოცავ {players[i].name} შენ მოიგე !!!!')
                    players[i].wins += 1
                    break
            elif playerTurn == 'Q':
                print('თქვენ გამოხვედით თამაშიდან.')
                break
            else:
                print(f'სამწუხაროდ {players[i].name} სროლა გამაზე')
                i = not i


playerOne_Name = input('მოთამაშე 1 - შეიყვანეთ თქვენი სახელი: ')
while playerOne_Name == '':
    playerOne_Name = input('მოთამაშე 1 - გთხოვთ შეიყვანოთ თქვენი სახელი: ')

playerOne_VictoryPhrase = input('მოთამაშე 1 - თუ გსურს შეიყვანე შენი გამარჯვების ფრაზა, თუ არადა დააწექი Enter ღილაკს: ')
if playerOne_VictoryPhrase == '':
    playerOne_VictoryPhrase = None
else:
    playerOne_VictoryPhrase == playerOne_VictoryPhrase

count = 0
playerOne_Ship_Position = []
ship_One = 0
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

while count < 3:
    playerOne_ship = ''
    playerOne_ship_letter = input(f'გემი {ship_One + 1}-სთვის შეიყვანეთ თქვენთვის სასურველი ასო: ').upper()
    while playerOne_ship_letter == '' or playerOne_ship_letter not in letters:
        playerOne_ship_letter = input(f'შეიყვანეთ სწორი ასო {ship_One + 1}-სთვის: ').upper()
    playerOne_ship_number = input(f'გემი {ship_One + 1}-სთვის შეიყვანეთ თქვენთვის სასურველი რიცხვი: ')
    while playerOne_ship_number == '' or playerOne_ship_number not in numbers:
        playerOne_ship_number = input(f'შეიყვანე სწორი რიცხვი {ship_One + 1}-სთვის: ').upper()
    playerOne_ship += playerOne_ship_letter + playerOne_ship_number
    playerOne_Ship_Position.append(playerOne_ship)
    playerOne_ship = ''
    ship_One += 1
    count += 1

print('პირველი მოთამაშის გემის პოზიციებია:', playerOne_Ship_Position)

P1 = Player(playerOne_Name, playerOne_Ship_Position, playerOne_VictoryPhrase)
print(P1)

playerTwo_Name = input('მოთამაშე 2 - შეიყვანეთ თქვენი სახელი: ')
while playerTwo_Name == '':
    playerTwo_Name = input('მოთამაშე 2 - გთხოვთ შეიყვანოთ თქვენი სახელი: ')
playerTwo_VictoryPhrase = input('მოთამაშე 2 - თუ გსურს შეიყვანე შენი გამარჯვების ფრაზა, თუ არადა დააწექი Enter ღილაკს: ')
if playerTwo_VictoryPhrase == '':
    playerTwo_VictoryPhrase = None
else:
    playerTwo_VictoryPhrase == playerTwo_VictoryPhrase

count = 0
playerTwo_Ship_Position = []
ship_Two = 0
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

while count < 3:
    playerTwo_ship = ''
    playerTwo_ship_letter = input(f'გემი {ship_Two + 1}-სთვის შეიყვანეთ თქვენთვის სასურველი ასო: ').upper()
    while playerTwo_ship_letter not in letters:
        playerTwo_ship_letter = input(f'შეიყვანეთ სწორი ასო {ship_Two + 1}-სთვის: ').upper()
    playerTwo_ship_number = input(f'გემი {ship_Two + 1}-სთვის შეიყვანეთ თქვენთვის სასურველი რიცხვი: ')
    while playerTwo_ship_number not in numbers:
        playerTwo_ship_number = input(f'შეიყვანე სწორი რიცხვი {ship_Two + 1}-სთვის: ').upper()
    playerTwo_ship += playerTwo_ship_letter + playerTwo_ship_number
    playerTwo_Ship_Position.append(playerTwo_ship)
    playerTwo_ship = ''
    ship_Two += 1
    count += 1

print('მეორე მოთამაშის გემის პოზიციებია:', playerTwo_Ship_Position)

P2 = Player(playerTwo_Name, playerTwo_Ship_Position, playerTwo_VictoryPhrase)
print(P2)

ask_Player_Map = input("""შეიყვანეთ თქვენთვის სასურველი რუკა რომელზეც ითამაშებთ
1) შავი ზღვა 2)ლისის ტბა 3) კუს ტბა
შეიყვანეთ: """)
if ask_Player_Map == '1':
    game_map = 'შავი ზღვა'
elif ask_Player_Map == '2':
    game_map = 'ლისის ტბა'
elif ask_Player_Map == '3':
    game_map = 'კუს ტბა'
else:
    map_count = 0
    while map_count < 1:
        ask_Player_Map = input('შეიყვანე ასო 1-დან 3-მდე: ')
        if ask_Player_Map == '1':
            game_map = 'შავი ზღვა'
            map_count += 1
        elif ask_Player_Map == '2':
            game_map = 'ლისის ტბა'
            map_count += 1
        elif ask_Player_Map == '3':
            game_map = 'კუს ტბა'
            map_count += 1

G1 = Game(game_map, P1, P2)
print(f'{G1.map} - ბრძოლის ადგილი!')
G1.gameOn(P1, P2)


print(f'{P1.name}-ის მოგებები:', P1.wins)
print(f'{P2.name}-ის მოგებები:', P2.wins)

# gamarjoba