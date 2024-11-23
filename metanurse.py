import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if serious health risks are detected
    if hypertension > 0.25 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # Sleep

    # Use coffee to boost alertness while managing hypertension
    if 0.4 <= alertness < 0.7 and hypertension <= 0.2 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # High alertness and low intoxication yields work focus
    if alertness >= 0.65 and intoxication <= 0.1:
        return 0  # Just work

    # Use beer when alertness is very low to ease into work
    if alertness < 0.4 and intoxication < 0.15:
        return 2  # Drink beer and work

    # Default to sleep if none of the above conditions apply
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)