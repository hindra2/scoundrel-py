# Rules:

1. Remove all red face cards, red aces and jokers
2. Start with 20 health (max cap)
3. Draw a 4 card dungeon to start
4. Go through the dungeon by taking cards, applying/healing damage and taking weapons
5. Only 1 weapon card can be active at a time
   a) Monsters of any damage can be taken, the damage dealt is monster damage - weapon damage
   b) After a monster has been taken by a weapon, only monsters of lower damage than that monster can be taken again by the same weapon
   c) The player is not forced to discard a weapon
6. The dungeon can be progressed (filled with draws) when there is only 1 card left in the 4 dungeons

# Suits:

Spades & Clubs - monster cards \
Hearts - healing \
Diamonds - Weapons

# Card Class

```
class Card:
    init:
        rank
        suit

```

## Suits:

0 = spades \
1 = clubs \
2 = hearts

## Ranks:

0 = null \
1 - 13 = Ace - King

# Deck Class

```
class Deck:
    init:
        cards = [Cards]
        build()

    build() - builds a random deck
    shuffle() - shuffles a built deck
    draw() - returns the card obejct in the queue
```
