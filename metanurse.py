import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.1 or time_since_slept > 16:
        return 3
    if alertness < 0.3 and hypertension <= 0.4:
        return 1
    if alertness < 0.4 and intoxication <= 0.1:
        return 2
    if alertness >= 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0
    if time_since_slept > 12:
        return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)