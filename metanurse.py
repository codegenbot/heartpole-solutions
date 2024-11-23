import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep on higher thresholds to prevent detriment to health
    if hypertension > 0.25 or intoxication > 0.12 or time_since_slept > 5:
        return 3  # Sleep

    # Sleep if alertness is significantly low
    if alertness < 0.65:
        return 3  # Sleep

    # Drink coffee if alertness is low and health indicators are within safe margins
    if 0.65 <= alertness < 0.75 and hypertension <= 0.15 and intoxication <= 0.08:
        return 1  # Drink coffee and work

    # Minimize beer usage; only use for a moderate alertness boost
    if alertness < 0.60 and intoxication <= 0.08:
        return 2  # Drink beer and work

    # Default action: stable work conditions
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)