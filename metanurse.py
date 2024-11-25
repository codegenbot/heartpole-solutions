import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.2 or time_since_slept > 12:
        return 3

    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.05:
        return 0

    if alertness <= 0.6 and hypertension < 0.5 and intoxication < 0.1:
        return 1

    if alertness <= 0.5 and intoxication < 0.15:
        return 2

    if time_since_slept > 7 and alertness <= 0.7 and hypertension < 0.5:
        return 1

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)