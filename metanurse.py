import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if health is critical
    if hypertension > 0.65 or intoxication > 0.45:
        return 3

    # Sleep if very fatigued or alertness too low
    if time_since_slept > 14 or alertness < 0.35:
        return 3

    # Use coffee early if it can boost alertness without hypertension risk
    if alertness < 0.5 and hypertension < 0.4 and time_elapsed <= 12:
        return 1

    # Work if alert and not all work is done
    if alertness >= 0.5 and work_done < 0.95:
        return 0

    # Default to sleeping for rest when conditions aren't met
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)