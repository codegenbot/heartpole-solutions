import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical condition for sleep due to severe health risk
    if (
        alertness < 0.5
        or hypertension > 0.6
        or intoxication > 0.4
        or time_since_slept > 6
    ):
        return 3  # Sleep

    # Use coffee if it's necessary and feasible to boost productivity
    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Favorable condition for just working: high alertness, low health risk
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication <= 0.3:
        return 0  # Just work

    # Discourage beer, favor actionable comforts
    return 0  # Default to working under safe conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)