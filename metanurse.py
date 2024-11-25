import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if intoxication >= 0.3 or time_since_slept > 12:
        return 3  # Prioritize sleep
    if alertness < 0.4 or time_since_slept > 8:
        return 3  # Sleep if very low alertness or too long without sleep
    if hypertension >= 0.07 and intoxication > 0.05:
        return 3  # Sleep in case of combined hypertension and intoxication
    if alertness < 0.7:
        return 1  # Boost alertness with coffee
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)