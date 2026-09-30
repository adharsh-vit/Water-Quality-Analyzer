from analyzer import analyze_water

good_record = {"pH": "7.2","tds": "420","turbidity": "2.4","hardness": "180","nitrate": "15","sulphate": "100","chlorine": "0.5","temperature": "26"}
score, status, problems = analyze_water(good_record)
print("Test 1")
print("Score:", score)
print("Status:", status)
print("Problems:", problems)

poor_record = {"pH": "5.5","tds": "800","turbidity": "8","hardness": "400","nitrate": "60","sulphate": "250","chlorine": "2","temperature": "40"}
score, status, problems = analyze_water(poor_record)
print("\nTest 2")
print("Score:", score)
print("Status:", status)
print("Problems:", problems)
