import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health states
    if hypertension > 0.3 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep when alertness is concerning
    if alertness < 0.5:
        return 3  # Sleep

    # Encourage sleep cyclically as time progresses for balance
    if time_elapsed % 100 > 80 and time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee strategically to boost alertness without risking hypertension
    if alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Moderate beer use to lower hypertension, but only if intoxication is very low
    if hypertension > 0.2 and intoxication < 0.02:
        return 2  # Drink beer and work

    # Default to work if all metrics are safe
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)