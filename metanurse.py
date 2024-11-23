import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.4:
        return 3
    if alertness < 0.4 or time_since_slept > 12:
        return 3
    if alertness < 0.7 and time_elapsed < 8:
        return 1
    if alertness >= 0.6 and hypertension < 0.25 and intoxication < 0.15 and work_done < 0.8:
        return 0
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)