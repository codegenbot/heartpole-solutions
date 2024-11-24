import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any serious health metric is exceeded
    if alertness < 0.5 or time_since_slept > 5 or hypertension >= 0.5 or intoxication >= 0.4:
        return 3  # Sleep to recover and prevent health risks

    # Drink coffee when alertness is moderate and conditions are otherwise favorable
    if alertness < 0.7 and hypertension < 0.45 and intoxication < 0.35:
        return 1  # Drink coffee and work to improve alertness

    # Work when conditions are good
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.25:
        return 0  # Just work if all health metrics are optimal

    # Default to regular work if no specific conditions above are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)