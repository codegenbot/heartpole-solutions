import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if hypertension or intoxication is above safe levels
    if hypertension > 0.15 or intoxication > 0.07:
        return 3
    # Ensure adequate rest based on alertness and time since last slept
    if alertness < 0.7 or time_since_slept > 5:
        return 3
    # Drink coffee to boost alertness safely
    if alertness < 0.85 and hypertension < 0.1 and intoxication < 0.04:
        return 1
    # Consider beer to celebrate/work in long periods when safe
    if time_elapsed > 700 and (hypertension < 0.08 and intoxication < 0.02):
        return 2
    # Default to working if all thresholds are comfortable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)