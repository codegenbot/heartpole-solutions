import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high hypertension or intoxication
    if hypertension > 0.6 or intoxication > 0.3:
        return 3
    
    # Sleep if alertness is low or much time has passed since last sleep
    if alertness < 0.5 or time_since_slept > 16:
        return 3

    # Use coffee to boost alertness during early hours
    if alertness < 0.7 and (time_elapsed < 10 or work_done < 0.4):
        return 1
    
    # Sleep during late hours if alertness is dropping
    if time_elapsed >= 14 and alertness < 0.6:
        return 3

    # With optimal alertness and low health risks, just work
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 0

    # Default to sleep if alertness is below threshold
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)