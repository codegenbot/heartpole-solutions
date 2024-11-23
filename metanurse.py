import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on severe health risks or extended awakeness
    if hypertension > 0.40 or intoxication > 0.20 or time_since_slept > 12:
        return 3  # Sleep

    # Sleep if alertness is dangerously low and health is affected
    if alertness < 0.5:
        return 3  # Sleep

    # Consider drinking coffee to boost alertness when conditions are safe
    if 0.5 <= alertness < 0.7 and hypertension <= 0.20 and intoxication <= 0.10:
        return 1  # Drink coffee and work

    # Avoid using beer; focus on recovery through sleep or coffee
    # Default to working when health parameters are optimized
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)