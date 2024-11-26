import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to prevent severe fatigue
    if alertness < 0.6 or time_since_slept > 7.0:
        return 3
    
    # Avoid severe health risks due to high hypertension or intoxication
    if hypertension > 0.07 or intoxication > 0.07:
        return 3
    
    # Assess the need for coffee to boost alertness when moderately awake
    if 0.6 <= alertness < 0.8 and hypertension <= 0.04:
        return 1

    # Default to working when health is stable and alertness is sufficient
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)