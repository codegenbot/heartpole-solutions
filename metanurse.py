import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.1:
        return 3  # health risk, prioritize sleep
    if time_since_slept >= 5:
        return 3  # take periodic breaks
    if alertness < 0.3:
        return 3  # avoid overwork with low alertness
    if alertness < 0.65 and hypertension < 0.015 and intoxication < 0.07:
        return 1  # boost alertness if safe
    return 0  # default to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)