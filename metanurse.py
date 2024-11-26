import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: Immediate sleep for critical health values
    if hypertension > 0.01 or intoxication > 0.025:
        return 3

    # Sleep if alertness is too low or it has been too long since last sleep
    if alertness < 0.7 or time_since_slept > 2.0:
        return 3

    # Use coffee cautiously and only if both hypertension and intoxication are low
    if alertness < 0.8 and hypertension < 0.007 and intoxication < 0.01:
        return 1

    # Beer should be used very cautiously; examine the trade-offs carefully
    if (
        0.7 <= alertness < 0.75
        and 0.007 < hypertension <= 0.009
        and intoxication < 0.02
    ):
        return 2

    # Work default if no other conditions are met
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)