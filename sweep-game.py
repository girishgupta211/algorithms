import random

a = []
for i in range(1, 14):
    a.append(("diamonds", i))

for i in range(1, 14):
    a.append(("spades", i))

for i in range(1, 14):
    a.append(("hearts", i))

for i in range(1, 14):
    a.append(("clubs", i))
random.shuffle(a)

available_cards = {"diamonds_1": 4, "diamonds_2": 2}

p1 = []
p2 = []
system = {"loose_cards": [], "houses": {11: {"team": 't1', "cards": [[2, 9], [3, 8]]}}}

p1_score = []
p2_score = []

# if bid card has only 1 value available_cards, then he hs to pickup

# 1 Picking_up {loose card/cards, house }
# bid value # 9 [loose numbers] [2, 7]
# bid value # 9 [hosue 9]

# 12 house , 3, 9 house <kach>


# 2 Throwing a loose card.
# simply add to loose cards

# Creating or adding to a house
# player must own any card >=9 to create a house

# Creating
# select loose_cards = [], [house with one length, loose_cards]
# eg bid value <= 12
# loose cards = [2, 4, 6] , [house :  9, loose card : [1, 2]], None ]

# Adding to a house (eg 12)
# house is available with team OR  house is not owned with team, but bid value is present with the player
# eg bid value : <=12 eg 2
# loose cards = [8, 2] , [house :  10]
# not a valid, [house :  9,loose cards = [1]] # DOUBT

# eg bid value :12
# loose cards = [] , [house :  None]

# house is not owned with team, but bid value is not present with the player:
# DO NOT ALLOW TO ADD to cards


# team assignment

# {11 : {team: 't', cards : [ [2, 9] , [3, 8]] }  # if lenght of cards is > 1 , cemented else normal
# {12 : [] }
# {13 : [] }
# {9 : [] }
# {10 : [] }
# loose_cards : [Q, 1, 5, 9, 2]

# 13
# loose cards : [Q, 1, 5, 9, 2]
# cemented_house : { face_vale  11: [2, 9] , [3, 8] }
# house : {11 : [2, 9] }

# distribute_4-4_cards_initially
for i in range(4):
    system.append([a.pop()])
    p1.append(a.pop())
    p2.append(a.pop())
print(p1)
print(p2)
print(system)

if all(t[1] < 9 for t in p1):
    print("no card is greater than 8")
    exit(-1)

bid = int(input("if no card is greater than 8 input 0"))

# if bid==0:
#     exit()
# print(system)


# match=input("if there is match input yes else no")
# if match=="no":
#     throw=int(input("enter the index of card"))
#     system.append([p1.pop(throw)])
# else:
#     p1_score.append(p1.pop(int(input("give matched card index"))))
#     pick=input("index of picked card")
#     q=0
#     for i in range(len(pick)):
#         p1_score.append([system.pop(int(pick[i-q]))][0])
#         q=q+1
# print(p1_score,"\n",system,"\n")
# if len(system)==0:
#     p1_score.append(("sweep,25"))
#
#
# for i in range(8):
#         p1.append(a.pop())
#         p2.append(a.pop())
#
# # print(system)
# def players_turn(player,score_card):
#     print("your cards are",player)
#     if len(system)==0:
#         system.append([player.pop(int(input("index of card to be thrown")))])
#     else:
#         print("system cards are",system)
#         choice=input("choose - pick,cement,kaccha")
#         print(choice)
#         if choice=="pick":
#             pass
#         elif choice=="cement":
#             pass
#         elif choice=="kaccha":
#             pass
#
# players_turn(p2,p2_score)
