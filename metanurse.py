import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize Sleep for critical recovery needs
    if time_since_slept > 8 or alertness < 0.35 or hypertension > 0.65 or intoxication > 0.6:
        return 3  # Sleep

    # Use Coffee wisely to boost productivity, maintaining health
    if 0.35 <= alertness < 0.55 and hypertension <= 0.5 and intoxication < 0.4:
        return 1  # Drink coffee and work

    # Use Beer carefully to keep alertness in balance without overuse
    if 0.4 <= alertness < 0.55 and intoxication < 0.35 and hypertension < 0.4:
        return 2  # Drink beer and work

    # Safely encourage working when all health indicators are in good range
    if alertness >= 0.55 and hypertension < 0.4 and intoxication < 0.35:
        return 0  # Just work

    return 0  # Safe default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)