import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if health parameters are critically out of balance
    if (
        alertness <= 0.5
        or hypertension > 0.25
        or intoxication > 0.1
        or time_since_slept >= 10
    ):
        return 3  # Sleep to reset and maintain health

    # Moderate use of coffee to boost alertness safely, without risking hypertension
    if (
        alertness < 0.65
        and hypertension < 0.18
        and intoxication < 0.1
        and time_since_slept < 6
    ):
        return 1  # Drink coffee if it's safe enough to boost alertness

    # Work safely under optimal conditions
    if alertness >= 0.8 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0  # Just work if conditions are optimal for productivity

    # Use beer wisely without risking high intoxication levels, only if relaxed work is needed
    if (
        alertness > 0.75
        and intoxication <= 0.02
        and hypertension < 0.12
        and time_since_slept < 4
    ):
        return 2  # Drink beer as a stress relief measure when it's very safe

    return 0  # Default to working if no alterations are needed

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)