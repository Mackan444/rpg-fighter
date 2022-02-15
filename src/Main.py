from ast import Break
from importlib import resources
from random import randint
import Resorces
from Resorces import Character, Goblin

if __name__  == "__main__":
    nemy = Character("Nemy", 20, 5, 2)
    Goblin_one = Goblin(10, 3, 1)

    print(nemy)
    print()
    print(Goblin_one)

    fight_round = 1
    print("========Fight========")
    while nemy.get_health() !=0 and Goblin_one.get_health() !=0:
        print(f"Round {fight_round}")
        nemy_attack = nemy.damage()*randint(1,3)
        Goblin_one.take_damage(nemy_attack)
        if(Goblin_one.get_health() == 0):
            print("Goblin has died")
            break
        else:
            print(f"Goblin has {Goblin_one.get_health()} hp left")
            Goblin_attack = Goblin_one.damage()*randint(1,4)
            nemy.take_damage(Goblin_attack)
            print(f"Nemy has{nemy.get_health()} hp left")
            if (nemy.get_health() == 0): print("Nemy has died")
        fight_round +=1

    if(nemy.get_health() == 0): print("The Goblin won")
    else: print
