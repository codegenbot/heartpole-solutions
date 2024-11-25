import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize health indicators to avoid critical conditions
    if (
        alertness < 0.4
        or hypertension > 0.2
        or intoxication > 0.2
        or time_since_slept > 5
    ):
        return 3  # Sleep

    # If productivity is very high, prioritize lightweight tasks
    if work_done > 0.7:
        if alertness >= 0.5 and hypertension <= 0.1:
            return 0  # Just work

    # Boost alertness with coffee if it's safe
    if (
        alertness < 0.6
        and hypertension < 0.15
        and intoxication < 0.1
        and time_since_slept <= 5
    ):
        return 1  # Drink coffee and work

    # Consider beer if conditions are relaxed and work_done is low
    if (
        work_done < 0.4
        and alertness >= 0.5
        and hypertension < 0.15
        and intoxication < 0.1
    ):
        return 2  # Drink beer and work

    # Default to sleep to rejuvenate
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)