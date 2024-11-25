import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        time_since_slept > 6
        or alertness < 0.2
        or hypertension > 0.6
        or intoxication > 0.4
    ):
        return 3  # Sleep when any health indicator is critical
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Ideal condition to work
    if alertness < 0.5 and hypertension < 0.45 and intoxication < 0.3:
        return 1  # Use coffee prudently for boosting alertness
    if hypertension > 0.5:
        return 3  # Rest if stress is high
    return 0  # Default to working under manageable conditions


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)