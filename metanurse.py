import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If too long without sleep, or very low alertness, prioritize sleep
    if time_since_slept > 8 or alertness < 0.3 or hypertension > 0.7:
        return 3  # Need to prioritize sleep
    
    # If sufficiently alert and health indicators are low, focus on working
    if alertness >= 0.8 and hypertension < 0.3 and intoxication == 0.0:
        return 0  # Work
    
    # If alertness can be enhanced without risking health, use coffee
    if alertness >= 0.5 and hypertension < 0.4:
        return 1  # Drink coffee and work
    
    # Only use beer to relax when alertness is low and not intoxicated
    if 0.3 <= alertness < 0.5 and intoxication == 0.0 and hypertension < 0.35:
        return 2  # Drink beer to relax
    
    return 3  # Default to sleep if none other conditions are met safely

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)