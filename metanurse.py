import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 8:
        return 3
    if alertness < 0.5 and hypertension < 0.07 and intoxication < 0.02 and time_since_slept < 6:
        return 1
    if alertness >= 0.6 and hypertension <= 0.1 and intoxication <= 0.02:
        return 0
    if work_done < 0.1 and alertness > 0.55 and hypertension < 0.06 and intoxication < 0.01:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)