import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health indicators reach critical levels
    if hypertension >= 0.3 or intoxication >= 0.05 or alertness <= 0.6 or time_since_slept >= 6:
        return 3
    # Use coffee if alertness is low but hypertension is under control
    if alertness < 0.75 and hypertension < 0.25:
        return 1
    # Default action is just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)