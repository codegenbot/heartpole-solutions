import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to combat alertness issues quicker
    if alertness < 0.5 or time_since_slept > 8:
        return 3  # Sleep for recovery

    # Adjust for slightly higher hypertension risk
    if hypertension > 0.4 or intoxication > 0.4:
        return 3  # Sleep to reduce health risks

    # Use coffee with stricter health checks
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.35:
        return 1  # Drink coffee to boost alertness

    # Optimal condition for pure work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Work

    # Allow beer more selectively
    if 0.3 <= hypertension < 0.5 and intoxication < 0.2:
        return 2  # Drink beer to relax

    # Default to working if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)