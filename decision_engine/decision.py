def get_action(incident, severity):
    
    if incident == "fire":
        if severity == "high":
            return "🚨 Evacuate immediately & call fire department"
        else:
            return "⚠️ Trigger fire alarm and inspect area"

    elif incident == "overheating":
        if severity == "high":
            return "🔥 Shut down system & inspect cooling urgently"
        else:
            return "⚙️ Check cooling system"

    elif incident == "intrusion":
        return "🔐 Alert security & activate surveillance"

    elif incident == "equipment_failure":
        if severity == "high":
            return "🛑 Stop machinery immediately"
        else:
            return "🔧 Schedule maintenance check"

    else:
        return "✅ System operating normally"
    print("Decision module loaded")
    
    