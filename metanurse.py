import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping more conservatively for better health management
    if alertness < 0.6 or time_since_slept > 6:
        return 3

    # Avoid caffeine if hypertension is even slightly elevated and alertness is low
    if hypertension >= 0.06:
        if alertness < 0.7:
            return 3
        return 0

    # Avoid work if intoxication is moderate
    if intoxication >= 0.08:
        return 3

    # Use coffee to boost productivity if alertness is moderate and hypertension is low
    if 0.6 <= alertness < 0.8 and hypertension < 0.04:
        return 1

    # High alertness means optional productivity work
    if alertness >= 0.8:
        return 0

    # Default to working without stimulants if no conditions necessitate otherwise
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)