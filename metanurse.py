import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health issues should prompt immediate sleep
    if hypertension > 0.12 or intoxication > 0.08 or time_since_slept > 6:
        return 3  # sleep to address serious health risks

    # Alertness and moderate work conditions
    if alertness < 0.5:
        return 3  # sleep is needed when alertness is low

    if alertness < 0.7:
        if hypertension < 0.08:  # slightly stricter hypertension threshold
            return 1  # drink coffee when alertness is moderate and hypertension is low

    # Optimal conditions to work without external help
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.02:
        return 0  # work when all conditions are very good

    # Relaxation with beer only under controlled conditions
    if work_done < 0.3 and alertness > 0.6:
        if intoxication < 0.04:
            return 2  # beer to boost morale with clear health status

    return 0  # default to working with balanced conditions


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)