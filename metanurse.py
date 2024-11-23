import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep when alertness is low or the user is significantly compromised
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.6
        or time_since_slept > 8
    ):
        return 3  # Prioritize sleep for recovery

    # Coffee for boosting alertness but careful with hypertension
    if 0.3 <= alertness < 0.5 and hypertension < 0.15 and intoxication < 0.15:
        return 1  # Drink coffee and work for safe alertness boost

    # Safe working conditions
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.25:
        return 0  # Work efficiently

    # Beer to manage moderate hypertension
    if hypertension >= 0.4 and intoxication < 0.4:
        return 2  # Drink beer to relax

    # Default fallback to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)