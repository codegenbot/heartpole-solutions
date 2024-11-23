import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate sleep if conditions are critical
    if hypertension > 0.2 or intoxication > 0.15 or time_since_slept > 10:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.4:
        return 3  # Sleep

    # Drink coffee if alertness is moderately low and conditions are fine
    if 0.4 <= alertness < 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Drink beer if intoxication is low and alertness is sufficient while not hypertensive
    if intoxication <= 0.1 and alertness >= 0.7 and hypertension <= 0.2:
        return 2  # Drink beer and work

    # Default working mode in safe and alert conditions
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)