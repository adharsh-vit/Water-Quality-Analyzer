def calculate_statistics(records):

    if not records:
        print("\nNo records available.")
        return

    ph_values = []
    tds_values = []
    turbidity_values = []

    for record in records:
        ph_values.append(float(record["pH"]))
        tds_values.append(float(record["tds"]))
        turbidity_values.append(float(record["turbidity"]))

    print("\n")
    print("=" * 50)
    print("          WATER QUALITY STATISTICS")
    print("=" * 50)

    print("Total Records     :", len(records))

    print("\n--- pH ---")
    print("Average pH        :", round(sum(ph_values) / len(ph_values), 2))
    print("Highest pH        :", max(ph_values))
    print("Lowest pH         :", min(ph_values))

    print("\n--- TDS ---")
    print("Average TDS       :", round(sum(tds_values) / len(tds_values), 2), "mg/L")
    print("Highest TDS       :", max(tds_values), "mg/L")
    print("Lowest TDS        :", min(tds_values), "mg/L")

    print("\n--- Turbidity ---")
    print("Average Turbidity :", round(sum(turbidity_values) / len(turbidity_values), 2), "NTU")
    print("Highest Turbidity :", max(turbidity_values), "NTU")
    print("Lowest Turbidity  :", min(turbidity_values), "NTU")

    print("=" * 50)
