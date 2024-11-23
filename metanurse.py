import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if there's significant health risk
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep to offset health issues
    
    if time_since_slept > 10 or (alertness < 0.3 and time_elapsed >= 16):
        return 3  # Sleep if awake too long or very low alertness late in day
    
    if alertness < 0.5:
        if time_elapsed < 8: 
            return 1  # Coffee if worktime and low alertness
        return 3  # Otherwise, rest if alertness is low
    
    if alertness >= 0.5 and work_done < 0.7:
        return 0  # Work if alertness is good and work is incomplete
    
    return 0 if alertness > 0.6 else 3  # Default: Work if alert, otherwise rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)