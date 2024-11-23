import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical alertness or health issues
    if alertness < 0.3 or hypertension > 0.5 or intoxication > 0.4 or time_since_slept > 14:
        return 3

    # Sleep if awake time is relatively high
    if time_since_slept > 12 and alertness < 0.6:
        return 3
    
    # Use coffee carefully to boost alertness when safe
    if alertness < 0.6 and hypertension <= 0.25 and intoxication <= 0.2:
        return 1

    # Use beer even more selectively with very stable conditions
    if alertness >= 0.5 and intoxication <= 0.05 and hypertension <= 0.15 and work_done < 0.7:
        return 2

    # Default to work if health is stable and alertness is adequate
    return 0 if alertness >= 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)