import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk
    if hypertension >= 0.02 or intoxication >= 0.015:
        return 3

    # Sleep if alertness is dangerously low or after long periods without sleep
    if alertness < 0.6 or time_since_slept > 8:
        return 3

    # Drink coffee to boost moderate alertness if hypertension is safe
    if 0.6 <= alertness < 0.8 and hypertension < 0.012:
        return 1

    # Continue working with high alertness and low health risks
    if alertness >= 0.8 and hypertension <= 0.01 and intoxication <= 0.01:
        return 0

    # If alertness is low and intoxication moderate, drink beer to relax
    if alertness < 0.6 and intoxication < 0.012:
        return 2

    # Default to just work if no conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)