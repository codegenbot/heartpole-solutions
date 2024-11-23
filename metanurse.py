import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: sleep if any health indicator is critical
    if hypertension > 0.3 or intoxication > 0.2:
        return 3  # Sleep

    # Sleep if alertness is low
    if alertness < 0.7:
        return 3  # Sleep

    # Use coffee cautiously: moderate alert but safe health levels
    if 0.7 <= alertness < 0.85 and hypertension <= 0.2 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Encourage sleep if too much time has passed without rest
    if time_since_slept > 4:
        return 3  # Sleep

    # Default action: Just work
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)