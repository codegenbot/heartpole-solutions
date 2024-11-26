import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust health indicators to stricter limits
    if hypertension > 0.03 or intoxication > 0.08:
        return 3
    if time_since_slept > 5.5 + (time_elapsed / 200):  # Dynamic sleep necessity
        return 3

    # Be conservative with coffee and beer
    if alertness < 0.6 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    if alertness < 0.5 and intoxication < 0.04:
        return 2

    # Work is favored only with high alertness and low health risks
    if alertness >= 0.75 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    return 3  # Default to rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)