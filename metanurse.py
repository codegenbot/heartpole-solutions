import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # If critical health factors are high, prioritize sleep
    if hypertension > 0.5 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Sleep to avoid severe health issues
    # Use coffee when alertness is low, provided it doesn't increase health risks
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.15:
        return 1  # Coffee to boost alertness safely
    # If the alertness is decent and health metrics are normal, just work
    if alertness > 0.6 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work
    # In mild intoxication, which might need relaxation
    if intoxication > 0.1:
        return 2  # Drink beer and work to moderate intoxication
    return 0  # Default to work if none above apply


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)