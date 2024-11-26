import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust hypertension and intoxication thresholds for health prioritization
    if hypertension > 0.02 or intoxication > 0.03:
        return 3
    if time_since_slept > 5:
        return 3

    # Dynamic alertness management considering health and productivity
    if alertness < 0.7:
        if hypertension < 0.02 and intoxication < 0.02:
            return 1

    # Work if alert and health parameters are safe
    if alertness >= 0.75:
        return 0

    # Enforce sleep if work threshold crossed
    if work_done > 12 and time_elapsed > 30:
        return 3

    # Default to sleep to avoid health risks
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)