import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious health issues
    if hypertension > 0.2 or intoxication > 0.2:
        return 3  # sleep to mitigate health risks
    
    # Sleep if alertness is low or haven't slept for too long
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # prioritize sleeping to restore alertness
    
    # Boost alertness if it's moderately low
    if 0.4 <= alertness < 0.7:
        return 1  # drink coffee to boost alertness

    # Balance productivity and relaxation when not in optimal conditions
    if work_done < 0.5 and alertness >= 0.5:
        return 2  # drink beer to relax and work

    # Optimal working conditions
    if alertness >= 0.7 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # just work in optimal conditions
    
    # Default to just work if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)