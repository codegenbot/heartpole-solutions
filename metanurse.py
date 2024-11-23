import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if hypertension, intoxication, or lack of sleep are critical
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    # Encourage sleep if alertness drops significantly
    if alertness < 0.4:
        return 3  # Sleep

    # Use coffee if alertness is low while maintaining safe thresholds
    if 0.4 <= alertness < 0.6 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Consider using beer for slight alertness boost without exceeding intoxication
    if 0.4 <= alertness < 0.5 and 0.1 < intoxication <= 0.15:
        return 2  # Drink beer and work

    # Regular work if conditions are optimal
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)