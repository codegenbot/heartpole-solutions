import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize sleeping if health thresholds are critical
    if hypertension > 0.6 or intoxication > 0.6 or time_since_slept > 6:
        return 3  # Sleep

    # Ensure optimal alertness
    if alertness < 0.5:
        return 3  # Sleep

    # Work if alertness and health are balanced
    if alertness > 0.9 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Drink coffee to boost alertness without major health impact
    if alertness >= 0.5 and alertness < 0.8 and hypertension < 0.5:
        return 1  # Drink coffee and work

    # Beer is a last resort for maintaining alertness during mild intoxication
    if intoxication >= 0.2 and intoxication < 0.5 and alertness >= 0.6:
        return 2  # Drink beer and work

    # Default to rest when potentially risky
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)