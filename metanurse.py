import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.6 or time_since_slept >= 3:
        return 3  # Sleep more aggressively when needed
    if intoxication > 0.2 or hypertension >= 0.4:
        return 0  # Avoid coffee to manage intoxication and hypertension
    if alertness < 0.75 and hypertension < 0.3:
        return 1  # Use coffee where alertness needs boost with manageable hypertension
    if alertness > 0.85:
        return 0  # Optimal working condition
    return 0  # Default: work when conditions are moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)