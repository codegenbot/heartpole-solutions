import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Check severe hypertension and intoxication immediately:
    if hypertension > 0.05 or intoxication > 0.05:
        return 3  # Prioritize sleep to address severe issues immediately

    # Prioritize sleep if not slept for long or moderate health concerns:
    if time_since_slept > 5 or hypertension > 0.03 or intoxication > 0.03:
        return 3  # More aggressive in opting for sleep

    # Opt for coffee if alertness is below a balanced threshold and health allows:
    if alertness < 0.7 and hypertension < 0.025 and intoxication < 0.02:
        return 1

    # Work only if all health parameters are optimal:
    if alertness >= 0.75 and hypertension < 0.01 and intoxication < 0.01:
        return 0

    # Default action to sleep if no conditions for coffee or direct work are met:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)