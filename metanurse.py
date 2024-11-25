import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for critical health risks
    if hypertension > 0.15 or intoxication > 0.1:
        return 3
    # Sleep if significantly fatigued or it's been a long time since last sleep
    if alertness < 0.6 or time_since_slept > 5:
        return 3
    # Drink coffee if alertness is low but health parameters are safe
    if alertness < 0.75 and hypertension < 0.12 and intoxication < 0.05:
        return 1
    # Default: keep working without any substances
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)