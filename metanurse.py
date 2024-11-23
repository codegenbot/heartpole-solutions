import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If sleep is needed based on alertness or sleep time, prioritize it
    if alertness < 0.5 or time_since_slept > 12:
        return 3  # Sleep for recovery

    # Check if hypertension or intoxication is at a critical level
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep to reduce health risks

    # Use coffee when alertness is below productivity threshold without excessive health risk
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.35:
        return 1  # Drink coffee to boost alertness

    # Work when conditions are optimal for productivity
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Work

    # Consider beer if moderate hypertension without risk of intoxication
    if 0.4 <= hypertension < 0.6 and intoxication < 0.25:
        return 2  # Drink beer to relax

    # Default to working if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)