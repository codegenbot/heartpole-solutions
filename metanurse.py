import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusted thresholds to be more health conscious
    if hypertension > 0.15 or intoxication > 0.08 or alertness < 0.6 or time_since_slept > 6:
        return 3
    if alertness < 0.8 and hypertension < 0.12 and intoxication < 0.05:
        return 1
    # Allow beer if under pressure but hypertension is manageable
    if intoxication < 0.05 and hypertension < 0.12:
        return 2
    if alertness >= 0.85 and hypertension < 0.1 and intoxication < 0.02:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)