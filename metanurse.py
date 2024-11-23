import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Check health-first conditions: high hypertension or intoxication
    if hypertension > 0.2 or intoxication > 0.2:
        return 3  # Sleep to lower health risks
    
    # If sleep deprivation is an issue
    if time_since_slept > 8:
        return 3  # Sleep to recover

    # Improve alertness safely with coffee if needed
    if alertness < 0.4 and hypertension < 0.1 and intoxication < 0.1:
        return 1  # Coffee work combo

    # If alertness is moderate and hypertension is significantly low
    if alertness < 0.7:
        return 0  # Just work to maintain balance and progress

    # Use beer if productivity is very high and all other indicators are favorable
    if work_done > 10 and alertness > 0.5 and intoxication < 0.1:
        return 2  # For a minor risk-reward balance

    # Reassess default sleep for recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)