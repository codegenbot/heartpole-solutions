import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when alertness or intoxication indicates a health risk
    if (
        alertness < 0.4
        or hypertension >= 0.5
        or intoxication >= 0.4
        or time_since_slept >= 6
    ):
        return 3  # Must sleep

    # Prefer sleep if alertness is low and there is accumulating fatigue
    if alertness < 0.5 or time_since_slept > 5:
        return 3  # Prefer sleep

    # Use coffee if it substantially improves alertness with minimal hypertension risk
    if alertness < 0.6 and hypertension < 0.35 and intoxication < 0.25:
        return 1  # Drink coffee and work

    # Default just to work if all health factors are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)