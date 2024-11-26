import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.012 or intoxication > 0.15:
        return 3
    if time_since_slept >= 8:
        return 3
    if alertness < 0.4:
        return 3
    if alertness < 0.6 and hypertension < 0.008 and intoxication < 0.08:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)