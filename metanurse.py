import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if any health indicator is critically off
    if (
        alertness < 0.6
        or hypertension >= 0.5
        or intoxication >= 0.3
        or time_since_slept >= 6
    ):
        return 3  # Must sleep

    # Prioritize sleep if alertness is decreasing and health risks are emerging
    if alertness < 0.7 or time_since_slept > 5:
        return 3

    # Work if all health indicators are optimal and alertness is high
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee to boost alertness if within safe hypertension and intoxication levels
    if alertness < 0.8 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Default to work if health is stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)