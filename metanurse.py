import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk
    if hypertension > 0.015 or intoxication > 0.01:
        return 3

    # Sleep if alertness too low or after moderate periods without sleep
    if alertness < 0.8 or time_since_slept > 5:
        return 3

    # Drink coffee if alertness is moderate and no hypertension risk to boost productivity
    if 0.8 <= alertness < 0.9 and hypertension < 0.012:
        return 1

    # Just work if alertness is high and health risks are low
    if alertness >= 0.9 and hypertension <= 0.01 and intoxication <= 0.005:
        return 0

    # Avoid drinking beer to reduce risk of intoxication
    # Default to just work if no conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)