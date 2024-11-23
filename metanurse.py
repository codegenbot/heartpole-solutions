import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep conditions to ensure balanced health and productivity
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.6
        or time_since_slept > 9
    ):
        return 3  # Sleep as a recovery mechanism under more relaxed conditions

    # Use coffee for alertness when health is stable
    if 0.3 <= alertness < 0.5 and hypertension < 0.2 and intoxication < 0.1 and time_since_slept <= 5:
        return 1  # Safe coffee boost without health risks

    # Work under optimal conditions where health isn't at risk
    if alertness >= 0.5 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Efficient work in healthy state

    # Limit beer usage, prioritize relaxation only if hypertension persists
    if 0.3 <= hypertension < 0.5 and intoxication < 0.4 and time_since_slept <= 6:
        return 2  # Use beer judiciously for mild hypertension

    # Default work approach to maintain productivity when health isn't critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)