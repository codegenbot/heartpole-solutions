import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical sleep requirements
    if alertness < 0.4 or hypertension > 0.1 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee to boost alertness safely
    if alertness < 0.6 and hypertension < 0.1:
        return 1  # Drink coffee and work

    # Work if high alertness with safe levels
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 0  # Just work

    # Otherwise, default to safe rest
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)