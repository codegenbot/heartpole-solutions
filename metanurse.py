import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3

    if alertness < 0.4:
        return 3
    
    if alertness < 0.55 and time_elapsed < 6 and work_done < 0.3:
        return 1
    
    if alertness >= 0.55 and hypertension <= 0.2 and intoxication <= 0.15:
        return 0
    
    if time_elapsed >= 12 and alertness < 0.45:
        return 3

    return 0 if alertness > 0.5 and hypertension <= 0.2 and intoxication <= 0.15 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)