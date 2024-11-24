import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping for urgent health needs
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # Sleep

    # Sleep to prevent health issues with extreme hypertension or intoxication
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep

    # Boost alertness with coffee if moderately low and safe
    if alertness < 0.6 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Consider beer when hypertension is moderate and safe intoxication
    if 0.5 < hypertension <= 0.7 and intoxication < 0.3:
        return 2  # Drink beer and work

    # Proceed with work under optimal conditions
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    return 3  # Default to sleeping safely


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)