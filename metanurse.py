import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize serious health concerns: sleep if necessary
    if intoxication >= 0.5 or hypertension >= 0.6 or time_since_slept > 7:
        return 3
    # Moderate health issues or sleep deprivation
    if alertness < 0.5 or time_since_slept > 5:
        return 3
    # Drink coffee to boost alertness if it's moderately low
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.3:
        return 1
    # Safe to work if alertness is good and health risks are low
    if alertness >= 0.75 and hypertension < 0.3 and intoxication < 0.2:
        return 0
    # Default safe action
    return 2 if intoxication < 0.15 and hypertension < 0.2 and alertness >= 0.6 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)