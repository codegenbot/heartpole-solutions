import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high hypertension or intoxication
    if hypertension > 0.5 or intoxication > 0.25:
        return 3
    
    # Sleep if alertness is very low or much time has passed since last sleep
    if alertness < 0.4 or time_since_slept > 18:
        return 3

    # Use coffee to boost alertness during early productive hours
    if alertness < 0.6 and (time_elapsed < 10 or work_done < 0.5):
        return 1
    
    # Sleep during late hours if alertness is dropping significantly
    if time_elapsed >= 14 and alertness < 0.5:
        return 3

    # With optimal alertness and manageable health risks, just work
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 0

    # Default to sleep if alertness or other conditions necessitate recuperation
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)