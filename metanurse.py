import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or time_since_slept >= 6 or hypertension > 0.15 or time_elapsed > 10:
        return 3
    
    if 0.4 <= alertness < 0.7 and hypertension <= 0.05 and intoxication < 0.05:
        return 1
    
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 0
    
    if intoxication < 0.05 and work_done > 5 and time_elapsed % 10 == 0:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)