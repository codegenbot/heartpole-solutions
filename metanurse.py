import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or alertness < 0.3:
        return 3
    if alertness >= 0.85 and hypertension <= 0.15 and intoxication <= 0.1:
        return 0
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.15:
        return 1
    if alertness < 0.5 and intoxication < 0.1 and hypertension < 0.15 and time_since_slept <= 5:
        return 2
    return 3 if time_since_slept > 6 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)