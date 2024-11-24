import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health thresholds must always take precedence
    if hypertension > 0.65 or intoxication > 0.35 or alertness < 0.4:
        return 3  # Immediate prioritization of sleep

    # Regular sleep to avoid severe health and alertness impacts
    if time_since_slept >= 6:
        return 3  # Regular rest to prevent chronic fatigue

    # Coffee is used only when absolutely necessary and within safe hypertension levels
    if alertness < 0.55 and hypertension <= 0.5:
        return 1  # Coffee helps boost alertness under safe conditions

    # Working is prioritized when all conditions are favorable
    if alertness >= 0.75 and hypertension <= 0.40 and intoxication <= 0.05:
        return 0  # Optimal conditions for maximum productivity

    # More restrained beer usage with emphasis on relaxation but caution
    if alertness >= 0.65 and hypertension < 0.50 and intoxication <= 0.15:
        return 2  # Safe and mildly relaxing beer option

    return 3  # Default fallback always returns to sleeping

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)