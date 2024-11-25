import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping for critical conditions
    if hypertension > 0.15 or intoxication > 0.2 or time_since_slept > 10:
        return 3  # urgent need for sleep

    # Address moderate sleep needs or low alertness
    if time_since_slept > 6 or alertness < 0.3:
        return 3  # sleep needed when slightly fatigued

    # Use coffee to boost moderate alertness and maintain productivity
    if 0.3 <= alertness < 0.7 and hypertension < 0.1:
        return 1  # coffee can help sustain alertness without raising hypertension

    # Optimal working conditions purely for productivity
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.1:
        return 0  # ideal state, keep working

    # Relax slightly if productivity is very low
    if work_done < 0.2 and intoxication <= 0.1:
        return 2  # use beer lightly when not much work has been done
    
    # Default to just working when conditions are moderate
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)