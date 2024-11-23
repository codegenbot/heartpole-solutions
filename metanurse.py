import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if hypertension or intoxication levels are high
    if hypertension > 0.35 or intoxication > 0.25:
        return 3

    # Opt to sleep based on low alertness or long awake period
    if time_since_slept > 8 or alertness < 0.3:
        return 3

    # Moderate use of coffee only when alertness is low and it's early
    if alertness < 0.4 and time_elapsed < 6 and hypertension < 0.2:
        return 1

    # Be cautious with beer; prefer when intoxication is very low
    if intoxication <= 0.1 and alertness < 0.5 and work_done < 0.5 and time_elapsed < 8:
        return 2

    # Work if health metrics are within acceptable thresholds
    if (
        alertness >= 0.3
        and hypertension <= 0.2
        and intoxication <= 0.1
        and work_done < 0.85
    ):
        return 0

    # Adapt sleeping during late hours based on combined factors
    if alertness < 0.35 and time_elapsed > 8:
        return 3

    # Default: Work if moderate alertness, else rest
    return 0 if alertness >= 0.4 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)