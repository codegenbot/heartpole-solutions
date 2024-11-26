import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are unfavorable
    if (
        alertness < 0.6
        or hypertension > 0.06
        or intoxication > 0.03
        or time_since_slept >= 2.0
    ):
        return 3
    # Use coffee judiciously if conditions are acceptable, providing a moderate boost
    if 0.6 <= alertness < 0.8 and hypertension < 0.05 and intoxication < 0.02:
        return 1
    # Default to just working when alert and health indicators are stable
    if alertness >= 0.75 and hypertension < 0.03 and intoxication < 0.01:
        return 0
    # Fallback action to minimize risks
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)