import pandas as pd
import matplotlib.pyplot as plt

equipment_df = pd.read_csv('russia_losses_equipment.csv') 
corrections_df = pd.read_csv('russia_losses_equipment_correction.csv') 
personnel_df = pd.read_csv('russia_losses_personnel.csv') 

equipment_df = equipment_df.dropna().drop_duplicates()
corrections_df = corrections_df.dropna().drop_duplicates()
personnel_df = personnel_df.dropna().drop_duplicates()

equipment_df['date'] = pd.to_datetime(equipment_df['date'])
corrections_df['date'] = pd.to_datetime(corrections_df['date'])
personnel_df['date'] = pd.to_datetime(personnel_df['date'])

equipment_stats = equipment_df.describe()
corrections_stats = corrections_df.describe()
personnel_stats = personnel_df.describe()

print("Статистика втрат техніки:")
print(equipment_stats)

print("\nСтатистика корекцій втрат техніки:")
print(corrections_stats)

print("\nСтатистика втрат особового складу:")
print(personnel_stats)

equipment_grouped = equipment_df.groupby(equipment_df['date'].dt.year).agg({'tanks': 'sum', 'aircraft': 'sum', 'ships': 'sum'})
equipment_sorted = equipment_df.sort_values(by='tanks', ascending=False)

plt.figure(figsize=(10, 5))
plt.plot(equipment_df['date'], equipment_df['tanks'])
plt.xlabel('Дата')
plt.ylabel('Кількість втраченої техніки')
plt.title('Динаміка втрат танків')
plt.show()
