import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health parameters are concerning
    if hypertension > 0.4 or intoxication > 0.3:
        return 3
    
    # Require sleep if alertness is very low, regardless of work done
    if alertness < 0.3:
        return 3
    
    # Encourage rest/coffee if moderately sleep deprived or alertness is low and still early in the cycle
    if time_since_slept > 16:
        return 3
    if alertness < 0.5 and time_elapsed < 8:
        return 1
    
    # If overall conditions are good, just work
    if alertness >= 0.6 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0
    
    # If time is advanced, favor resting when alertness is low
    if time_elapsed >= 12:
        return 3 if alertness < 0.4 else 0

    # Default to coffee and work if not fully alert
    return 1 if alertness < 0.6 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)