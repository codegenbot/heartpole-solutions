import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.5:
        return 3
    if time_since_slept > 12 or alertness < 0.25:
        return 3
    if alertness < 0.5 and hypertension < 0.5:
        return 1
    if work_done < 0.8 and alertness >= 0.4:
        return 0
    if alertness < 0.6 and time_elapsed < 16:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)