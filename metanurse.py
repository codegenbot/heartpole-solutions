import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust thresholds for hypertensive risk and intoxication
    if hypertension > 0.1 or intoxication > 0.3:
        return 3  # Sleep to combat high health risks

    # Re-evaluate necessity for sleep
    if time_since_slept >= 8 or alertness < 0.3:
        return 3  # Sleep for recovery and optimal productivity

    # Optimize alertness with coffee
    if alertness < 0.6:
        return 1  # Drink coffee and work to heighten alertness

    # Optimized working condition
    if alertness >= 0.6:
        return 0  # Proceed with work as conditions are favorable

    return 0  # Default to working as productive baseline


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)