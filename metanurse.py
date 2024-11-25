import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If alertness is very low or too high of health risks, prioritize sleep
    if alertness < 0.25 or hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3
    
    # If alertness is low, drink coffee unless hypertension is high
    if alertness < 0.4 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1

    # If all parameters are within a healthy range, just work
    if alertness >= 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 0

    # If alertness is high and it's safe, consider a beer to reduce stress if work_done is low
    if alertness > 0.7 and hypertension < 0.1 and intoxication < 0.05 and work_done < 0.5:
        return 2

    # Default to working if no specific guidelines are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)