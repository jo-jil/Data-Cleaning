import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("file1.csv")
print(df)

one = df['silver_nine'].sum()
two = df['silver_six'].sum()
three = df['silver_three'].sum()
four = df['silver_zero'].sum()

gone = df['gold_nine'].sum()
gtwo = df['gold_six'].sum()
gthree = df['gold_three'].sum()
gfour = df['gold_zero'].sum()

data = {'silver_nine': [one],
        'silver_six': [two],
        'silver_three': [three],
        'silver_zero': [four],
        'gold_nine': [gone],
        'gold_six': [gtwo],
        'gold_three': [gthree],
        'gold_zero': [gfour]
        }

# Creates pandas DataFrame.
evie_pick = pd.DataFrame(data, index=['Evie'])
print(df)
print(df["silver_nine"].plot(kind='hist'))
evie_pick.to_csv('file.csv')
