import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep for serious health or exhaustion concerns
    if hypertension > 0.15 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # earlier intervention with sleep

    # Manage moderate alertness with quick boosts
    if alertness < 0.4:
        return 1  # use coffee to soon boost alertness

    # Optimal working conditions
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # work if conditions are perfect

    # Use beer for balance if work is insufficient
    if work_done < 0.3 and alertness > 0.5 and intoxication <= 0.15:
        return 2  # use beer moderately to relax and work

    # Default to just working when conditions moderate
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)