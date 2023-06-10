from random import random, randint


def election():
    A_region_1 = 0.87
    A_region_2 = 0.65
    A_region_3 = 0.17
    A_wins = 0
    for i in range(10_000):
        A_regional_wins = 0
        region_1_elections = random()
        if region_1_elections <= A_region_1:
            A_regional_wins += 1
        region_2_elections = random()
        if region_2_elections <= A_region_2:
            A_regional_wins += 1
        region_3_elections = random()
        if region_3_elections <= A_region_3:
            A_regional_wins += 1
        if A_regional_wins > 1:
            A_wins += 1

    print(f'Candidate A wins with probability: {A_wins / 100}%')
    print(f'Candidate B wins with probability: {(10_000 - A_wins) / 100}%')
            
election()

def coin_toss():
    flips = 0
    for i in range(10_000):
        first_flip = randint(0, 1)
        flips += 1
        while True:
            next_flip = randint(0, 1)
            flips += 1
            if next_flip != first_flip:
                break
    print(f'Average flips to get both sides of coin: {flips / 10_000}')

coin_toss()
