import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or hypertension > 0.6 or intoxication > 0.5:
        return 3
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.3:
        return 1
    if alertness >= 0.5 and intoxication <= 0.2:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)