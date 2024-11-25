import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on a more relaxed alertness threshold and other health checks
    if (
        alertness < 0.5
        or hypertension > 0.1
        or intoxication > 0.1
        or time_since_slept >= 5
    ):
        return 3

    # Use coffee when alertness is moderate but without pushing hypertension or intoxication
    if 0.5 <= alertness < 0.7 and hypertension <= 0.07 and intoxication <= 0.05:
        return 1

    # Only work directly when optimal health and alertness metrics are achieved
    if alertness >= 0.7 and hypertension <= 0.05 and intoxication < 0.05:
        return 0

    # Consider beer when work_done is zero to kick start, avoid otherwise
    if work_done == 0 and intoxication <= 0.03 and alertness < 0.4:
        return 2

    # Default working when conditions for others aren't met but above critical thresholds
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)