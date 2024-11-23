import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.3: 
        return 3

    if alertness < 0.5 or time_since_slept > 15:
        return 3

    if alertness < 0.7 and time_elapsed < 10:
        return 1

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)