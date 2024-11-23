import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if health risk parameters exceed thresholds
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness is low
    if alertness < 0.7:
        return 3  # Sleep

    # Drink coffee if alertness moderately low with safe health parameters
    if 0.7 <= alertness < 0.9 and hypertension < 0.15 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Periodic rest every 150 steps to maximize long-term productivity
    if time_elapsed >= 150:
        return 3  # Sleep to recharge

    # Default to working if conditions are optimal
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)