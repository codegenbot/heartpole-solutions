import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3
    
    if time_since_slept > 12 or alertness < 0.4:
        return 3
    
    if alertness < 0.5 and work_done < 0.9:
        return 1
    
    return 0 if alertness >= 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)