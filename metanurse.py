import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If alertness is too low or health metrics are risky, prioritize sleep
    if alertness <= 0.3 or hypertension >= 0.7 or intoxication >= 0.7 or time_since_slept > 6:
        return 3  # Sleep to recover

    # If alertness is high and no immediate health concern, keep working
    if alertness > 0.9 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Just work

    # Drink coffee if alertness is moderate to remain productive without adverse health impacts
    if 0.3 < alertness <= 0.9 and hypertension < 0.4 and intoxication < 0.4:
        return 1  # Drink coffee and work

    # Consider drinking beer if hypertension is low but intoxication is starting to rise
    if 0.3 < alertness <= 0.6 and hypertension < 0.4 and intoxication < 0.6:
        return 2  # Drink beer and work

    # Default to rest by sleeping if any significant health concern persists
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)