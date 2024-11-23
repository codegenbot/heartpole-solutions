import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.3 or hypertension >= 0.25 or intoxication >= 0.25:
        return 3  # Sleep

    if time_since_slept > 10:
        return 3  # Sleep

    if alertness < 0.6 and hypertension < 0.1:
        return 1  # Drink coffee and work

    if alertness >= 0.65:
        return 0  # Just work

    return 0  # Default to work if conditions are moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)