import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health is compromised or alertness is low
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.35 or time_since_slept > 8:
        return 3  # Sleep
    
    # Use coffee to boost alertness if mild stress and low intoxication
    if alertness < 0.65 and hypertension < 0.5 and intoxication <= 0.1:
        return 1  # Drink coffee and work
    
    # Base case for work without stimulants if alert and health parameters are stable
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # Use beer cautiously to manage hypertension if it doesn’t cause high intoxication
    if 0.1 < intoxication < 0.25 and hypertension > 0.5:
        return 2  # Drink beer and work

    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)