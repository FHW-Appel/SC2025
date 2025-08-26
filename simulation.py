
# Ruleset
# Variablen definiert

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
    for strategie1 in strategie_liste:
        ergebnis.append([])
        for strategie2 in strategie_liste:
            punkte_der_strategie1 = []
            for ind in range(spielanzahl):
                history1 = []
                history2 = []
                punkte_der_strategie1 = 0
                for round in range(rundenanzahl):
                    st1acted = strategie1.act(history1, history2) # st1acted = how strategy 1 acted
                    st2acted = strategie2.act(history2, history1)
                    history1.append(st1acted)
                    history2.append(st2acted)
                    punkte_der_strategie1 += eval_ruleset(st1acted, st2acted)[0]
                

                    
#def test():
#    print(eval_ruleset(True, False))
