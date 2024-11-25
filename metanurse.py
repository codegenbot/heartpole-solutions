import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.6 or time_since_slept >= 8 or hypertension > 0.03:
        return 3
    if alertness < 0.7 and hypertension < 0.03 and intoxication <= 0.02:
        return 1
    if alertness >= 0.8 and hypertension < 0.025 and intoxication < 0.03:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)