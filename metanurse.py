import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical conditions to address first
    if time_since_slept >= 8 or alertness < 0.4 or hypertension > 0.8:
        return 3  # Sleep

    # Prioritize combating low alertness while keeping health in check
    if alertness < 0.6 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Beer can help manage moderate hypertension if conditions allow
    if hypertension > 0.5 and intoxication < 0.3:
        return 2  # Drink beer and work

    # Optimal productivity conditions
    if alertness > 0.75 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    return 3  # Default to sleep if no other condition is met


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)