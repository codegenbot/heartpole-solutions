import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for health critical states, be more cautious here
    if hypertension > 0.25 or intoxication > 0.08 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep when alertness is too low
    if alertness < 0.7:
        return 3  # Sleep

    # Limit coffee usage if hypertension is slightly elevated
    if 0.7 <= alertness < 0.8 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # It's safer to just work when health indicators are optimal
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)