import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping for critical or high moderate conditions
    if (
        hypertension > 0.1
        or intoxication > 0.15
        or time_since_slept > 8
        or alertness < 0.3
    ):
        return 3  # urgent to moderate need for sleep

    # Use coffee to boost productivity unless health concerns are significant
    if 0.3 <= alertness < 0.7 and hypertension < 0.075:
        return 1  # coffee can aid focus without exacerbating hypertension

    # Optimal state for working
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 0  # ideal state, keep working

    # Avoid beer unless it's certain to not significantly detract from productivity
    if work_done < 0.15 and intoxication <= 0.05:
        return 2

    # Default action
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)