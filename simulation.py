coop_coop = [3, 3]
defect_defect = [1, 1]
coop_defect = [5, 0]
defect_coop = [0, 5]

dict = {
    (True, True): [3, 3],
    (False, False): [1, 1],
    (True, False): [5, 0],
    (False, True): [0, 5]
}

def eval_ruleset(strategy_1: bool, strategy_2: bool):
    if strategy_1 and strategy_2:
        return coop_coop
    if not strategy_1 and not strategy_2:
        return defect_defect
    if strategy_1 and not strategy_2:
        return coop_defect
    if not strategy_1 and strategy_2:
        return defect_coop

