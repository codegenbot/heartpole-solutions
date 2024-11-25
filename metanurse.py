import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.35 or intoxication >= 0.08 or alertness <= 0.55 or time_since_slept > 6:
        return 3
    if alertness < 0.75 and hypertension < 0.15:
        return 1
    if intoxication < 0.05 and hypertension < 0.20 and alertness > 0.80:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)