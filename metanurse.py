import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are high
    if hypertension > 0.25 or intoxication > 0.25 or time_since_slept > 5:
        return 3
    # Drink coffee to boost alertness if safely under health thresholds
    if alertness < 0.5 and hypertension < 0.15 and intoxication < 0.1:
        return 1
    # Work if alertness is high and health indicators are low
    if alertness >= 0.7 and hypertension < 0.15 and intoxication < 0.05:
        return 0
    # Drink beer only if work done is high and health indicators are low
    if (
        work_done > 8
        and alertness > 0.4
        and intoxication < 0.15
        and hypertension < 0.15
    ):
        return 2
    # Default to sleeping to recover
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)