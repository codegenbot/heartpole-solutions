import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3  # Sleep if alertness is low, hypertension or intoxication are high, or haven't slept recently

    if alertness >= 0.8 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work if all health indicators are optimal

    if alertness < 0.8 and alertness >= 0.5 and hypertension <= 0.6:
        return 1  # Drink coffee and work if alertness is moderate and hypertension is controlled

    if hypertension <= 0.5 and intoxication <= 0.2:
        return 2  # Drink beer and work only if alertness isn't optimal but other health indicators remain safe

    return 3  # Default to sleep if health conditions are uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)