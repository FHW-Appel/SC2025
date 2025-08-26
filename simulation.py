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

#roundanzahl = 50 #Input von der Konsole


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

def schleife(spielanzahl, rundenanzahl):
    ergebnis = [] # ergebnis[strategieindex] = [durchschnittliche Punkeanzahl, durchsch...]
    for st1ind, strategie1 in enumerate(strategie_liste):
        ergebnis.append([])
        for st2ind, strategie2 in enumerate(strategie_liste):
            punkte_der_strategie1 = []
            for spiel_ind in range(spielanzahl):
                history1 = []
                history2 = []
                punkte_der_strategie1.append(0)
                for round in range(rundenanzahl):
                    st1acted = strategie1.act(history1, history2) # st1acted = how strategy 1 acted
                    st2acted = strategie2.act(history2, history1)
                    history1.append(st1acted)
                    history2.append(st2acted)
                    punkte_der_strategie1[spiel_ind] += eval_ruleset(st1acted, st2acted)[0]
            ergebnis[st1ind].append(sum(punkte_der_strategie1)/spielanzahl)
    return ergebnis

                    
#def test():
#    print(eval_ruleset(True, False))
