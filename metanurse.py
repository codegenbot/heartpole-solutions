import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk
    if hypertension > 0.015 or intoxication > 0.01:
        return 3

    # Sleep if alertness too low or after shorter periods without sleep
    if alertness < 0.75 or time_since_slept >= 5:
        return 3

    # Broaden decision to drink coffee to improve productivity
    if 0.7 <= alertness < 0.85 and hypertension < 0.01:
        return 1

    # Drink beer for stress relief under safe conditions
    if 0.85 <= alertness < 0.9 and hypertension < 0.015 and intoxication < 0.005:
        return 2

    # Just work if alertness high and health risks are controlled
    if alertness >= 0.9 and hypertension <= 0.008 and intoxication <= 0.004:
        return 0

    # Default to just work if no specific conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)