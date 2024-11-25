import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for any health risk
    if hypertension > 0.01 or intoxication > 0.015:
        return 3

    # Sleep if alertness too low or time_since_slept exceeds limit
    if alertness < 0.7 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is moderately low and health indicators are fine
    if 0.7 <= alertness < 0.85 and hypertension < 0.01 and intoxication < 0.01:
        return 1

    # Avoid beer unless workload is low, intoxication is minimal, and it's been a while
    if intoxication < 0.005 and time_elapsed > 20 and work_done < 3:
        return 2

    # Just work if alertness is high
    if alertness >= 0.85:
        return 0

    # Default to just work if no other conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)