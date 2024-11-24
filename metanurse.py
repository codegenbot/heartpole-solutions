import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Ensure safety first: take breaks when under significant health threat
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep

    # Sleep if heavily fatigued
    if time_since_slept > 8:
        return 3  # Sleep

    # Prioritize work during optimal conditions
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness with acceptable health risk: use coffee for a boost
    if 0.5 <= alertness < 0.8 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Default to resting if certain thresholds are not met
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)