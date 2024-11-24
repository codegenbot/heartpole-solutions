import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for serious health concerns
    if time_since_slept > 8 or hypertension >= 0.7 or intoxication >= 0.6:
        return 3
    # Sleep if alertness is low and time since last sleep is high
    if alertness < 0.5 or time_since_slept > 6:
        return 3
    # Use coffee when alertness is moderately low
    if alertness < 0.6 and hypertension < 0.6:
        return 1
    # Work when alertness is high and health metrics are safe
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    # Use beer sparingly if intoxication is acceptable
    return 2 if intoxication < 0.4 else 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)