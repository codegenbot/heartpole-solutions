import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.6 or hypertension > 0.3 or intoxication > 0.15 or time_since_slept >= 6:
        return 3
    if alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1
    if alertness > 0.9 and intoxication < 0.05 and hypertension <= 0.2:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)