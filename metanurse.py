import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if alertness/health metrics are significantly off
    if alertness < 0.5 or hypertension > 0.12 or intoxication > 0.08 or time_since_slept > 8:
        return 3
    
    # Use coffee when alertness is low, avoiding high hypertension and intoxication
    if alertness >= 0.5 and alertness < 0.7 and hypertension <= 0.1 and intoxication <= 0.03:
        return 1
    
    # Allow normal work when alertness is sufficient and health stats are good
    if alertness >= 0.7 and hypertension <= 0.08 and intoxication <= 0.02:
        return 0
    
    # Rarely use beer as a strategic choice if work_done is too low and no urgent health warnings
    if work_done < 0.2 and alertness >= 0.6 and hypertension < 0.09 and intoxication < 0.02:
        return 2

    # Default to work if alertness is not concerning
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)