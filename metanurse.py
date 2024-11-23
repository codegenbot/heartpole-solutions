import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5 or alertness < 0.2:
        return 3

    if time_since_slept > 5.5:
        return 3

    if alertness < 0.4 and hypertension < 0.5:
        return 1

    if 0.5 < hypertension <= 0.6 and intoxication < 0.2:
        return 2

    if alertness >= 0.65 and hypertension < 0.25 and intoxication < 0.2:
        return 0

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)