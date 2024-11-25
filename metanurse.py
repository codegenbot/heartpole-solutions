import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.7 or time_since_slept > 4:
        return 3
    if alertness < 0.85 and hypertension < 0.1 and intoxication < 0.05:
        return 1
    if alertness >= 0.85 and hypertension < 0.2 and intoxication == 0.0 and work_done < 0.5:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)