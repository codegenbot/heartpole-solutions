import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if health issues are significant
    if hypertension > 0.35 or intoxication > 0.25:
        return 3

    # Opt to sleep if time awake or low alertness
    if time_since_slept > 10 or alertness < 0.25:
        return 3

    # Use coffee strategically early in the day or if alertness is just below moderate
    if alertness < 0.5 and time_elapsed < 7:
        return 1

    # Refined beer strategy
    if (
        intoxication <= 0.15
        and alertness < 0.5
        and work_done < 0.5
        and time_elapsed < 9
    ):
        return 2

    # Work with reasonable health and productivity measures
    if (
        alertness >= 0.35
        and hypertension <= 0.15
        and intoxication <= 0.15
        and work_done < 0.8
    ):
        return 0

    # Adapt rest in late hours based on combined factors
    if alertness < 0.35 and time_elapsed > 9:
        return 3

    # Final choice based on moderate alertness
    return 0 if alertness >= 0.4 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)