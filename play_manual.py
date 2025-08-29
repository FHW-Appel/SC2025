import importlib
import os
from colorama import init, Fore, Style

init(autoreset=True)

strat_dir = "strat"
strategie_liste = []
strategie_namen = []

for filename in os.listdir(strat_dir):
    if filename.endswith(".py") and not filename.startswith("__"):
        modulname = f"{strat_dir}.{filename[:-3]}"
        modul = importlib.import_module(modulname)
        klassename = filename[:-3]
        strategie_klasse = getattr(modul, klassename)
        strategie_liste.append(strategie_klasse())
        strategie_namen.append(klassename)

ruleset_dict = {
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [0, 5],
    (False, True): [5, 0]
}

def eval_ruleset(player_action: bool, strategy_action: bool):
    return ruleset_dict.get((player_action, strategy_action))

print(Style.BRIGHT + Fore.CYAN + "\nWähle eine Strategie, gegen die du spielen möchtest:")
for i, name in enumerate(strategie_namen):
    print(Fore.YELLOW + f"{i + 1}: {name}")

wahl = int(input(Fore.CYAN + "\nNummer der Strategie: ")) - 1
if not (0 <= wahl < len(strategie_liste)):
    print(Fore.RED + "❌ Ungültige Auswahl.")
    exit()

gegner = strategie_liste[wahl]
gegner_name = strategie_namen[wahl]

print(Style.BRIGHT + Fore.GREEN + f"\n🎮 Du spielst gegen: {gegner_name}\n")

rundenanzahl = int(input(Fore.CYAN + "Wie viele Runden möchtest du spielen? "))
history_player = []
history_strategy = []
score_player = 0
score_strategy = 0

for runde in range(1, rundenanzahl + 1):
    print(Style.BRIGHT + Fore.MAGENTA + f"\n🕓 Runde {runde}")
    while True:
        eingabe = input(Fore.CYAN + "Deine Aktion (c = kooperieren 🤝, b = betrügen ❌): ").lower()
        if eingabe in ['c', 'b']:
            break
        print(Fore.RED + "❗ Ungültige Eingabe. Bitte 'c' oder 'b' eingeben.")

    player_action = eingabe == 'c'
    strategy_action = gegner.act(history_strategy, history_player)

    history_player.append(player_action)
    history_strategy.append(strategy_action)

    punkte = eval_ruleset(player_action, strategy_action)
    score_player += punkte[0]
    score_strategy += punkte[1]

    def format_action(act):
        return Fore.GREEN + "Kooperiert 🤝" if act else Fore.RED + "Betrogen ❌"

    print(Fore.BLUE + f"\n🧍 Du hast: {format_action(player_action)}")
    print(Fore.BLUE + f"🤖 {gegner_name} hat: {format_action(strategy_action)}")

    print(Fore.YELLOW + f"\n🎯 Punkte diese Runde: Du = {punkte[0]}, {gegner_name} = {punkte[1]}")
    print(Fore.YELLOW + f"📊 Zwischenstand: Du = {score_player}, {gegner_name} = {score_strategy}")

print(Style.BRIGHT + Fore.GREEN + "\n🏁 --- Spiel beendet ---")
print(Fore.CYAN + f"\n🔢 Endstand nach {rundenanzahl} Runden:")
print(Fore.GREEN + f"🧍 Du: {score_player}")
print(Fore.RED + f"🤖 {gegner_name}: {score_strategy}")

if score_player > score_strategy:
    print(Style.BRIGHT + Fore.GREEN + "\n🎉 Du hast gewonnen!")
elif score_player < score_strategy:
    print(Style.BRIGHT + Fore.RED + "\n💀 Du hast verloren!")
else:
    print(Style.BRIGHT + Fore.YELLOW + "\n🤝 Unentschieden!")
