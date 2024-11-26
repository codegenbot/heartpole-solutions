import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 4 or alertness < 0.5 or intoxication > 0.15:
        return 3
    if alertness >= 0.75 and hypertension < 0.02 and intoxication < 0.05:
        return 0
    if alertness >= 0.6 and hypertension < 0.03 and time_elapsed % 5 != 0:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)