import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if severe health issues
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep to recover from health issues
    
    # Opt to sleep if time awake is excessive or alertness drops too low
    if time_since_slept > 14 or alertness < 0.3:
        return 3
    
    # Use coffee earlier in the day with moderate alertness
    if alertness < 0.6 and time_elapsed < 10:
        return 1
    
    # Take a beer break if work is stalled but not in danger
    if intoxication <= 0.3 and work_done < 0.5 and time_elapsed < 12:
        return 2
    
    # Work if health metrics are good and there's productive capability
    if alertness >= 0.5 and hypertension <= 0.25 and intoxication <= 0.2 and work_done < 0.9:
        return 0
    
    # Prioritize rest in later hours if getting tired
    if alertness < 0.4 and time_elapsed > 12:
        return 3

    # Default action based on remaining alertness
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)