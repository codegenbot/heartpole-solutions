import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep when there's a significant health risk
    if hypertension > 0.02 or intoxication > 0.12:
        return 3  # sleep if serious health risks
    if alertness < 0.3 or time_since_slept >= 9:
        return 3  # sleep to recover when very low alertness or lack of sleep
    if alertness < 0.6 and hypertension < 0.015 and intoxication < 0.1:
        return 1  # use coffee if alertness is moderately low and health parameters are safe
    return 0  # work if all metrics are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)