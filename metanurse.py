import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to critical health metrics
    if hypertension > 0.15 or intoxication > 0.15:
        return 3  # sleep to tackle serious issues

    # Prioritize sleep if time without sleep is excessively high
    if time_since_slept > 7:
        return 3

    # Sleep if alertness is critically low
    if alertness < 0.5:
        return 3

    # Use coffee strategically to boost alertness without health compromise
    if alertness < 0.7 and hypertension < 0.1:
        return 1

    # Opt for relaxation with beer only if health metrics are stable
    if work_done < 0.5 and intoxication < 0.08 and hypertension < 0.1:
        return 2

    # Work routinely if productive conditions are met
    if alertness >= 0.8 and hypertension < 0.09 and intoxication < 0.05:
        return 0

    # Default to working if no other condition is pressing
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)