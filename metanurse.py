import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep for critical health and rest recovery
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.3:
        return 3  # Sleep

    # Ensure regular sleep
    if time_since_slept > 8:
        return 3  # Sleep

    # Manage coffee consumption wisely
    if alertness < 0.6 and hypertension < 0.5 and time_since_slept < 5:
        return 1  # Drink coffee and work

    # Use beer cautiously with very low alertness and low intoxication
    if alertness < 0.45 and intoxication < 0.15:
        return 2  # Drink beer and work

    # Regular work with balanced health
    if alertness >= 0.65 and hypertension < 0.35 and intoxication < 0.25:
        return 0  # Just work

    # Default to safe option (rest)
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)