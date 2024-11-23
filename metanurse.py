import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Highest priority to prevent critical health issues
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 5:
        return 3  # Sleep

    # Conditions to increase alertness or reduce intoxication appropriately
    if alertness < 0.5 and time_since_slept <= 5:
        return 1  # Drink coffee and work
    
    if intoxication > 0.2:
        return 3  # Prefer sleep to avoid extra beer's negative effects unless critical
        
    # Work efficiently when conditions are optimal
    if alertness >= 0.65 and intoxication <= 0.15 and hypertension <= 0.2:
        return 0  # Just Work

    # Default to safe action of sleeping if uncertain
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)