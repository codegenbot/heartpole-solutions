import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if critical health issues are present
    if hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept >= 6:
        return 3

    # If significant work is yet to be done, focus more on productivity
    if work_done < time_elapsed * 0.6:
        if alertness < 0.5:
            return 1  # Drink coffee and work
        elif alertness < 0.3 and intoxication < 0.2:
            return 2  # Drink beer and work

    # Revise work criteria based on current alertness and health
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Default to sleep if no clear action is needed
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)