import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is very low, haven't slept for 3 hours or more, or intoxication/hypertension is concerning
    if (
        alertness < 0.65
        or time_since_slept > 3
        or intoxication > 0.08
        or hypertension > 0.03
    ):
        return 3
    # Use coffee more conservatively to boost alertness if conditions permit
    if alertness < 0.8 and hypertension < 0.04 and time_since_slept < 3:
        return 1
    # Avoid beer unless conditions are very safe
    if 0.8 <= alertness < 0.9 and intoxication < 0.05 and hypertension < 0.02:
        return 2
    # Safely work when conditions are optimal
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)