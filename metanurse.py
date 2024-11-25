import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping with stricter conditions
    if (
        alertness < 0.6
        or hypertension > 0.05
        or intoxication > 0.03
        or time_since_slept >= 2.0
    ):
        return 3

    # Use coffee to boost alertness, control hypertension & intoxication
    if 0.6 <= alertness < 0.8 and hypertension < 0.04 and intoxication < 0.02:
        return 1

    # Safe working conditions with lower hypertension and intoxication limits
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # Be cautious with beer; limit its conditions strictly
    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.3:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)