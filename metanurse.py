import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep conditions prioritizing recovery when severely compromised
    if (
        alertness < 0.2
        or hypertension > 0.8
        or intoxication > 0.7
        or time_since_slept > 10
    ):
        return 3  # Prioritize sleep for recovery in severe conditions

    # Coffee strategy for moderate alertness boost without risking hypertension
    if 0.2 <= alertness < 0.4 and hypertension < 0.1 and intoxication < 0.2:
        return 1  # Use coffee to boost alertness safely

    # Optimal conditions to work efficiently and safely
    if alertness >= 0.4 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Work in good condition

    # Beer for relaxation if mildly hypertension and needing to lower stress
    if hypertension >= 0.3 and intoxication < 0.5:
        return 2  # Beer to reduce hypertension-related stress

    # Default to work to maintain baseline productivity
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)