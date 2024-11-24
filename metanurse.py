import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep more strongly with stricter conditions
    if hypertension > 0.35 or intoxication > 0.25 or time_since_slept > 3:
        return 3  # Must sleep to reduce health risks

    # Adjust the alertness and intoxication thresholds for drinking beer
    if alertness < 0.5 and intoxication <= 0.15:
        return 2  # Drink beer and work for mild alertness improvement

    # Maintain work without drinking if completely alert and healthy
    if alertness >= 0.8 and hypertension <= 0.15 and intoxication < 0.05:
        return 0  # Just work

    # Increase the range and conditions for drinking coffee
    if 0.6 <= alertness < 0.8 and hypertension < 0.25:
        return 1  # Drink coffee and work

    # Default to sleep to err on the side of caution for any uncertainty
    return 3  # Sleep otherwise for recovery


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)