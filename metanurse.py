import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if lack of sleep is noticeable or intoxication is high
    if alertness < 0.5 or time_since_slept >= 4 or intoxication > 0.1:
        return 3
    # Drink coffee if slight alertness improvement is needed and hypertension allows
    if 0.5 <= alertness < 0.7 and hypertension < 0.05:
        return 1
    # Drink beer occasionally if alertness and health conditions are moderate
    if alertness >= 0.7 and intoxication < 0.02 and hypertension < 0.01:
        return 2
    # Default to working directly if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)