import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when necessary
    if time_since_slept >= 6 or alertness < 0.5 or hypertension > 0.05 or intoxication > 0.07:
        return 3

    # If alertness is low, but hypertension is manageable, try coffee
    if alertness < 0.7 and hypertension < 0.03:
        return 1

    # Drink beer only if it can improve productivity safely
    if alertness >= 0.8 and intoxication < 0.03:
        return 2

    # Otherwise, just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)