import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 12:
        return 3  # Sleep if health risks are higher
    
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # Sleep if tiredness is significant or alertness is very low
    
    if alertness < 0.6 and hypertension <= 0.12 and time_since_slept <= 8:
        return 1  # Drink coffee judiciously to boost productivity safely
    
    if intoxication < 0.05 and (0.4 < alertness < 0.7):
        return 2  # Occasionally use beer if it boosts focus without health risks

    if alertness >= 0.75 and hypertension < 0.1 and intoxication < 0.05 and time_elapsed < 900:
        return 0  # Work efficiently when all conditions are optimal
    
    return 0  # Default to working if conditions aren't clearly unsafe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)