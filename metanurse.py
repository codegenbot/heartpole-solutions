import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health risk is significant or if it's time
    if time_since_slept > 6 or alertness < 0.6 or hypertension > 0.08 or intoxication > 0.1:
        return 3

    # Use coffee very sparingly
    if alertness < 0.7 and hypertension < 0.05 and intoxication < 0.03:
        return 1

    # Optimal work conditions
    if alertness >= 0.75 and hypertension < 0.05 and intoxication < 0.02:
        return 0

    # Default: just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)