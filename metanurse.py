import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health risks
    if hypertension > 0.03 or intoxication > 0.03:
        return 3

    # Need to rest
    if alertness < 0.5 or time_since_slept > 4:
        return 3

    # Moderate health concerns - balance work and alertness
    if 0.5 <= alertness < 0.7:
        if hypertension < 0.02:
            return 1
        else:
            return 0

    if 0.7 <= alertness < 0.9:
        return 0

    if alertness >= 0.9:
        return 0

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)