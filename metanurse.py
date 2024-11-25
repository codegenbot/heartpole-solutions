import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 6 or hypertension > 0.25 or intoxication > 0.25:
        return 3  # prioritize sleep to avoid health hazards
    if alertness < 0.65 and hypertension < 0.25:
        return 1  # use coffee to increase alertness if it's safe
    if alertness > 0.75 and hypertension < 0.2 and intoxication == 0:
        return 0  # work efficiently under ideal conditions
    if intoxication < 0.1:
        return 2  # only consider beer if intoxication is very low
    return 0  # default to work if no conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)