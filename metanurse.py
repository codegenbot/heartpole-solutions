import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enhanced priority for sleep to prevent health degradation
    if (
        alertness < 0.65
        or time_since_slept >= 4
        or intoxication > 0.04
        or hypertension > 0.06
    ):
        return 3  # Sleep to recover effectively

    # Drink coffee judiciously to manage alertness
    if alertness < 0.75 and hypertension < 0.03 and time_since_slept < 3:
        return 1  # Use coffee sparingly

    # Beer is even more restrictive due to its potential impact
    if alertness > 0.90 and intoxication < 0.015 and hypertension < 0.004:
        return 2  # Beer is a reward under optimal conditions

    return 0  # Default action remains work under stable conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)