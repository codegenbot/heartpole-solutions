import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.8 or intoxication > 0.4 or time_since_slept > 7 or alertness < 0.4:
        return 3  # Sleep

    if alertness >= 0.9 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    if 0.7 <= alertness < 0.9 and hypertension <= 0.55:
        return 1  # Drink coffee and work

    if alertness >= 0.5 and hypertension > 0.6 and intoxication <= 0.3:
        return 2  # Drink beer and work

    return 3  # Default to sleep if other conditions don't match

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)