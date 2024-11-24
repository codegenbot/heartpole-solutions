import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Basic health prevention
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 3.5:
        return 3  # Prioritize sleep

    # Coffee logic: use when alertness is moderate but safe
    if 0.5 <= alertness < 0.8 and hypertension <= 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Work when in optimal condition
    if alertness >= 0.8 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Just work

    # More conservative use of beer
    if 0.25 < intoxication < 0.35 and hypertension < 0.5:
        return 2  # Drink beer and work

    return 3  # Default to sleep

# Loop through input to process up to 1000 steps
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)