import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate sleep for long-term health, slightly relaxed conditions
    if hypertension > 0.35 or intoxication > 0.18 or time_since_slept > 7:
        return 3  # Sleep

    # Rest if alertness falls critically low
    if alertness < 0.55:
        return 3  # Sleep

    # Use coffee wisely with careful monitoring of health metrics
    if 0.55 <= alertness < 0.65 and hypertension <= 0.25 and intoxication <= 0.12:
        return 1  # Drink coffee and work

    # Avoid beer unless necessary
    if alertness < 0.6 and 0.12 < intoxication <= 0.15:
        return 2  # Drink beer and work

    # Default action when health is stable and safe
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)