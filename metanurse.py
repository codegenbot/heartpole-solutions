import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.15 or intoxication >= 0.05:
        return 3  # Prioritize sleep if nearing health risk
    
    if time_since_slept > 6 or alertness <= 0.4:
        return 3  # Sleep if tired or alertness is critically low

    if time_elapsed > 12:
        return 3  # Rest after sustained work period
    
    if alertness < 0.5 and hypertension < 0.1:
        return 1  # Consider coffee boost for moderate alertness
    
    if alertness >= 0.8 and intoxication < 0.02:
        return 0  # Ideal conditions to just work
    return 0  # Default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)