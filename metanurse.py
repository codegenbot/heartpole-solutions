import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    if time_since_slept > 12 or (time_since_slept > 10 and alertness < 0.5):
        return 3
    if alertness < 0.3 and time_since_slept <= 10 and hypertension < 0.3:
        return 1
    if work_done < 0.8:
        if alertness > 0.5:
            return 0
        else:
            return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)