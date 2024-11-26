import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health safeguards
    if hypertension > 0.03 or intoxication > 0.1:
        return 3  # Immediate sleep to mitigate risks

    # Sleep strategy based on prolonged activity or moderate alertness decline
    if time_since_slept > 4 or alertness < 0.4:
        return 3  # Sleep for rest restoration
    
    # Use coffee sparingly at safe health levels
    if 0.4 <= alertness < 0.7 and (hypertension < 0.02 and intoxication < 0.05):
        return 1  # Coffee boost
    
    # Perform work when alertness satisfies sustainability with minimal risk
    if alertness >= 0.7 and intoxication < 0.05:
        return 0  # Work securely with alertness maintained

    return 0  # Default to work if no specific action is triggered

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)