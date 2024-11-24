import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Absolute priority on hypertension
    if hypertension > 0.8:
        return 3  # Sleep

    # Handle intoxication
    if intoxication > 0.5:
        return 3  # Sleep

    # Alertness and sleep management
    if time_since_slept >= 8 or alertness < 0.5:
        return 3  # Sleep

    # Use coffee to improve alertness without risking health
    if alertness < 0.6 and hypertension <= 0.5:
        return 1  # Drink coffee and work

    # Normal working condition
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Fallback to sleep if none apply
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)