import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to prevent exhaustion and health issues
    if (
        alertness < 0.4
        or hypertension > 0.1
        or intoxication > 0.08
        or time_since_slept >= 4
    ):
        return 3

    # Use coffee cautiously, enhancing when alertness is moderate but health indicators are stable
    if 0.4 <= alertness < 0.6 and hypertension < 0.04 and intoxication < 0.04:
        return 1

    # Work if alertness and health are optimal
    if alertness >= 0.6 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)