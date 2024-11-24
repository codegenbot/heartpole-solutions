import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is too low or health risks are too high
    if alertness <= 0.5 or hypertension >= 0.5 or intoxication >= 0.5 or time_since_slept > 6:
        return 3  # Sleep to recover

    # Work if alertness and health are optimal
    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work

    # Drink coffee if alertness is moderate and health risks are low
    if alertness <= 0.8 and hypertension < 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Default to rest by sleeping if any health concern exists
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)