import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize critical sleeping when dangerous or tired
    if hypertension > 0.6 or intoxication > 0.5 or time_since_slept > 5:
        return 3  # Sleep

    # Consider sleeping if alertness is lower
    if alertness < 0.5:
        return 3  # Sleep

    # Optimal working conditions
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.25:
        return 0  # Just work

    # Boost productivity with coffee if alertness needs help and conditions allow
    if alertness < 0.8 and alertness >= 0.5 and hypertension < 0.5:
        return 1  # Drink coffee and work

    # Default to sleep if conditions are uncertain
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)