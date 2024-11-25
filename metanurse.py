import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.6 or hypertension >= 0.2 or intoxication >= 0.1 or time_since_slept > 6:
        return 3  # Prioritize sleep for better health management
    if alertness < 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee to boost alertness if health allows
    if alertness > 0.85 and intoxication < 0.02 and hypertension < 0.1:
        return 2  # Drink beer only if health conditions are optimal
    return 0  # Default to working if everything is balanced

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)