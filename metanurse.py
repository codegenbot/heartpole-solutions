import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.4:
        return 3
    if alertness < 0.5 or time_since_slept > 10:
        return 3
    if alertness < 0.6 and time_since_slept <= 8:
        return 1
    if alertness >= 0.7 and work_done < 0.9:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)