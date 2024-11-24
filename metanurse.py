import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if alertness is very low or intoxication/hypertension are too high
    if alertness <= 0.3 or hypertension >= 0.7 or intoxication >= 0.7 or time_since_slept > 10:
        return 3  # Must sleep to recover

    # If alertness is good and health parameters are fine, focus on maximizing work
    if alertness >= 0.8 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Just work

    # If alertness is moderate, consider caffeine unless health metrics are worrying
    if alertness < 0.8 and hypertension < 0.5 and intoxication < 0.5:
        return 1  # Drink coffee and work

    # Use beer option prudently when awareness is dropping but intoxication allows it
    if alertness < 0.6 and intoxication < 0.3:
        return 2  # Drink beer and work

    return 3  # Default to rest by sleeping if any concerns

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)