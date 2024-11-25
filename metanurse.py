import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.40 or intoxication > 0.10 or alertness < 0.60 or time_since_slept > 5:
        return 3
    if alertness < 0.70 and hypertension < 0.20:
        return 1
    if 0.05 < intoxication < 0.10 and hypertension < 0.25 and alertness > 0.70:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)