import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health indicators more strongly
    if hypertension > 0.75 or intoxication > 0.4:
        return 3  # Sleep
    
    # Ensure adequate rest based on alertness and sleep time
    if time_since_slept >= 5 or alertness < 0.55:
        return 3  # Sleep
    
    # Use coffee cautiously to improve alertness without risking hypertension
    if alertness < 0.65 and hypertension <= 0.3:
        return 1  # Drink coffee and work
    
    # Optimize work when conditions are favorable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)