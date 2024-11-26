import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If alertness is low or have not slept for a long time or too intoxicated, prioritize sleep
    if alertness < 0.6 or time_since_slept >= 4 or intoxication > 0.1:
        return 3
    # Drink coffee if alertness isn't optimal but hypertension is under control
    if alertness < 0.75 and hypertension < 0.05:
        return 1
    # Drink beer if alertness is moderate but avoid if intoxicated or hypertensive
    if 0.75 <= alertness < 0.85 and intoxication < 0.08 and hypertension < 0.03:
        return 2
    # Work if all parameters allow for a safe operation
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)