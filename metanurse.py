import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if moderate health levels are met or work is excessive.
    if hypertension >= 0.25 or intoxication >= 0.05 or alertness <= 0.65 or time_since_slept >= 5 or work_done >= 0.8:
        return 3
    # Use coffee if alertness is low but not near sleep requirement or high hypertension
    if alertness < 0.75 and hypertension < 0.2 and time_since_slept < 4:
        return 1
    # Default action is just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)