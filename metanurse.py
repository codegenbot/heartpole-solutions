import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.08 or intoxication > 0.04 or alertness < 0.5 or time_since_slept >= 6:
        return 3
    if alertness < 0.85 and hypertension < 0.04 and intoxication < 0.02 and time_since_slept < 4:
        return 1
    if alertness < 0.75 and hypertension < 0.03 and intoxication < 0.02:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)