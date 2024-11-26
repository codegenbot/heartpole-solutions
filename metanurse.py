import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.15 or intoxication > 0.15:
        return 3  # Sleep when health indicators (hypertension or intoxication) are critically high
    if time_since_slept >= 4:
        return 3  # Sleep when it's been a long time since sleeping
    if alertness < 0.4:
        return 1  # Drink coffee when alertness is low but health indicators are not critical
    if alertness >= 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Work normally when alertness is high and health indicators are low
    return 0  # Default to working if no critical health issues are detected


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)