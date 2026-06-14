def get_alert(status):

    if status == "HAZARDOUS":
        return "🚨 AIR QUALITY DANGEROUS!"

    elif status == "POOR":
        return "🔴 Air Pollution High"

    elif status == "MODERATE":
        return "🟡 Air Quality Moderate"

    else:
        return "🟢 Air Quality Good"