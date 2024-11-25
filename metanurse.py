import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or alertness < 0.3 or hypertension > 0.6:
        return 3  # Prioritize sleeping when overtired or highly stressed
    if intoxication > 0.3:
        return 3  # Sleep if intoxication level is high
    if alertness >= 0.7 and hypertension < 0.5 and intoxication == 0:
        return 0  # Work optimally when conditions are favorable
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Use coffee to boost alertness within safe limits
    if intoxication < 0.3 and 0.3 <= alertness < 0.7: 
        return 2  # Occasionally use beer to help relax
    return 0  # Default to working without stimulants in typical conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)