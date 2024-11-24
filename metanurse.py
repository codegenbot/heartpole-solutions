import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health concerns first
    if hypertension > 0.7 or intoxication > 0.3:
        return 3  # Sleep to reduce stress and intoxication
    
    # Check if need sleep based on alertness and time since last sleep
    if time_since_slept >= 6 or alertness < 0.5:
        return 3  # Sleep to regain alertness
    
    # Use coffee to boost alertness when not hypertensive
    if alertness < 0.7 and hypertension <= 0.4:
        return 1  # Drink coffee and work
    
    # Normal work condition
    if alertness >= 0.7 and hypertension < 0.4:
        return 0  # Just work

    # Fallback to sleeping if conditions are not met
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)