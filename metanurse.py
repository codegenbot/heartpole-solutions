import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if alertness is very low or it's been too long since sleeping
    if alertness < 0.5 or time_since_slept > 8:
        return 3
    # If any health indicator is high, prioritize rest
    if hypertension >= 0.4 or intoxication >= 0.2:
        return 3
    # Consider drinking coffee and working if alertness is low but safe to work
    if alertness < 0.7 and hypertension < 0.35 and intoxication < 0.1:
        return 1
    # Default action is to just work if everything seems optimal
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)