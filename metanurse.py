import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for maintaining health and productivity
    if alertness < 0.3 or time_since_slept > 7 or hypertension > 0.5:
        return 3
    # Drink coffee if alertness is low and it's safe
    if alertness < 0.5 and hypertension < 0.4 and intoxication <= 0.3:
        return 1
    # Drink beer if sleep is less of an issue, but alertness can be boosted
    if alertness < 0.5 and intoxication <= 0.2 and time_since_slept <= 6:
        return 2
    # Just work if conditions are optimal
    if alertness >= 0.5 and intoxication <= 0.2:
        return 0
    # Default action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)