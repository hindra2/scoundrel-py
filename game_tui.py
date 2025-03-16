from CardUtils import Deck
import os


class ScoundrelTUI():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.dungeon = [None, None, None, None]
        self.init_dungeon()

        self.weapon = None
        self.monsters = []

        self.health = 20

        self.running = True

        self.discard_pile = []

    def init_dungeon(self):
        for i in range(0, 4):
            self.dungeon[i] = self.deck.draw()

    def fill_dungeon(self):
        none_count = self.dungeon.count(None)

        if none_count == 3:
            for i in range(0, 4):
                if self.dungeon[i] is None:
                    self.dungeon[i] = self.deck.draw()


    def print_board(self):
        dungeon = ""
        for card in self.dungeon:
            if card is None:
                dungeon += " |_| "
                continue
            dungeon += str(card)

        if self.weapon is None:
            weapon = "|_|"
        else:
            weapon = str(self.weapon)

        ui = f"Health: {self.health}\nWeapon: {weapon}"

        monsters_str = "Monsters: "
        for card in self.monsters:
            monsters_str += str(card)

        discard = ""
        for card in self.discard_pile:
            discard += str(card)

        print("====Scoundrel====")
        print(dungeon)
        print(ui)
        if self.monsters:
            print(monsters_str)
        print(discard)

    def parse_card(self, card):
        if card.suit == 0 or card.suit == 1:
            if not self.weapon:
                self.discard_pile.append(card)
                self.health -= card.rank
            else:
                if self.weapon.rank >= card.rank:
                    pass
                if len(self.monsters) == 0 or self.monsters[-1].rank <= card.rank:
                    self.monsters.append(card)
                    self.health -= (card.rank - self.weapon.rank)
        elif card.suit == 2:
            self.health += card.rank
            self.discard_pile.append(card)
            if self.health > 20:
                self.health = 20
        else:
            self.weapon = card

    def handle_player_input(self):
        try:
            index = input("Card to take: ")
            if index == "q":
                self.running = False
                return
            currCard = self.dungeon[int(index) - 1]
            if currCard is None:
                print("There's no card in that position!")
                return
            self.dungeon[int(index) - 1] = None
            self.parse_card(currCard)
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 4.")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def win(self):
        print("YOU CLEARED THE DUNGEON YOU SCOUNDREL")

    def lose(self):
        print("YOU DIED :(")

    def run(self):
        while self.running:
            self.fill_dungeon()
            self.clear_terminal()
            self.print_board()
            if self.health <= 0:
                self.running = False
                self.clear_terminal()
                self.lose()
                break
            if self.deck.cards_remaining() == 0:
                self.running = False
                self.clear_terminal()
                self.win()
                break
            self.handle_player_input()
