import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if significantly overdue or health metrics are poor
    if time_since_slept >= 5.0 or alertness < 0.3 or hypertension > 0.08 or intoxication > 0.06:
        return 3
    
    # Use coffee to boost productivity when alertness is moderate and health allows
    if 0.3 <= alertness < 0.65 and hypertension < 0.06 and intoxication < 0.05 and time_since_slept < 4.0:
        return 1
    
    # Work if you are alert and health metrics are good
    if alertness >= 0.65 and hypertension < 0.04 and intoxication < 0.03:
        return 0
    
    # Consider beer to relax when work done is very low and alertness is poor, not frequently
    if work_done < 0.01 and intoxication <= 0.02 and alertness < 0.25 and time_since_slept < 3.0:
        return 2
    
    # Default to working if no explicit other action is required
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)