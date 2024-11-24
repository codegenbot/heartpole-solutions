import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High priority to sleep on serious health issues
    if time_since_slept > 7 or hypertension >= 0.45 or intoxication >= 0.25:
        return 3
    # Sleep if slightly moderate alertness or sleep deprivation
    if alertness < 0.65 or time_since_slept > 5:
        return 3
    # Moderate alertness, low health risk, need a boost
    if alertness < 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 1
    # Safe to work: good alertness and minimal health risks
    if alertness >= 0.8 and hypertension < 0.15 and intoxication < 0.1:
        return 0
    # Default to taking a careful approach:
    return 2 if intoxication < 0.15 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)