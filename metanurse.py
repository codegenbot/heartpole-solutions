import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.01 or intoxication > 0.1 or alertness < 0.3 or time_since_slept >= 10:
        return 3
    if alertness < 0.5 and hypertension < 0.007 and intoxication < 0.05:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)