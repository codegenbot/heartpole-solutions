import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 9:
        return 3
    if 0.5 <= alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.15:
        return 1
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0
    if work_done >= 0.75:
        return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)