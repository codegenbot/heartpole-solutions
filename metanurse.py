import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if critical thresholds are met
    if alertness < 0.6 or hypertension > 0.12 or intoxication > 0.04 or time_since_slept > 5:
        return 3  # Sleep if critical

    # Use coffee if it can effectively boost alertness safely
    if alertness < 0.75 and hypertension < 0.1 and intoxication < 0.03:
        return 1  # Drink coffee and work

    # Default to just work if conditions are safe
    if hypertension < 0.08 and intoxication < 0.02:
        return 0  # Just work

    return 0  # Fallback to just work if no other conditions apply

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)