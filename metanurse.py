import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Re-prioritize sleep based on stricter health checks
    if (
        alertness < 0.7
        or hypertension > 0.65
        or intoxication > 0.3
        or time_since_slept >= 5
    ):
        return 3  # Must sleep

    # Prioritize health-safe alertness
    if alertness >= 0.85 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work

    # Safely boost alertness with coffee
    if alertness <= 0.75 and hypertension <= 0.5:
        return 1  # Drink coffee and work

    # Avoid using beer as intoxication control is critical

    return 0  # Default to work without risk increase


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)