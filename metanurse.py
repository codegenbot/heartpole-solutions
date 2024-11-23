import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if intoxication > 0.3 or hypertension > 0.45:
        return 3
    
    if time_since_slept > 8 and alertness < 0.5:
        return 3
    
    if alertness < 0.4:
        return 3
    
    if alertness < 0.6 and time_elapsed < 12 and work_done < 0.5:
        return 1
    
    if alertness > 0.6 and hypertension < 0.2 and intoxication < 0.15:
        return 0
    
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)