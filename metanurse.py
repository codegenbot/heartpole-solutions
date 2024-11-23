import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep more aggressively based on tighter conditions
    if hypertension >= 0.25 or intoxication > 0.2 or time_since_slept > 4 or alertness < 0.35:
        return 3  # Sleep

    # Use coffee cautiously to prevent hypertension increase
    if alertness < 0.4 and hypertension < 0.15:
        return 1  # Drink coffee and work

    # Just work if conditions are generally acceptable
    if alertness >= 0.6 and (hypertension < 0.2 or intoxication < 0.15):
        return 0  # Just work

    return 0  # Default to just work with slightly relaxed criteria

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)