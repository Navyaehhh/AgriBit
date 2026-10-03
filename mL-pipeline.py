import ee
import pandas as pd
ee.Initialize(project="agribit-499813")
data = ee.FeatureCollection("projects/agribit-499813/assets/Training_Data")
features = data.getInfo()["features"]
rows = []
for feature in features:
    rows.append(feature["properties"])
df = pd.DataFrame(rows)
df.to_csv("GEE/Training_Data.csv", index=False)
print("Training data updated.")