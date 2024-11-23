import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.3 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # sleep
    if alertness < 0.2:
        return 1  # drink coffee and work
    if intoxication > 0.2:
        return 3  # sleep
    if alertness < 0.4:
        return 1  # drink coffee and work
    if time_since_slept > 6:
        return 3  # sleep
    return 0  # just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)