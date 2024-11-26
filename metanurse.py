import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for any health red flags
    if hypertension > 0.01 or intoxication > 0.04:
        return 3  # sleep to recover from health threats

    # Sleep if significantly sleep-deprived or alertness is critically low
    if time_since_slept >= 3 or alertness < 0.5:
        return 3  # ensure rest and recovery

    # Utilize coffee when moderately tired and health indicators are at baseline levels
    if alertness < 0.65 and hypertension < 0.005 and intoxication < 0.02:
        return 1  # boost alertness with minimal risk

    # Default to working if all conditions are healthy
    return 0  # work continuously when in optimal health and alert

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)