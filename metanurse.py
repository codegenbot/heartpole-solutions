import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or time_since_slept >= 6:
        return 3  # sleep
    if hypertension > 0.02 or intoxication > 0.1:
        return 3  # sleep
    if 0.5 <= alertness < 0.7 and time_since_slept < 3:
        return 1  # drink coffee and work
    if 0.7 <= alertness < 0.8 and hypertension < 0.002 and intoxication < 0.03:
        return 2  # drink beer and work
    return 0  # just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)