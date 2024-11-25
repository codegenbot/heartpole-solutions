import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 8:
        return 3
    if alertness < 0.5 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)