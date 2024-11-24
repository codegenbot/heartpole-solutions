import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical condition: prioritize sleep if any serious condition is noticed
    if hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept >= 6:
        return 3  # Must sleep

    # Ideal work condition: high alertness and no health risks
    if alertness >= 0.8 and hypertension <= 0.25 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee cautiously to boost alertness without risking health
    if 0.5 < alertness < 0.8 and hypertension < 0.35 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Avoid using beer; promote sleep otherwise
    return 3  # Prefer to sleep if not in optimal health or alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)