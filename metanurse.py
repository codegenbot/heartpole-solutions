import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Must sleep if severe health risk or lacking sleep significantly
    if hypertension >= 0.6 or intoxication >= 0.4 or time_since_slept >= 5:
        return 3  # Must sleep

    # Work if highly alert and health risks minimal
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee if moderate alertness and low health risks
    if 0.5 <= alertness < 0.7 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Prefer sleep in all ambiguous cases or mild health risks
    return 3  # Sleep otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)