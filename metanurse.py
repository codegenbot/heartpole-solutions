import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if in any significant risky condition
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 12:
        return 3  # Sleep in risky conditions

    # Just work if alertness is good, and health indicators are within low-risk
    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work when in best condition

    # Coffee can help boost productivity; only when moderately tired but not at risk
    if 0.5 <= alertness < 0.8 and hypertension < 0.7 and intoxication < 0.2:
        return 1  # Coffee and work to boost alertness

    # Avoid beer due to health concerns; fallback to sleep if decision proximity is needed
    return 3  # Default to sleep for health and safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)