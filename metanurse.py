import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health issues
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # sleep if any serious health issues

    # If not serious, manage alertness and productivity
    if alertness < 0.3:
        return 3  # sleep to recover alertness

    if alertness < 0.5:
        return 1  # coffee if moderately alert and no severe conditions

    # If conditions are optimal
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # just work to maximize productivity

    # For a balance of productivity and well-being
    if work_done < 0.25 and alertness > 0.4:
        return 2  # beer to relax slightly and work

    return 0  # default to just working if everything else is optimal


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)