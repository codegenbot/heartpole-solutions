import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if alertness is critically low or health indicators signal high risk
    if (
        alertness < 0.5
        or hypertension >= 0.5
        or intoxication > 0.3
        or time_since_slept >= 5
    ):
        return 3  # Sleep

    # Drink coffee and work if alertness is sub-optimal, but health is stable
    if 0.5 <= alertness < 0.6 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Work if all parameters are within optimal bounds
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication <= 0.15:
        return 0  # Just work

    # If alertness is low and intoxication is very low, drink beer to relax and work if not at risk
    if alertness < 0.5 and hypertension <= 0.4 and intoxication <= 0.05:
        return 2  # Drink beer and work

    # Default to sleeping more if not entirely sure; focus more on health preservation
    return 3  # Sleep if uncertain


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)