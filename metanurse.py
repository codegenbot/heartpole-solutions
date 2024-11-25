import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.75 or intoxication > 0.45 or time_since_slept > 10:
        return 3

    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.1:
        return 0

    if 0.5 <= alertness <= 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 1

    if alertness < 0.5 and hypertension < 0.45 and intoxication < 0.1:
        return 2

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)