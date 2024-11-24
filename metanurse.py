import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is low, or other risk factors are high
    if (
        alertness < 0.5
        or hypertension > 0.4
        or intoxication > 0.25
        or time_since_slept >= 4
    ):
        return 3  # Sleep

    # Use coffee if slightly low alertness and health limits are manageable
    if 0.5 <= alertness < 0.65 and hypertension <= 0.35 and intoxication < 0.2:
        return 1  # Coffee and work

    # Just work when health conditions are optimal
    if alertness >= 0.65 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work

    # Use beer if alertness is in mid range and statuses allow relaxation
    if 0.5 <= alertness < 0.55 and intoxication <= 0.1 and hypertension <= 0.35:
        return 2  # Drink beer and work

    # Default to working if conditions allow for productivity
    return 0  # Just work if uncertain


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)