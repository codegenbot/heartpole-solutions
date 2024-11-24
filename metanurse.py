import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # IMMEDIATE: Sleep if hypertension/intoxication is moderately high
    if hypertension > 0.08 or intoxication > 0.08:
        return 3

    # Sleep if significant time passed since last sleep or overall time
    if time_since_slept > 4 or time_elapsed > 12:
        return 3

    # Drink coffee if alertness is low and health indicators permit
    if alertness < 0.7 and hypertension < 0.06 and intoxication < 0.05:
        return 1

    # Prefer working if balanced and alertness is moderately sufficient
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.02:
        return 0

    # Use beer only if intoxication is extremely low and productivity high
    if work_done > 25 and alertness > 0.7 and intoxication < 0.02:
        return 2

    # Default to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)