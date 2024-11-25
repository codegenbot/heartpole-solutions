import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping for critical conditions
    if hypertension > 0.12 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # urgent need for sleep

    # Address moderate sleep needs or low alertness
    if time_since_slept > 5 or alertness < 0.4:
        return 3  # sleep to recover alertness

    # Use coffee to improve alertness without health risk
    if 0.4 <= alertness < 0.7 and hypertension < 0.08:
        return 1  # boost alertness with coffee

    # Optimal working conditions purely for productivity
    if alertness >= 0.7 and hypertension < 0.12 and intoxication < 0.05:
        return 0  # optimal state for working

    # Default to working if no major health concerns
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)