import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.5 or intoxication > 0.25 or time_since_slept > 8:
        return 3
    if alertness < 0.7 and hypertension <= 0.45 and intoxication <= 0.15:
        return 1
    if alertness >= 0.7 and hypertension <= 0.35 and intoxication <= 0.1:
        return 0
    if intoxication < 0.05 and hypertension < 0.25:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)