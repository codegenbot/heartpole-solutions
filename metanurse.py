import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for very low alertness or extended sleep deprivation
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # sleep

    # Prevent high hypertension, prioritize health
    if hypertension >= 0.07:
        return 3  # sleep

    # Use coffee to quickly boost alertness without raising hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.05:
        return 1  # drink coffee and work

    # Maintain a healthy state to work efficiently
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.03:
        return 0  # just work

    # Avoid drinking beer since intoxication impairs health
    if work_done < 0.1 and intoxication < 0.02:
        return 2  # drink beer

    # Default to work if all else is balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)