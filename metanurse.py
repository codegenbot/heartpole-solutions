import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if very low alertness or prolonged time since last sleep
    if alertness < 0.5 or time_since_slept > 10:
        return 3

    # Avoid work if intoxication or significant hypertension is present
    if intoxication >= 0.2 or hypertension >= 0.1:
        return 3

    # Use caffeine if alertness is between 0.5 and 0.75, and hypertension is under control
    if 0.5 <= alertness < 0.75 and hypertension < 0.05:
        return 1

    # Work if conditions are generally optimal
    if alertness >= 0.75:
        return 0

    # Use beer sparingly if alertness is critically low and not ready for sleep
    if alertness < 0.5 and time_since_slept < 8:
        return 2

    # Default to just work if no other criteria met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)