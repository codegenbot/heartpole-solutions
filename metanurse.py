import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health
    if hypertension > 0.25 or intoxication > 0.25 or time_since_slept > 8:
        return 3  # Sleep

    # Adjust alertness thresholds for optimal productivity
    if alertness < 0.65:
        return 1 if hypertension <= 0.15 else 3  # Drink coffee only if safe

    # Avoid further intoxication if already high
    if intoxication > 0.2:
        return 3  # Sleep to clear intoxication

    # Maximize work efficiency when conditions are optimal
    if alertness >= 0.7 and intoxication <= 0.1:
        return 0  # Just work

    # Default: Maintain current state
    return 3 if alertness < 0.5 else 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)