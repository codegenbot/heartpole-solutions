import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4:
        return 3
    if alertness < 0.6 and hypertension < 0.35 and intoxication <= 0.2:
        return 1
    if alertness >= 0.8 and hypertension < 0.3 and intoxication <= 0.1:
        return 0
    if alertness < 0.5 and hypertension < 0.4 and intoxication <= 0.3:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)