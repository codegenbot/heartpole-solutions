import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Prioritize sleep to avoid health risks
    if alertness < 0.5 and time_since_slept <= 5 and intoxication < 0.2:
        return 1  # Boost alertness by drinking coffee
    return 0  # Default to working if conditions are safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)