import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when health risks are conservative
    if hypertension >= 0.15 or intoxication >= 0.1:
        return 3  # Sleep

    # Sleep management with reduced threshold
    if time_since_slept >= 6 or alertness < 0.4:
        return 3  # Sleep

    # Adjust coffee condition for conservative alertness
    if alertness < 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Strict condition for default work
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Just work

    # Default to sleep in uncertain situations
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)