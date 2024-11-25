import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health is at risk or alertness requires it
    if hypertension > 0.3 or intoxication > 0.2 or alertness < 0.5 or time_since_slept > 6:
        return 3
    
    # If alertness is low but within a safe hypertension and intoxication level, consider drinking coffee
    if alertness < 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    
    # If not intoxicated and health looks good with moderate alertness, consider drinking beer
    if alertness >= 0.7 and hypertension < 0.2 and intoxication <= 0.05 and work_done < 0.5:
        return 2
    
    # Default to working if health metrics and alertness are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)