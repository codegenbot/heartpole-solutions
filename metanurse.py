import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health indicator is critical or it's been a long time since sleeping
    if hypertension > 0.25 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # Sleep

    # Drink coffee if alertness is low but health indicators are fine
    if alertness < 0.6 and hypertension <= 0.2 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Reward consistency in work with just working
    if alertness >= 0.55 and hypertension <= 0.2:
        return 0  # Just work

    # As a reward/relaxation, allow beer only if work is sufficiently progressed
    if work_done >= 50 and intoxication < 0.15:
        return 2  # Drink beer and work

    # Default to working if none of the conditions match
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)