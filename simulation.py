import importlib
import os

strategie_liste = []
strat_dir = "strat"
for filename in os.listdir(strat_dir):
    if filename.endswith(".py") and not filename.startswith("__"):
        modulname = f"{strat_dir}.{filename[:-3]}"
        modul = importlib.import_module(modulname)
        klassename = filename[:-3]
        strategie_klasse = getattr(modul, klassename)
        strategie_liste.append(strategie_klasse())

#roundanzahl = 50 #Input von der Konsole

ruleset_dict = {
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [0, 5],
    (False, True): [5, 0]
}

def eval_ruleset(strategy_1: bool, strategy_2: bool):
    return ruleset_dict.get((strategy_1, strategy_2))

# Start of simulation

def schleife(rundenanzahl):
    print(f"Strategien: {[strategie.__class__.__name__ for strategie in strategie_liste]}")
    ergebnis = []
    for strategie1 in strategie_liste:
        row = []
        for strategie2 in strategie_liste:
            history1, history2 = [], []
            score = 0
            for _ in range(rundenanzahl):
                st1acted = strategie1.act(history1, history2)
                st2acted = strategie2.act(history2, history1)
                history1.append(st1acted)
                history2.append(st2acted)
                score += eval_ruleset(st1acted, st2acted)[0]
            row.append(score)
        ergebnis.append(row)

    total_scores = [sum(row) for row in ergebnis]
    for i, total in enumerate(total_scores):
        print(f"{strategie_liste[i].__class__.__name__}: Gesamtpunkte: {total}")

    # Find the best strategy
    best_index = total_scores.index(max(total_scores))
    print(f"\nBeste Strategie: {strategie_liste[best_index].__class__.__name__} mit {total_scores[best_index]} Gesamtpunkten")
    return ergebnis
                    