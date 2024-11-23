import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Priority checks for serious health issues
    if hypertension > 0.6 or intoxication > 0.3:
        return 3  # Sleep if significant health issues exist
    # Encourage sleep when alertness is critically low or overly awake
    if alertness < 0.5 and time_since_slept >= 6:
        return 3  # Improve rest prioritization
    # Use coffee prudently
    if alertness < 0.6 and time_since_slept <= 8 and time_elapsed < 9:
        return 1  # Drink coffee and work in earlier hours
    # Encourage productivity with sufficient alertness
    if alertness >= 0.7 and work_done < 0.8:
        return 0  # Just work if alert and work is not enough
    # Long awake periods are handled
    if time_since_slept > 12:
        return 3  # Sleep after extended wake period
    return 0  # Default to just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)