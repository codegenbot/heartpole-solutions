import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if necessary, considering health indicators conservatively
    if (
        alertness < 0.6
        or time_since_slept >= 5
        or intoxication > 0.05
        or hypertension > 0.07
    ):
        return 3  # Sleep to recover

    # Drink coffee if alertness is moderate, ensuring safety for blood pressure
    if alertness < 0.7 and hypertension < 0.04:
        return 1  # Coffee to boost alertness safely

    # Drink beer only when health indicators are very good
    if alertness > 0.85 and intoxication < 0.02 and hypertension < 0.005:
        return 2  # Reward with beer in optimal conditions

    return 0  # Default to work if conditions are stable


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)