import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if any health indicator is dangerously off
    if (
        alertness < 0.4
        or hypertension >= 0.5
        or intoxication >= 0.3
        or time_since_slept >= 6
    ):
        return 3  # Must sleep

    # Prioritize sleep if consumption patterns become risky
    if alertness < 0.5 or time_since_slept >= 5:
        return 3  # Prefer sleep

    # Use coffee only if alertness is moderately low and no health risk
    if alertness < 0.6 and hypertension < 0.35 and intoxication < 0.15 and time_since_slept < 5:
        return 1  # Drink coffee and work

    # Very limited scenarios to drink beer chiefly to enhance creativity or keep alert when slightly low
    if intoxication < 0.2 and alertness < 0.6 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Work if all health indicators are optimal and alertness is good
    if alertness >= 0.6 and hypertension < 0.25 and intoxication < 0.1:
        return 0  # Just work

    # Default to work if health is stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)