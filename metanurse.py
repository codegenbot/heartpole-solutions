import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.2 or alertness < 0.5 or time_since_slept > 8:
        return 3
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 1
    if alertness >= 0.7 and hypertension <= 0.25 and intoxication == 0.0 and time_since_slept <= 5:
        return 0
    if intoxication <= 0.1 and work_done < 0.6:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)