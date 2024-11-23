import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if severe health issues
    if hypertension > 0.4 or intoxication > 0.3:
        return 3  # Sleep to recover from health issues

    # Opt to sleep if time awake is excessive or alertness is very low
    if time_since_slept > 12 or alertness < 0.2:
        return 3

    # Use coffee if alertness is moderate early in the day
    if alertness < 0.6 and time_elapsed < 8:
        return 1

    # Take a beer break if low intoxication, moderate alertness, and productivity is needed
    if (
        intoxication <= 0.2
        and alertness < 0.5
        and work_done < 0.5
        and time_elapsed < 10
    ):
        return 2

    # Work if metrics show reasonable health and productive measures
    if (
        alertness >= 0.4
        and hypertension <= 0.2
        and intoxication <= 0.2
        and work_done < 0.8
    ):
        return 0

    # Prioritize rest in later hours if getting tired
    if alertness < 0.3 and time_elapsed > 10:
        return 3

    # Default action based on greater alertness threshold
    return 0 if alertness >= 0.45 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)