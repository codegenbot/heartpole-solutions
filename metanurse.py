import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping for critical conditions
    if hypertension > 0.15 or intoxication > 0.2 or time_since_slept > 10:
        return 3  # urgent need for sleep

    # Address moderate sleep needs or low alertness
    if time_since_slept > 6 or alertness < 0.3:
        return 3  # sleep needed when slightly fatigued

    # Use coffee if alertness is high with moderate hypertension
    if alertness >= 0.7 and 0.1 <= hypertension < 0.2:
        return 1  # use coffee to maintain productivity but watch for hypertension limits

    # Use coffee to boost moderate alertness and maintain productivity
    if 0.3 <= alertness < 0.7 and hypertension < 0.1:
        return 1  # coffee helps sustain alertness without raising hypertension

    # Optimal working conditions purely for productivity
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.1:
        return 0  # ideal state, keep working

    # Handle low work done cautiously
    if work_done < 0.2 and intoxication <= 0.1 and time_since_slept < 5 and alertness > 0.3:
        return 2  # lightly use beer when not much work is done, avoid high intoxication impact

    # Default to just working under moderate conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)