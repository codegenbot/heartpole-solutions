import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when sleep is vastly overdue or alertness is very low
    if alertness < 0.6 or time_since_slept > 6.0:
        return 3
    
    # Avoid worsening health hazards
    if hypertension > 0.03 or intoxication > 0.03:
        return 3
    
    # Use coffee to mildly boost alertness, check for lower hypertension
    if 0.6 <= alertness < 0.8 and hypertension <= 0.02:
        return 1

    # Default to working without any boosters
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)