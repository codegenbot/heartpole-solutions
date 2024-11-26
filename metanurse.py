import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize rest highly if health indicators are concerning
    if hypertension > 0.05 or intoxication > 0.05:
        return 3
    
    # Ensure sleep is taken often enough to maintain minimal alertness drops
    if time_since_slept > 4.0:
        return 3

    # Use coffee if alertness is low, but hypertension is under control
    if alertness < 0.75 and hypertension <= 0.02:
        return 1

    # Avoid actions increasing intoxication if already at a balance
    if alertness >= 0.75 and intoxication <= 0.02:
        return 0

    # Default balance between relaxation and work when conditions allow
    if alertness >= 0.7 and intoxication > 0.02 and intoxication <= 0.04:
        return 2

    return 0  # Default to working when health parameters are within safe zones

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)