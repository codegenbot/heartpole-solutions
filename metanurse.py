import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep only if it's really needed
    if hypertension >= 0.8 or intoxication >= 0.6:
        return 3
    
    # Encourage sleep if sleepless or close to stressing out
    if time_since_slept >= 10 or (hypertension >= 0.7 and time_since_slept >= 7):
        return 3

    # Prefer working if in good condition
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0

    # Use coffee to boost productivity, especially when alertness drops.
    if 0.3 <= alertness < 0.7 and hypertension < 0.5:
        return 1

    return 2 if intoxication < 0.4 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)