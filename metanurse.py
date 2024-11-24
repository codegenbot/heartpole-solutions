def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for recovery
    if alertness < 0.6 or time_since_slept > 10:
        return 3  # Sleep for recovery

    # Sleep if hypertension or intoxication implies health risk
    if hypertension > 0.4 or intoxication > 0.3:
        return 3  # Sleep to manage health risks

    # Use coffee cautiously to enhance alertness without health risk
    if alertness < 0.75 and hypertension < 0.2 and intoxication < 0.2:
        return 1  # Drink coffee to boost alertness

    # Work when conditions are optimal
    if alertness >= 0.75 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Work

    # Fallback option
    return 0


import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)