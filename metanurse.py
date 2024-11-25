import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.08 or intoxication > 0.06 or time_since_slept >= 3:
        return 3
    if 0.5 <= alertness < 0.65 and hypertension < 0.05 and intoxication < 0.02:
        return 1
    if alertness >= 0.65 and hypertension < 0.03 and intoxication < 0.01:
        return 0
    if work_done < 0.03 and intoxication <= 0.01 and alertness < 0.35:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)