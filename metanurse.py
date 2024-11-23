import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 10:
        return 3  # Sleep if any health risk is significant

    if alertness < 0.5:
        return 1  # Drink coffee and work to boost alertness

    if intoxication > 0.2:
        return 2  # Drink beer to manage intoxication

    if alertness >= 0.6:
        return 0  # Keep working if alertness is reasonably high

    return 3  # Default: Sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)