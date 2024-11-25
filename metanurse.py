import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low or it's been a long time since sleep
    if alertness < 0.6 or time_since_slept > 6:
        return 3

    # Avoid caffeine if hypertension is notable
    if hypertension >= 0.06:
        return 3 if alertness < 0.7 else 0

    # Avoid work if intoxication level is present
    if intoxication > 0:
        return 3

    # Use caffeine for productivity if conditions allow
    if alertness < 0.7 and hypertension < 0.04:
        return 1

    # Optimal alertness for productive work
    if alertness >= 0.7:
        return 0

    # Default to cautious work strategy
    return 2 if alertness < 0.65 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)