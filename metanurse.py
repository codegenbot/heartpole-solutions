import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health metrics are risky
    if hypertension >= 0.15 or intoxication >= 0.1:
        return 3  # Sleep

    # Sleep for alertness below threshold or if awake for too long
    if alertness < 0.4 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee to boost alertness within safe bounds
    if alertness < 0.7 and hypertension < 0.12 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Default to work if conditions are safe and productive
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)