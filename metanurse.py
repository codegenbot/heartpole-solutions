import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 6:
        return 3  # Sleep more aggressively
    if alertness < 0.4 and hypertension <= 0.2 and intoxication < 0.2:
        return 1  # Drink coffee only when very needed
    if alertness >= 0.6 and intoxication <= 0.1:
        return 0  # Just work if alert and sober
    if work_done > 20 and intoxication < 0.15:
        return 2  # Relax, but earlier if conditions favorable
    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)