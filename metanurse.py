import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.1 or intoxication > 0.08 or time_since_slept >= 4:
        return 3
    if 0.4 <= alertness < 0.55 and hypertension < 0.04 and intoxication < 0.04:
        return 1
    if alertness >= 0.55 and hypertension < 0.03 and intoxication < 0.03:
        return 0
    if work_done < 0.05 and intoxication <= 0.01 and alertness < 0.25:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)