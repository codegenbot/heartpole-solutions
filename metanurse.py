import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for increased hypertension or intoxication
    if hypertension >= 0.1 or intoxication >= 0.06:
        return 3  # Sleep

    # Avoid coffee if it's been too long since last sleep
    if alertness < 0.5 or time_since_slept >= 6:
        return 3  # Sleep
    
    # Use coffee sparingly, considering health stats and time_since_slept
    if alertness < 0.75 and hypertension < 0.08 and intoxication < 0.03 and time_since_slept < 5:
        return 1  # Drink coffee and work

    # Default to working if conditions are optimal, maintaining productivity
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)