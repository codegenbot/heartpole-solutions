import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if severely sleep deprived or high hypertension/intoxication is detected
    if (
        alertness < 0.2
        or time_since_slept >= 6
        or hypertension > 0.006
        or intoxication > 0.07
    ):
        return 3
    # Use coffee only if alertness is low, but hypertension is under control, and it's been a reasonable time since sleep
    if alertness < 0.4 and time_since_slept < 3 and hypertension < 0.005:
        return 1
    # Regular work if alertness and health parameters are adequate
    if 0.6 <= alertness and hypertension < 0.006 and intoxication < 0.05:
        return 0
    # Default to cautious work
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)