import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health over productivity when conditions are concerning
    if (
        alertness < 0.4  # Slightly increase the alertness threshold for sleep
        or hypertension > 0.07  # Lower threshold for hypertension to prioritize health
        or intoxication > 0.05  # Adjust intoxication threshold accordingly
        or time_since_slept >= 3.5  # Encourage more frequent sleep
    ):
        return 3

    # Allow coffee with slightly relaxed conditions
    if 0.4 <= alertness < 0.6 and hypertension < 0.05 and intoxication < 0.04:
        return 1
    
    # Work if safe, under appropriate conditions
    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.03:
        return 0

    # Default to work under safe conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)