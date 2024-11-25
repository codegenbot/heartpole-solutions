import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.25 or intoxication >= 0.06 or alertness <= 0.6 or time_since_slept > 5:
        return 3
    if alertness < 0.7 and hypertension < 0.1:
        return 1
    if intoxication < 0.04 and hypertension < 0.15 and alertness > 0.75:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)