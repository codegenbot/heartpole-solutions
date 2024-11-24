import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health issues are detected or if alertness is low
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee to boost work under safe conditions
    if 0.5 <= alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work
    
    # Work if alertness is good and health risks are minimal
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Enable beer usage only if it helps with productivity without adverse health effects
    if 0.6 <= alertness < 0.7 and intoxication < 0.3 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)