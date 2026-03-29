def get_action(incident):
    if incident == "fire":
        return "Evacuate immediately"
    elif incident == "overheating":
        return "Inspect cooling system"
    elif incident == "intrusion":
        return "Alert security"
    elif incident == "equipment_failure":
        return "Schedule maintenance"
    else:
        return "No action needed"