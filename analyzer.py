def analyze_water(record):

    score = 0
    problems = []
    
    ph = float(record["pH"])
    if 6.5 <= ph <= 8.5:
        score += 1
    else:
        problems.append("pH")

    tds = float(record["tds"])
    if tds <= 500:
        score += 1
    else:
        problems.append("TDS")

    turbidity = float(record["turbidity"])
    if turbidity <= 5:
        score += 1
    else:
        problems.append("Turbidity")

    hardness = float(record["hardness"])
    if hardness <= 300:
        score += 1
    else:
        problems.append("Hardness")
        
    nitrate = float(record["nitrate"])
    if nitrate <= 45:
        score += 1
    else:
        problems.append("Nitrate")

    sulphate = float(record["sulphate"])
    if sulphate <= 200:
        score += 1
    else:
        problems.append("Sulphate")

    chlorine = float(record["chlorine"])
    if chlorine <= 1:
        score += 1
    else:
        problems.append("Chlorine")
        
    temperature = float(record["temperature"])
    if temperature <= 35:
        score += 1
    else:
        problems.append("Temperature")
        
    quality_score = (score / 8) * 100
    if quality_score >= 90:
        status = "Good"
    elif quality_score >= 60:
        status = "Needs Attention"
    else:
        status = "Poor"
    return quality_score, status, problems

