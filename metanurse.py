import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are risky:
    if hypertension > 0.07 or intoxication > 0.15:
        return 3
    if time_since_slept > 5:  # Slightly increased sleep interval
        return 3
    if alertness < 0.4:  # Lowered to ensure sleep when very fatigued
        return 3

    # Coffee to boost alertness when slightly fatigued:
    if 0.4 <= alertness < 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Work when alert and healthy:
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    # Default to sleep if unsure:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)