import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if necessary conditions are met
    if time_since_slept >= 8 or alertness < 0.5 or intoxication > 0.15:
        return 3
    # Avoid work if health indicators are concerning
    if hypertension > 0.05 or intoxication > 0.10:
        return 0
    # Optimize periods of high alertness with coffee if safe
    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.05:
        return 1
    # Use beer only as a mild relaxant if conditions are safe
    if alertness < 0.7 and intoxication < 0.08:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)