import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical conditions
    if (
        hypertension > 0.012
        or intoxication > 0.04
        or alertness < 0.5
        or time_since_slept > 5
    ):
        return 3

    # Use coffee carefully for low alertness without critical health impacts
    if 0.5 <= alertness < 0.6 and hypertension < 0.009 and intoxication < 0.02:
        return 1

    # Save beer for extreme productivity pushes but ensure minimal health risks
    if (
        alertness > 0.6
        and time_elapsed % 250 == 0
        and hypertension < 0.007
        and intoxication < 0.01
    ):
        return 2

    # Default to work under balanced conditions
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)