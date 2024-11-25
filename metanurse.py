import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or hypertension > 0.6 or alertness < 0.4:
        return 3
    if alertness > 0.8 and hypertension < 0.2 and intoxication < 0.05:
        return 0
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.05:
        return 1
    if intoxication == 0.0 and hypertension > 0.3 and alertness < 0.5:
        return 2
    
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)