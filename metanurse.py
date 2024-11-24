import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.7 or intoxication >= 0.5 or time_since_slept > 8:
        return 3
    
    if 0.4 <= alertness < 0.6 and hypertension < 0.6 and intoxication <= 0.3:
        return 1

    if alertness >= 0.6 and hypertension <= 0.4 and intoxication < 0.2:
        return 0

    if 0.5 <= alertness < 0.6 and intoxication < 0.3 and hypertension < 0.4:
        return 2

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)