import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical condition: must sleep if any serious condition is noticed
    if hypertension >= 0.75 or intoxication >= 0.55:
        return 3  # Must sleep

    # Allow more time before immediate sleep if alertness is still maintainable
    if time_since_slept >= 8 or (hypertension >= 0.65 and time_since_slept >= 6):
        return 3  # Must sleep

    # Ideal work condition: high alertness and no health risks
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.25:
        return 0  # Just work

    # Use coffee to boost alertness if hypertension is manageable
    if 0.4 < alertness < 0.8 and hypertension < 0.5:
        return 1  # Drink coffee and work

    # Avoid using beer; prefer sleep or coffee
    return 3  # Prefer to sleep if not in optimal health or alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)