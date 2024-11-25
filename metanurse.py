import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping with slightly adjusted thresholds
    if (
        alertness < 0.5
        or hypertension > 0.07
        or intoxication > 0.05
        or time_since_slept >= 2.5
    ):
        return 3

    # Use coffee more broadly to boost alertness and work efficiency
    if 0.5 <= alertness < 0.7 and hypertension < 0.05 and intoxication < 0.02:
        return 1

    # Keep working conditions safe and stable
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.01:
        return 0

    # Be very cautious with beer to avoid health issues
    if work_done < 0.02 and intoxication <= 0.01 and alertness < 0.3:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)