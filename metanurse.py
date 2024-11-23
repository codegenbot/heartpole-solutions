import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness or intoxication are poor
    if alertness < 0.3 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep is necessary

    # Prioritize health: avoid hypertension increase
    if hypertension > 0.6:
        return 3  # Sleep to recover from high stress levels

    # Use coffee when alertness is moderately low without high hypertension risk
    if 0.3 <= alertness < 0.5 and hypertension < 0.3:
        return 1  # Use coffee boost

    # Consider beer moderation if alertness is very high and not intoxicated
    if alertness > 0.7 and intoxication <= 0.2:
        return 2  # Temporary relief with beer if needed

    # Work in optimal conditions
    if alertness >= 0.5 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Work in balanced condition

    # Default to safe productivity measures
    return 0  # Default to work when conditions are alright

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)