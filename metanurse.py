import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if severely sleep deprived or critical hypertension/intoxication
    if time_since_slept >= 6 or hypertension > 0.02 or intoxication > 0.15:
        return 3
    # Consider sleep if moderately sleep deprived or moderate health issues
    if time_since_slept >= 4 or hypertension > 0.01 or intoxication > 0.1:
        return 3
    # Use coffee cautiously to boost alertness without exceeding moderate time_since_slept threshold
    if alertness < 0.5 and time_since_slept < 4:
        return 1
    # Regular work if alertness and health parameters are optimal
    if 0.7 <= alertness and hypertension < 0.008 and intoxication < 0.05:
        return 0
    # Default action to cautiously proceed with just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)