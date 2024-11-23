import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health-first considerations
    if hypertension > 0.65 or intoxication > 0.45:
        return 3  # Sleep to reduce hypertension/intoxication
    if time_since_slept > 16 or alertness < 0.25:
        return 3  # Critical need for sleep
    
    # Strategic balancing of productivity and alertness
    if alertness < 0.6 and hypertension < 0.3:
        return 1  # Drink coffee to boost alertness and work
    
    # Normal working conditions
    if alertness >= 0.5 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0  # Continue work if conditions are favorable
    
    # Default to working, if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)