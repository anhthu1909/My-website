import pandas as pd
dt = pd.read_csv("dataset\play_tennis.csv")
print(dt)
#dt.Outlook[dt.Play Tennis=="Yes"]
#or
PlayYes = dt[dt["Play Tennis"] == "Yes"]
PlayYes.Outlook

dtOy = dt.Outlook[dt["Play Tennis"] == "Yes"]
P1_1 = dtOy.value_counts()


P1_1 = P1_1/dtOy.count()
print (P1_1)

dtOn = dt.Outlook[dt["Play Tennis"] == "No"]
P1_2 = dtOn.value_counts()/dtOn.count()
print (P1_2)

dtTy = dt.Temperature[dt["Play Tennis"] == "Yes"]
P2_1 = dtTy.value_counts()/dtTy.count()
print (P2_1)

dtTy = dt.Temperature[dt["Play Tennis"] == "No"]
P2_2 = dtTy.value_counts()/dtTy.count()
print (P2_2)

dtHy = dt.Humidity[dt["Play Tennis"] == "Yes"]
P3_1 = dtHy.value_counts()/dtHy.count()
print (P3_1)

dtHy = dt.Humidity[dt["Play Tennis"] == "No"]
P3_2 = dtHy.value_counts()/dtHy.count()
print (P3_2)

dtWy = dt.Wind[dt["Play Tennis"] == "Yes"]
P4_1 = dtWy.value_counts()/dtWy.count()
print (P4_1)

dtWy = dt.Wind[dt["Play Tennis"] == "No"]
P4_2 = dtWy.value_counts()/dtWy.count()
print (P4_2)

Play = dt["Play 
          Tennis"][dt["Play Tennis"] == "Yes"].value_counts()/dt["Play Tennis"].count()
print(Play)

P_Yes = P1_1["Rain"]*P2_1["Cool"]*P3_1["High"]*P4_1["Weak"]*Play["Yes"]
P_No = P1_2["Rain"]*P2_2["Cool"]*P3_2["High"]*P4_2["Weak"]*(1 - Play["Yes"])

print(P_Yes)
print(P_No)

PY = P_Yes/(P_Yes + P_No)
PN = P_No/(P_Yes + P_No)

print(PY)
print(PN)

print(dt["Play Tennis"][dt["Play Tennis"] == "Yes"])
