import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health metric is slightly elevated
    if hypertension > 0.1 or intoxication > 0.1:
        return 3

    # Prioritize sleeping if significantly sleep deprived
    if time_since_slept > 5:
        return 3

    # Prefer working if alert and health metrics are very low
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Use coffee only if alertness is low and no health risks present
    if alertness < 0.5 and hypertension < 0.05 and intoxication < 0.05:
        return 1
    
    # Default to working if none of the above conditions meet
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)