import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Serious health concerns have highest priority
    if hypertension > 0.6 or intoxication > 0.35:
        return 3  # Sleep to address health issues
    # Make sure to sleep if alertness is critically low or lack of sleep
    if alertness < 0.4 or time_since_slept > 12:
        return 3  # Sleep to restore alertness or after long awake period
    # Use coffee delicately to manage alertness without overuse
    if alertness < 0.5 and time_since_slept <= 8:
        return 1  # Drink coffee and work if needed
    # If productive and sufficiently alert, focus purely on work
    if alertness >= 0.7 and work_done < 0.9:
        return 0  # Just work if everything is suitable
    return 0  # Default to just work if all other conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)