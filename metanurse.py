import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High priority on health issues
    if hypertension > 0.3 or intoxication > 0.4 or time_since_slept > 12:
        return 3  # Critical need to sleep

    if time_since_slept > 8:
        return 3  # Regular sleep schedule

    if alertness < 0.5:
        # Different response based on alertness level
        if alertness < 0.3:
            return 3  # Lack of alertness suggests sleep
        else:
            return 1  # Coffee boost for moderate alertness drop

    # Conditions for drinking beer
    if intoxication < 0.2 and alertness > 0.6:
        return 2  # Opportunity to relax a bit without major drawbacks

    # Optimal work condition
    if alertness >= 0.65 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    return 0  # Default to just working if none of the above applies

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)