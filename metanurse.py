import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: Sleep if necessary
    if hypertension > 0.02 or intoxication > 0.1 or time_since_slept >= 8:
        return 3
    # Encourage sleep if alertness is very low
    if alertness < 0.4:
        return 3
    # Drink coffee if alertness is low but hypertension is acceptable
    if alertness < 0.7 and hypertension < 0.015:
        return 1
    # Work if reasonably alert
    if 0.7 <= alertness < 0.85:
        return 0
    # If none of the above, default to sleep
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)