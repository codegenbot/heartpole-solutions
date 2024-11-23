import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if any critical health threshold is met
    if hypertension > 0.3:
        return 3  # Sleep to reduce hypertension
    if intoxication > 0.3:
        return 3  # Sleep to recover from intoxication
    if time_since_slept > 7:
        return 3  # Ensure regular sleep cycle to prevent long-term fatigue

    # Consider coffee only if below alertness threshold and low risk
    if alertness < 0.6 and hypertension <= 0.1:
        return 1  # Drink coffee to boost alertness if risk is low

    # Avoid further intoxication if levels are noticeable
    if intoxication > 0.2:
        return 3  # Sleep, avoid intoxicating further

    # Optimize work when conditions are favorable
    if alertness >= 0.7 and intoxication <= 0.1:
        return 0  # Proceed with work

    # Default fallback: if none of the critical actions are triggered, maintain health
    return 3 if alertness < 0.5 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)