import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical sleep condition
    if (
        alertness < 0.3
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 10
    ):
        return 3

    # Moderate sleep need
    if time_since_slept > 8:
        return 3

    # Balanced decision between caffeine, work, and beer
    if alertness < 0.7 and hypertension < 0.65 and intoxication < 0.25:
        return 1

    if alertness >= 0.7 and hypertension < 0.65 and intoxication < 0.2:
        return 0

    if 0.7 < hypertension < 0.75 and 0.3 <= intoxication < 0.35:
        return 2

    # Default safer option
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)