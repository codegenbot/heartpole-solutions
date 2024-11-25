import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if high hypertension or high intoxication or haven't slept for too long
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept >= 8:
        return 3
    # Sleep if alertness is very low
    if alertness < 0.3:
        return 3
    # Drink coffee and work if alertness is low and hypertension is not a concern
    if alertness < 0.5 and hypertension < 0.1:
        return 1
    # Avoid beer if intoxication is even slightly present and work if possible
    if intoxication >= 0.05:
        return 0
    # Otherwise, just work if alertness is high enough
    if alertness >= 0.6:
        return 0
    return 0  # Default action is to work if all conditions are safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)