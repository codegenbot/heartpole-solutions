import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any immediate health concerns are high
    if hypertension >= 0.3 or intoxication >= 0.25:
        return 3  # Sleep

    # Sleep if alertness is critically low or not achieved enough work
    if alertness < 0.5 or work_done < 0.3:
        return 3  # Sleep
    
    # Drink coffee to maintain alertness within reasonable parameters
    if alertness < 0.65 and hypertension < 0.25 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Manage resting intervals to ensure the need for rest
    if time_since_slept > 8:
        return 3  # Sleep

    # Default to working if conditions are reasonably safe
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)