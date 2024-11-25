import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5 or hypertension > 0.35 or intoxication > 0.1:
        return 3
    if alertness < 0.75 and hypertension < 0.25 and time_since_slept < 4:
        return 1
    if hypertension > 0.25 and intoxication < 0.05:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)