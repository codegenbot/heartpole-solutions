import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize severe conditions first
    if hypertension > 0.35 or intoxication > 0.25:
        return 3  # Sleep to reduce hypertension or intoxication

    if time_since_slept > 10 or alertness < 0.45:
        return 3  # Sleep due to lack of rest or low alertness

    # Use coffee cautiously to boost alertness if alertness is moderately low
    if alertness < 0.55 and hypertension < 0.25:
        return 1  # Drink coffee when safe for a mild alertness boost

    # Default to working under reasonable conditions
    if alertness >= 0.65 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0  # Work if all conditions are favorable

    # Default to the safest general action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)