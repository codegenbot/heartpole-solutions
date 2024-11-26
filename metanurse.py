import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate health by reducing hypertension and intoxication
    if hypertension > 0.15 or intoxication > 0.35:
        return 3  # Sleep for health recovery

    # Strategic sleep: for regular breaks in addition to recovery-based
    if time_since_slept >= 7 or (time_since_slept >= 5 and time_elapsed % 50 == 0):
        return 3  # Sleep to maintain health and alertness

    # Optimize alertness with coffee only when slightly low
    if alertness < 0.5:
        return 1  # Drink coffee and work to boost alertness without over-dependence

    # Work if alertness and health levels are adequate
    if alertness >= 0.5:
        return 0  # Continue working with optimal conditions

    return 0  # Default to working


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)