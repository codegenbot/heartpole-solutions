import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health risk conditions
    if hypertension > 0.02 or intoxication > 0.08:
        return 3  # Sleep

    # Management of alertness and work-life balance
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep

    # Use coffee to boost alertness responsibly
    if alertness < 0.7 and hypertension < 0.01:
        return 1  # Drink coffee and work

    # Use beer to relax but keep intoxication in check
    if alertness >= 0.9 and intoxication <= 0.05:
        return 2  # Drink beer and work

    # Limit excessive work
    if work_done > 60:
        return 3  # Sleep

    # Default work option
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)