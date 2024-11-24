import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep on serious health issues
    if time_since_slept > 6 or hypertension >= 0.7 or intoxication >= 0.6:
        return 3
    # Consider sleeping if alertness is low or haven't slept for a while
    if alertness < 0.6 or time_since_slept > 4:
        return 3
    # Drink coffee only if alertness is moderate and other conditions less severe
    if alertness < 0.8 and hypertension < 0.5:
        return 1
    # Work if health metrics are fine
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.2:
        return 0
    # Default to beer if slightly intoxicated, else work
    return 2 if intoxication < 0.4 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)