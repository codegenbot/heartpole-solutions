import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if health issues are significant
    if hypertension > 0.3 or intoxication > 0.2:
        return 3

    # Opt to sleep if time awake is long or alertness is very low
    if time_since_slept > 8 or alertness < 0.3:
        return 3

    # Use coffee strategically early in the day or if alertness is just below moderate
    if alertness < 0.6 and time_elapsed < 8:
        return 1

    # Refine beer strategy to be more cautious
    if (
        intoxication <= 0.1
        and alertness < 0.5
        and work_done < 0.6
        and time_elapsed < 10
    ):
        return 2

    # Work with reasonable health and productivity measures
    if (
        alertness >= 0.4
        and hypertension <= 0.1
        and intoxication <= 0.1
        and work_done < 0.75
    ):
        return 0

    # Adapt rest in late hours based on combined factors
    if alertness < 0.35 and time_elapsed > 8:
        return 3

    # Final choice based on moderate alertness
    return 0 if alertness >= 0.45 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)