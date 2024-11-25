import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep for serious health or exhaustion concerns
    if hypertension > 0.1 or intoxication > 0.1 or time_since_slept > 5:
        return 3  # earlier intervention with sleep

    # Manage low alertness with quick boosts
    if alertness < 0.3:
        if hypertension <= 0.1:
            return 1  # use coffee if it's safe
        return 3

    # Optimal working conditions
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.03:
        return 0  # work if conditions are perfect

    # Use beer to relax without over-intoxication
    if work_done < 0.3 and alertness > 0.6 and intoxication < 0.1:
        return 2  # use beer moderately to relax and work

    # Default to just working when conditions moderate
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)