import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health indicators show degradation
    if alertness < 0.5 or hypertension >= 0.5 or intoxication >= 0.3 or time_since_slept >= 6:
        return 3  # Must sleep

    # Work if health parameters are optimal
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Coffee if alertness is reducing but hypertension/intoxication are manageable
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Use beer carefully for minor alertness boost if applicable
    if alertness < 0.6 and intoxication < 0.2 and hypertension < 0.4:
        return 2  # Drink beer and work

    # Default to sleep in case of doubt
    return 3  # Sleep if no better option

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)