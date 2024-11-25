import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if alertness is too low or hasn't slept for a long time
    if alertness < 0.6 or time_since_slept > 5:
        return 3

    # Drink coffee if alertness is moderate and there's no immediate hypertension risk 
    if 0.6 <= alertness < 0.8 and hypertension < 0.02:
        return 1

    # Work if alertness is moderately high
    if alertness >= 0.8:
        return 0

    # Default to just work if calm beer doesn't improve the situation
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)