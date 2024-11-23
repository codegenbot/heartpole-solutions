import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for tiredness or health concerns
    if alertness < 0.5 or hypertension > 0.55 or intoxication > 0.4 or time_since_slept >= 8:
        return 3  # Sleep is vital for recovery and productivity

    # Use coffee cautiously to boost alertness without increasing hypertension dangerously
    if alertness < 0.6 and hypertension < 0.5:
        return 1  # Use coffee to improve alertness safely

    # Beer rarely, if stress is significant but manage intoxication
    if 0.4 < hypertension <= 0.6 and intoxication < 0.2:
        return 2  # Opt for relaxation via beer under controlled conditions

    # Optimal conditions to work without stimulants
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Proceed with work

    return 0  # Default safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)