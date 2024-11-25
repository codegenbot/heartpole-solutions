import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or intoxication > 0.15 or time_since_slept >= 5:
        return 3  # Prioritize sleep
    
    if alertness < 0.4 and hypertension < 0.05 and intoxication < 0.05:
        return 1  # Use coffee to boost alertness safely

    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.03:
        return 0  # Continue working efficiently

    if work_done < 0.5 and intoxication < 0.05 and alertness < 0.6:
        return 2  # Consider beer for moderate productivity boost

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)