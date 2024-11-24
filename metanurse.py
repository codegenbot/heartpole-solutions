import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if urgently needed based on low alertness or high health risk
    if alertness <= 0.4 or hypertension >= 0.6 or intoxication >= 0.6 or time_since_slept > 8:
        return 3  # Must sleep to recover

    # Work if conditions are optimal
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work

    # Drink coffee to boost alertness safely
    if alertness < 0.8 and hypertension < 0.4 and intoxication < 0.4:
        return 1  # Drink coffee and work

    # Use beer as a last resort when alertness drops and safe to consume
    if alertness < 0.5 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to sleep if no safe action is clear

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)