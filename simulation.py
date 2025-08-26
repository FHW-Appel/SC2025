import importlib
import os
# Ruleset
# Variablen definiert

strategie_liste = []
strat_dir = "strat"
for filename in os.listdir(strat_dir):
    modulname = f"{strat_dir}.{filename[:-3]}"
    modul = importlib.import_module(modulname)
    klassename = filename[:-3]
    strategie_klasse = getattr(modul, klassename)
    strategie_liste.append(strategie_klasse())

roundanzahl = 50 #Input von der Konsole

dict = {
    # Strategy 1, Strategy 2 = reward strategy 1, reward strategy 2
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [5, 0],
    (False, True): [0, 5]
}

def eval_ruleset(strategy_1: bool, strategy_2: bool):
    return dict.get((strategy_1, strategy_2))

# Start of simulation

for strategie in strategie_liste:
    for strategie2 in strategie_liste:
        for round in range(0, roundanzahl):
            pass

print(eval_ruleset(True, False))
