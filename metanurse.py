import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health and adequate rest.
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 16:
        return 3  # Sleep to mitigate severe health issues
    
    # Work normally when health and alertness are adequate.
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work
    
    # Use coffee if alertness is low but other metrics are stable.
    if 0.4 <= alertness < 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Coffee and work
    
    # Fallback to sleep to ensure no negative impact.
    return 3  # Default to sleep 

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)