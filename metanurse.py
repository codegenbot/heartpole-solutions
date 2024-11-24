import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if needed
    if time_since_slept > 7 or alertness < 0.5:
        return 3  # Sleep

    # Control hypertension and intoxication balance
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep to avoid health issues

    # Boost alertness with coffee if it's moderately low but safe
    if alertness < 0.7 and hypertension <= 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Only consider beer if hypertension is moderate and intoxication is very low
    if 0.5 < hypertension <= 0.6 and intoxication < 0.2:
        return 2  # Drink beer and work

    # Optimal working conditions
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    return 3  # Sleep as a safe fallback


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)