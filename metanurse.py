import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk
    if hypertension > 0.015 or intoxication > 0.01:
        return 3

    # Sleep if alertness too low or after long periods without sleep
    if alertness < 0.75 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is moderate to improve productivity
    if 0.75 <= alertness < 0.85 and hypertension < 0.01:
        return 1

    # Just work if alertness is high and health risks are low
    if alertness >= 0.85 and hypertension <= 0.01 and intoxication <= 0.005:
        return 0

    # Default to just work if no conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)