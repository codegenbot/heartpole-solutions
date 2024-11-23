import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for severe conditions or low alertness
    if hypertension >= 0.25 or intoxication >= 0.2 or time_since_slept >= 4 or alertness < 0.4:
        return 3  # Sleep

    # Use coffee cautiously to boost alertness without high hypertension
    if alertness < 0.5:
        return 1  # Drink coffee and work

    # Main working condition with manageable health parameters
    if hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    if alertness >= 0.6 and hypertension < 0.2:
        return 0  # Just work

    # Avoid beer unless in specific condition with very low intoxication
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)