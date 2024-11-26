import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Check for high-risk indicators that necessitate sleep:
    if hypertension > 0.05 or intoxication > 0.1:
        return 3
    if time_since_slept > 6:
        return 3

    # Boost alertness with coffee if safe and needed:
    if alertness < 0.7:
        if hypertension < 0.04 and intoxication < 0.05:
            return 1
        else:
            return 3

    # Drink beer only when intoxication is safe and alertness is moderate:
    if 0.6 <= alertness < 0.8 and hypertension < 0.03 and intoxication < 0.04:
        return 2

    # Safely work if health conditions are non-threatening:
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)