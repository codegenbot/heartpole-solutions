import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        time_since_slept > 5
        or hypertension > 0.32
        or intoxication > 0.08
        or alertness < 0.6
    ):
        return 3  # Prioritize sleep to prevent health issues
    if alertness < 0.75 and hypertension < 0.2 and time_since_slept < 4:
        return 1  # Limited use of coffee ensuring safe boundaries
    return 0  # Default to work for productivity


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)