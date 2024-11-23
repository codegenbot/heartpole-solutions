import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.12 or intoxication >= 0.08 or time_since_slept >= 5:
        return 3  # Sleep

    if alertness < 0.4 and hypertension < 0.08 and intoxication < 0.03:
        return 1  # Drink coffee and work

    if alertness >= 0.6 and hypertension < 0.08 and intoxication < 0.03:
        return 0  # Just work

    return 3  # Default to sleep if conditions are uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)