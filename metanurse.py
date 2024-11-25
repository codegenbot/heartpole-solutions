import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.25 or intoxication >= 0.04 or alertness <= 0.5 or time_since_slept >= 5:
        return 3
    if alertness < 0.65 and hypertension < 0.2:
        return 1
    if intoxication < 0.03:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)