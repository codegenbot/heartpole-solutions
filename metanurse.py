import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 5 or hypertension > 0.25 or intoxication > 0.25:
        return 3  # prioritize sleep to avoid health hazards
    if alertness < 0.65 and hypertension < 0.25:
        return 1  # use coffee if alertness is low and it's safe
    if 0.65 < alertness < 0.8 and hypertension < 0.2 and intoxication == 0:
        return 0  # work efficiently with good alertness
    return 0  # default to work, avoid beer if intoxication is above 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)