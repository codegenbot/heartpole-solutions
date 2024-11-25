import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.15 or intoxication > 0.05 or alertness < 0.4 or time_since_slept > 4:
        return 3
    if alertness < 0.5 and hypertension <= 0.1 and intoxication < 0.03 and time_since_slept < 3:
        return 1
    if alertness > 0.8 and hypertension < 0.05 and intoxication < 0.01 and work_done < 0.1:
        return 2
    if alertness > 0.6 and hypertension <= 0.1 and intoxication < 0.03:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)