import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if severely lacking, or after long wake duration
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep
    
    # Avoid any action if hypertensive
    if hypertension > 0.6:
        return 3  # Sleep

    # Use coffee to boost alertness safely when needed
    if alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Choose to work when conditions are optimal
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work safely

    # Default to sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)