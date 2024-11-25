import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Encourage sleep sooner for better recovery
    if (
        alertness < 0.35
        or hypertension > 0.10
        or intoxication > 0.08
        or time_since_slept >= 4
    ):
        return 3

    # Allow coffee for a wider range of alertness
    if 0.35 <= alertness < 0.6 and hypertension < 0.05 and intoxication < 0.04:
        return 1

    # Continue work under broader conditions
    if alertness >= 0.6 and hypertension < 0.06 and intoxication < 0.06:
        return 0

    # Default to work if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)