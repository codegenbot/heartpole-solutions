import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust sleep priority and consider overall perceived fatigue
    if hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 8 or alertness < 0.4:
        return 3  # Sleep

    # Avoid risky actions if both hypertension or intoxication is near critical
    if any([hypertension > 0.2, intoxication > 0.1]):
        return 0  # Just work

    # Consider coffee if alertness is moderately low and health is stable
    if 0.4 <= alertness < 0.6 and hypertension < 0.2 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Make use of beer if alert but with moderate-to-low hypertension, ensure not intoxicated
    if alertness > 0.6 and hypertension < 0.15 and intoxication <= 0.05:
        return 2  # Drink beer and work

    # Default action, just work if all conditions appear balanced
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)