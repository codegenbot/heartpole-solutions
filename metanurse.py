import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health thresholds
    if hypertension > 0.05 or intoxication > 0.15:
        return 3  # Immediate sleep to reduce severe health risks

    # Consider sleep necessity based on extended wakefulness or low alertness
    if time_since_slept > 6 or alertness < 0.3:
        return 3  # Sleep to recover significant alertness

    # Use coffee tactfully at moderate alertness levels, but not excessively
    if alertness < 0.6 and (hypertension < 0.02 and intoxication < 0.1):
        return 1  # Coffee to maintain or slightly boost alertness

    # Proceed to work when alertness is sufficient and health indicators are within safe range
    if alertness >= 0.6 and intoxication < 0.05:
        return 0  # Work safely without stimulants

    return 0  # Default to working if other conditions aren't triggered

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)