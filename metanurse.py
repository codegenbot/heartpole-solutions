import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.012 or intoxication > 0.03:
        return 3
    if time_since_slept > 4 or alertness < 0.5:
        return 3
    if 0.5 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.02:
        return 1
    if time_elapsed >= 250 and time_elapsed % 200 == 0 and hypertension < 0.007 and intoxication < 0.01:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)