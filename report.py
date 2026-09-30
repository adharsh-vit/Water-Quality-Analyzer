
def generate_report(record, score, status, problems):

    print("\n")
    print("`" * 55)
    print("             WATER QUALITY REPORT")
    print("`" * 55)

    print("Record ID    :", record["id"])
    print("Location     :", record["location"])
    print("Date         :", record["date"])

    print("\nWater Parameters")
    print("-" * 55)

    print("pH :  ", record["pH"])
    print("TDS :", record["tds"], "mg/L")
    print("Turbidity :", record["turbidity"], "NTU")
    print("Hardness :", record["hardness"], "mg/L")
    print("Nitrate  :", record["nitrate"], "mg/L")
    print("Sulphate :", record["sulphate"], "mg/L")
    print("Chlorine :", record["chlorine"], "mg/L")
    print("Temperature :", record["temperature"], "°C")

    print("\nAnalysis")
    print("-" * 55)
    print("Quality Score :", round(score, 2), "/ 100")
    print("Overall Status:", status)

    if problems:
        print("\nParameters requiring attention:")
        for problem in problems:
            print("-", problem)
    else:
        print("\nAll analyzed parameters are within the reference limits.")

    print("\nRecommendation")
    print("-" * 55)

    if status == "Good":
        print("The analyzed parameters are within the reference limits.")
    elif status == "Needs Attention":
        print("Some parameters require attention. Further checking or treatment may be appropriate.")
    else:
        print("Several parameters are outside the reference limits. Further testing is recommended.")

    print("=" * 55)
