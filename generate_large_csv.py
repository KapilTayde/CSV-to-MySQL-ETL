import pandas as pd
import random
import faker

fake = faker.Faker()
data = []

for i in range(50000):  # Generating 50,000 rows
    data.append([i+1, fake.name(), random.randint(18, 60), fake.email()])

df = pd.DataFrame(data, columns=["id", "name", "age", "email"])
df.to_csv("large_data.csv", index=False)

print("✅ Large CSV file generated successfully!")
