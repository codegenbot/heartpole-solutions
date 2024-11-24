import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if key thresholds are exceeded indicating poor health
    if alertness < 0.35 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Must sleep to recover

    # Just work if alertness is high and health indicators are in a safe zone
    if alertness > 0.9 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work

    # Use coffee for an alertness boost within moderate range if health is stable
    if 0.6 <= alertness <= 0.9 and hypertension < 0.55 and intoxication < 0.35:
        return 1  # Drink coffee and work

    # Drink beer and work when alertness is moderate-low but intoxication and hypertension are low
    if 0.5 <= alertness < 0.6 and intoxication < 0.2 and hypertension < 0.5:
        return 2  # Drink beer and work

    # Default to sleeping for recovery in uncertain scenarios
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)