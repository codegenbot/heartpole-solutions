import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if alertness is too low or hasn't slept for long
    if alertness < 0.5 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is moderate and there's no immediate hypertension risk
    if 0.5 <= alertness < 0.75 and hypertension < 0.02:
        return 1

    # Drink beer if hypertension is low and intoxication is manageable,
    # to help balance alertness when it's getting low
    if alertness < 0.5 and hypertension < 0.02 and intoxication < 0.05:
        return 2

    # Work if alertness is high and health risks are low
    if alertness >= 0.75:
        return 0

    # Default to just work under normal conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)