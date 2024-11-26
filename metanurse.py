import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust the corresponding thresholds for better performance
    
    # Sleep if alertness is critical or health issues are imminent
    if (
        alertness < 0.5
        or hypertension > 0.06
        or intoxication > 0.05
        or time_since_slept >= 3.0
    ):
        return 3

    # Drink coffee if alertness is moderately decreasing, yet safe
    if 0.5 <= alertness < 0.75 and hypertension < 0.05 and intoxication < 0.04:
        return 1

    # Work optimally if all conditions are ideal for high productivity
    if alertness >= 0.75 and hypertension < 0.04 and intoxication < 0.03:
        return 0

    # Use beer only as a last resort if productivity is almost nil
    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.2:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)