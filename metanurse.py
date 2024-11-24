import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for any critical health indicators or not enough sleep
    if (
        hypertension > 0.7
        or intoxication > 0.6
        or time_since_slept > 7
        or alertness < 0.5
    ):
        return 3
    # Use coffee only when alertness is moderate and other metrics are safe
    if 0.5 <= alertness < 0.65 and hypertension < 0.4 and intoxication < 0.3:
        return 1
    # Work quietly only when alertness is high and health metrics are low
    if alertness >= 0.65 and hypertension < 0.35 and intoxication < 0.25:
        return 0
    # Default to beer if other less demanding options have been exhausted
    return 2


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)