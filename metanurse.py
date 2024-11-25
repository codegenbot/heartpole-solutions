import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.15:
        return 3
    if alertness < 0.6 or time_since_slept > 6:
        return 3
    if alertness < 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    if alertness >= 0.9 and hypertension < 0.1 and intoxication < 0.05 and work_done < 0.4:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)