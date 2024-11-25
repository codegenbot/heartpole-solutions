import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Tune sleep conditions
    if alertness < 0.5 and (hypertension > 0.75 or intoxication > 0.35 or time_since_slept > 10):
        return 3  # Sleep

    # Refine work conditions
    if alertness > 0.9 and hypertension < 0.65 and intoxication < 0.15:
        return 0  # Just work

    # Moderate use of coffee
    if 0.6 <= alertness < 0.9 and hypertension < 0.7 and intoxication < 0.15:
        return 1  # Coffee and work

    # Restrict beer use
    if alertness < 0.6 and hypertension < 0.55 and intoxication < 0.25:
        return 2  # Beer and work

    # Default to sleep to maintain recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)