import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health over productivity with refined thresholds
    if hypertension > 0.3 or intoxication > 0.15 or alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep for health if any critical threshold is crossed

    if intoxication < 0.05 and hypertension < 0.2 and alertness >= 0.8 and work_done < 0.4:
        return 2  # Drink beer if relax and leisure threshold under control
    
    if alertness < 0.65 and hypertension < 0.25:
        return 1  # Drink coffee to boost alertness
    
    return 0  # Default to just work if no urgent health indicators

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)