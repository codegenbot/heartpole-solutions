import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep more actively for sustainable health
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep

    # Healthy optimal working condition
    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.1:
        return 0  # Just work

    # Coffee if alertness is slightly below optimal but avoid if hypertension is high
    if 0.6 <= alertness <= 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 1  # Coffee and work

    # Avoid beer unless specifically targeting mild relaxation with given limits on intoxication
    if 0.4 <= alertness < 0.6 and hypertension < 0.5 and intoxication <= 0.2:
        return 2  # Beer and work
    
    # Default to safeguarding health by sleeping
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)