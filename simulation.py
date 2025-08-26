dict = {
    # Strategy 1, Strategy 2 = reward strategy 1, reward strategy 2
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [5, 0],
    (False, True): [0, 5]
}

def eval_ruleset(strategy_1: bool, strategy_2: bool):
    return dict.get((strategy_1, strategy_2))

print(eval_ruleset(True, False))
