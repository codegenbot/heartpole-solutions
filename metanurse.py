import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is very low or health is compromised
    if (
        alertness < 0.3
        or hypertension > 0.07
        or intoxication > 0.08
        or time_since_slept >= 8.0
    ):
        return 3
    # Increase alertness with coffee if it is moderate and blood pressure allows
    if alertness < 0.5 and hypertension <= 0.04:
        return 1
    # If alertness is good, manage stress with beer
    if 0.5 <= alertness < 0.7 and intoxication <= 0.03 and hypertension <= 0.025:
        return 2
    # Default to work under optimal conditions
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)