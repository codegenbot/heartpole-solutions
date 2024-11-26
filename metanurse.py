import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if lack of sleep is noticeable or intoxication is high
    if alertness < 0.5 or time_since_slept >= 5 or intoxication > 0.15:
        return 3
    # Stay cautious with hypertension and intoxication levels
    if alertness < 0.7 and hypertension < 0.02:
        return 1
    # Avoid increasing intoxication too quickly
    if 0.70 <= alertness < 0.80 and intoxication < 0.10 and hypertension < 0.02:
        return 2
    # Default to working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)