import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any health risk is present
    if hypertension > 0.015 or intoxication > 0.09:
        return 3
    # Sleep based on alertness and time since last slept
    if time_since_slept >= 5 or alertness < 0.4:
        return 3
    # Coffee to boost work unless health conditions are risky
    if alertness < 0.7 and hypertension < 0.012 and intoxication < 0.06:
        return 1
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)