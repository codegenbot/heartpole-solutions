import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health checks
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep to recover from severe health risks
    
    # Moderate health risks
    if alertness < 0.3 or time_since_slept > 10:
        return 3  # Sleep to recover alertness or reduce sleep deprivation

    # Use coffee if productivity can be boosted safely
    if alertness < 0.5 and hypertension < 0.35 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Just work if health and alertness are in safe, productive ranges
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Default to sleep under uncertain conditions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)