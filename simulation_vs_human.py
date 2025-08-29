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

ruleset_dict = {
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [0, 5],
    (False, True): [5, 0]
}

def eval_ruleset(strategy_1: bool, strategy_2: bool):
    return ruleset_dict.get((strategy_1, strategy_2))

def bool_input(prompt):
    while True:
        eingabe = input(prompt + " (C für Kooperieren, D für Defektieren): ").strip().upper()
        if eingabe == "C":
            return True
        elif eingabe == "D":
            return False
        else:
            print("Bitte C oder D eingeben.")

def play_vs_strategy(strategy, rundenanzahl):
    print(f"\nDu spielst gegen: {strategy.__class__.__name__}")
    history_human, history_ai = [], []
    score_human, score_ai = 0, 0

    for runde in range(1, rundenanzahl + 1):
        print(f"\nRunde {runde}:")
        human_action = bool_input("Dein Zug")
        ai_action = strategy.act(history_ai, history_human)
        print(f"Strategie spielt: {'C' if ai_action else 'D'}")

        history_human.append(human_action)
        history_ai.append(ai_action)

        punkte_human, punkte_ai = eval_ruleset(human_action, ai_action)
        score_human += punkte_human
        score_ai += punkte_ai
        print(f"Punkte diese Runde: Du: {punkte_human}, Strategie: {punkte_ai}")
        print(f"Zwischenstand: Du: {score_human}, Strategie: {score_ai}")

    print(f"\nEndstand gegen {strategy.__class__.__name__}: Du: {score_human}, Strategie: {score_ai}")

def main():
    print("Wähle eine Strategie gegen die du spielen möchtest:")
    for idx, strat in enumerate(strategie_liste):
        print(f"{idx}: {strat.__class__.__name__}")
    while True:
        try:
            strat_idx = int(input("Nummer der Strategie: "))
            if 0 <= strat_idx < len(strategie_liste):
                break
            else:
                print("Ungültige Nummer.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")

    while True:
        try:
            rundenanzahl = int(input("Wie viele Runden möchtest du spielen? "))
            if rundenanzahl > 0:
                break
            else:
                print("Bitte eine positive Zahl eingeben.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")

    play_vs_strategy(strategie_liste[strat_idx], rundenanzahl)

if __name__ == "__main__":
    main()