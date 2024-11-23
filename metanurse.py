import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep if there's significant health risk
    if time_since_slept > 8:
        return 3
    if alertness < 0.5 and hypertension < 0.5:
        return 1
    if work_done < 0.8 and alertness >= 0.5:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)