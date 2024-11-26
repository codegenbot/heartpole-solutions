import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.012 or intoxication > 0.05:
        return 3
    
    if time_since_slept >= 3:
        return 3
    
    if alertness < 0.3:
        return 3
    
    if 0.35 <= alertness < 0.5 and hypertension < 0.007:
        return 1
    
    if 0.5 <= alertness < 0.85:
        return 0
    
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)