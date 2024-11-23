import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health states
    if hypertension > 0.25 or intoxication > 0.1 or time_since_slept > 7:
        return 3  # Sleep

    # Sleep if alertness is below a safer threshold
    if alertness < 0.6:
        return 3  # Sleep

    # Encourage sleep periodically for better health, balance time to rest
    if time_elapsed % 100 > 75 and time_since_slept >= 5:
        return 3  # Sleep

    # Use coffee judiciously to enhance alertness only under safe conditions
    if alertness < 0.8 and hypertension <= 0.12 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Restrict beer consumption to manage hypertension carefully
    if hypertension > 0.18 and intoxication < 0.01:
        return 2  # Drink beer and work

    # Default to work if all metrics are not indicating potential health issues
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)