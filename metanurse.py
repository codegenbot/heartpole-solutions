import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.5
        or time_since_slept > 6
    ):
        return 3  # Sleep if any health indicator is critical

    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work if all health indicators are excellent

    if alertness >= 0.5 and alertness < 0.8 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Drink coffee and work if alertness is moderately low, and safe

    if intoxication < 0.2 and hypertension < 0.5:
        return 2  # Drink beer and work only if health is safe

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)