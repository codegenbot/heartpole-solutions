import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep conditions need to be addressed first
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 7:
        return 3  # Sleep prioritization

    # If alertness needs a boost and there's room for slight hypertension increase
    if alertness < 0.6 and hypertension < 0.5:
        return 1  # Coffee as productivity enhancer

    # Beer only in balanced moderate stress cases
    if 0.4 < hypertension <= 0.5 and intoxication < 0.3:
        return 2  # Beer for stress management

    # Stable conditions for working
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Work is safe

    return 0  # Default safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)