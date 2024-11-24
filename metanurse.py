import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize serious health concerns: sleep if necessary
    if time_since_slept > 7 or hypertension >= 0.6 or intoxication >= 0.5:
        return 3
    # Moderate health issues or sleep deprivation
    if alertness < 0.5 or time_since_slept > 5:
        return 3
    # Manage alertness if hypertension is acceptable
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 1
    # Safest to work: high alertness and low health risk
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0
    # Default safe action
    return 2 if intoxication < 0.25 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)