import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.6
        or hypertension > 0.06
        or intoxication > 0.04
        or time_since_slept >= 3.0
    ):
        return 3  # Sleep to recover

    if 0.6 <= alertness < 0.8 and hypertension < 0.05 and intoxication < 0.03:
        return 1  # Use coffee to boost alertness if needed

    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.02:
        return 0  # Safest condition to just work

    if work_done < 0.05 and intoxication <= 0.02 and alertness < 0.4:
        return 2

    return 0  # Default action to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)