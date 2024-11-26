import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # React to any significant health concern with rest
    if hypertension > 0.04 or intoxication > 0.04:
        return 3

    # Require sleep if alertness is too low or haven't slept in a while
    if alertness < 0.6 or time_since_slept > 4:
        return 3

    # Allow coffee to boost alertness if health conditions permit
    if alertness < 0.75:
        if hypertension < 0.02 and intoxication < 0.02:
            return 1

    # Continue working if high alert and stable health
    if alertness >= 0.75:
        if hypertension < 0.01 and intoxication < 0.01:
            return 0

    # Schedule rest based on work done and time elapsed
    if work_done > 15 and time_elapsed > 40:
        return 3

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)