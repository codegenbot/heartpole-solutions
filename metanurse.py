import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low or if it's been a long time since last slept
    if alertness < 0.65 or time_since_slept > 6:
        return 3
    # Sleep if hypertension is above a critical threshold
    if hypertension > 0.40:
        return 3
    # Sleep if intoxication is above a critical threshold
    if intoxication > 0.20:
        return 3
    # If alertness is slightly low and health conditions are within safe limits, use coffee
    if alertness < 0.75 and hypertension <= 0.35 and intoxication < 0.10:
        return 1
    # Default action is to just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)