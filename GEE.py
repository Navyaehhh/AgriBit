import ee
ee.Initialize(project="agribit-499813")   # Replace with your GCP project ID if needed
print("Connected to Earth Engine!")
startDate = ee.Date('2024-06-01')
endDate   = ee.Date('2025-10-01')
stepDays  = 15
