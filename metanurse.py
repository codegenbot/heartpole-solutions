import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping in cases of very low alertness or high sleep deprivation
    if alertness < 0.4 or time_since_slept > 7:
        return 3  # sleep

    # Use coffee sparingly when alertness is moderately low and hypertension is safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.05:
        return 1  # drink coffee

    # Optimal state for working without stimulants
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 0  # just work

    # Avoid beer; reserve it only if no significant work done and intoxication minimal
    if work_done < 0.1 and intoxication <= 0.03:
        return 2  # drink beer

    # Default to work if conditions are not critical
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)