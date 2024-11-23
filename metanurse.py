import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep conditions: strengthen to maintain health
    if alertness < 0.6 or hypertension > 0.55 or intoxication > 0.35 or time_since_slept >= 5:
        return 3  # Prioritize sleep sooner to prevent severe health effects

    # Use coffee wisely to manage moderate alertness drops
    if alertness < 0.65 and hypertension < 0.5:
        return 1  # Use coffee moderately when alertness slightly down

    # Beer condition for reducing stress, but cautiously
    if hypertension > 0.5 and intoxication < 0.25:
        return 2  # Beer only if stress-reduction is critical and intoxication allows

    # Optimal working conditions without any further boosts required
    if alertness >= 0.65 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Prime condition to work effectively

    return 0  # Default to work if specific conditions aren't met
    
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)