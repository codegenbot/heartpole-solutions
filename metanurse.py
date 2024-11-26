import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical or moderate health risk
    if hypertension > 0.012 or intoxication >= 0.005:
        return 3

    # Sleep if alertness is too low or after prolonged wakefulness
    if alertness < 0.85 or time_since_slept > 4:
        return 3

    # Drink coffee if slight boost needed and no hypertension risk
    if 0.85 <= alertness < 0.9 and hypertension < 0.008:
        return 1

    # Just work if conditions are optimal
    if alertness >= 0.9 and hypertension <= 0.008 and intoxication <= 0.002:
        return 0

    # Default to just work if nothing else fits
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)