import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for severe health symptoms or extremely low alertness
    if hypertension >= 0.25 or intoxication >= 0.2 or time_since_slept >= 6 or alertness < 0.3:
        return 3  # Sleep

    # Carefully use coffee to boost alertness with controlled hypertension
    if alertness < 0.5 and hypertension < 0.2:
        return 1  # Drink coffee and work

    # Main working condition ensuring alertness and health parameters remain optimal
    if alertness >= 0.65 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    # Encourage rest if the alertness is above threshold but hypertension is rising
    if alertness < 0.6:
        return 3  # Sleep

    # Avoid beer unless in very low-intoxication setting culture(less risky)
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)