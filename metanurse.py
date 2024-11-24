import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for low alertness or excessive time without sleep
    if time_since_slept >= 6 or alertness < 0.5:
        return 3  # Sleep

    # Consider drinking coffee to boost alertness if not too close to hypertension limits
    if alertness < 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Avoid beer if hypertension is high; use it only for specific situations
    if 0.4 <= hypertension <= 0.7 and intoxication < 0.2:
        return 2  # Drink beer and work

    # If all parameters are optimal, focus on work
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.15:
        return 0  # Just work

    # Default to sleep if none of the above conditions are met
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)