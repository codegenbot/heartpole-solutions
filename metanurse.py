import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.10:
        return 3
    if time_since_slept > 6 or alertness < 0.2:
        return 3
    if alertness < 0.5 and hypertension < 0.015 and intoxication < 0.05:
        return 1
    if intoxication > 0.04 and hypertension < 0.005:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)