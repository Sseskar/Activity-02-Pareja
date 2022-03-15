import random
from time import sleep

#Stats
level = 90
power = 110
a = 205
d = 188

#Modifiers
targets = 1
weather = 1
badge = 1
critical = 1
rand = random.uniform(0.85, 1)
stab = 1.5
type = 0.5
burn = 1
modifier = (targets*weather*badge*critical*rand*stab*type*burn*1)
damage = ((((((2 * level / 5) + 2) * power) * (a / d))) / (50 + 2) * modifier)

print("CHARIZARD used FIRE BLAST!")
sleep(0.70)
print("It's not very effective...")
sleep(0.70)
print("CHARIZARD attack dealt",round(damage), "damage to FERALIGATR")