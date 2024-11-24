import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.6 or intoxication > 0.5:
        return 3  # Sleep to recover from high risk

    if time_since_slept > 8 or alertness < 0.35:
        return 3  # Sleep due to exhaustion

    if alertness < 0.65 and hypertension < 0.35:
        return 1  # Drink coffee and work to boost alertness

    if intoxication < 0.15 and hypertension < 0.2 and alertness < 0.45:
        return 2  # Drink beer and work sparingly

    if alertness >= 0.65 and hypertension < 0.35 and intoxication < 0.25:
        return 0  # Just work

    return 3  # Default, safe option for uncertain scenarios

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)