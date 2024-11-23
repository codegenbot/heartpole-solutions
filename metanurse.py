import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Consider sleeping more conservatively
    if hypertension >= 0.25 or intoxication > 0.2 or time_since_slept > 6 or alertness < 0.3:
        return 3  # Sleep

    # Use coffee more aggressively if not hypertensive
    if alertness < 0.5 and hypertension < 0.2:
        return 1  # Drink coffee and work

    # Just work if conditions aren't critical, even if not perfect
    if alertness >= 0.6 and (hypertension < 0.15 or intoxication < 0.1):
        return 0  # Just work

    return 0  # Default to just work more often

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)