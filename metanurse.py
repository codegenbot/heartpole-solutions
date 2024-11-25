import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 8 or hypertension > 0.3 or intoxication > 0.4:
        return 3  # prioritize sleep when severely tired or health indicators are high
    if alertness < 0.6 and hypertension < 0.2:
        return 1  # consume coffee to boost alertness if hypertension is manageable
    if alertness > 0.7 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # work under optimal conditions
    if intoxication < 0.15:
        return 2  # if not intoxicated too much, use beer for relaxation
    return 0  # default to work if no other conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)