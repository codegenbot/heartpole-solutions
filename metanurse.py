import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if there's a significant health risk or severe sleep deprivation
    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 4:
        return 3  # Must sleep

    # Drink beer and work if intoxication level is manageable and we need slight relaxation
    if alertness < 0.4 and intoxication <= 0.2:
        return 2  # Drink beer and work

    # Work if highly alert and health risks are minimal
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee to boost productivity if under moderate alertness
    if 0.5 <= alertness < 0.7 and hypertension < 0.3:
        return 1  # Drink coffee and work

    # Default to sleeping if there's uncertainty or mild health risks
    return 3  # Sleep otherwise


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)