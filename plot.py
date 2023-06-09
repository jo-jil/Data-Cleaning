from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Complete.csv")
#dr = df.transpose()

#r = df.iloc[0].to_numpy()
#print(r)
#df = r.transpose()
print(df)

#marks = np.array([20, 13, 7, 0, 18, 2, 0, 0])



import matplotlib.pyplot as plt

data = {
    'silver_nine': [6, 20, 13, 2, 15, 13, 7],
    'silver_six': [9, 13, 16, 13, 15, 14, 12],
    'silver_three': [12, 7, 6, 14, 6, 7, 10],
    'silver_zero': [13, 0, 5, 11, 4, 6, 11],
    'gold_nine': [2, 18, 8, 0, 13, 7, 4],
    'gold_six': [4, 2, 7, 5, 6, 8, 6],
    'gold_three': [2, 0, 3, 9, 1, 2, 7],
    'gold_zero': [12, 0, 2, 6, 0, 3, 3]
}
colors = list(data.keys())
occurrences = [sum(data[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Everyones picks combined')
plt.show()


data = {
    'Nine': [128],
    'Six': [130],
    'Three': [86],
    'Zero': [76]
}
colors = list(data.keys())
occurrences = [sum(data[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Everyones pick Totals')
plt.show()

Daniela = {
    'silver_nine': [6],
    'silver_six': [9],
    'silver_three': [12],
    'silver_zero': [13],
    'gold_nine': [2],
    'gold_six': [4],
    'gold_three': [2],
    'gold_zero': [12]
}
colors = list(Daniela.keys())
occurrences = [sum(Daniela[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Daniela')
plt.show()
DanielaT = {
    'Nine': [8],
    'Six': [13],
    'Three': [14],
    'Zero': [25]
}
colors = list(DanielaT.keys())
occurrences = [sum(DanielaT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Daniela Totals')
plt.show()


Dave = {
    'silver_nine': [20],
    'silver_six': [13],
    'silver_three': [7],
    'silver_zero': [0],
    'gold_nine': [18],
    'gold_six': [2],
    'gold_three': [0],
    'gold_zero': [0]
}
colors = list(Dave.keys())
occurrences = [sum(Dave[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Dave')
plt.show()

DaveT = {
    'Nine': [38],
    'Six': [15],
    'Three': [7],
    'Zero': [0],

}
colors = list(DaveT.keys())
occurrences = [sum(DaveT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Dave totals')
plt.show()


Evie = {
    'silver_nine': [13],
    'silver_six': [16],
    'silver_three': [6],
    'silver_zero': [5],
    'gold_nine': [8],
    'gold_six': [7],
    'gold_three': [3],
    'gold_zero': [2]
}
colors = list(Evie.keys())
occurrences = [sum(Evie[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Evie')
plt.show()

EvieT = {
    'Nine': [21],
    'Six': [23],
    'Three': [9],
    'Zero': [7],
}
colors = list(EvieT.keys())
occurrences = [sum(EvieT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Evie Totals')
plt.show()


Kylie = {
    'silver_nine': [2],
    'silver_six': [13],
    'silver_three': [14],
    'silver_zero': [11],
    'gold_nine': [0],
    'gold_six': [5],
    'gold_three': [9],
    'gold_zero': [6]
}
colors = list(Kylie.keys())
occurrences = [sum(Kylie[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Kylie')
plt.show()

KylieT = {
    'Nine': [2],
    'Six': [18],
    'Three': [23],
    'Zero': [17]
}
colors = list(KylieT.keys())
occurrences = [sum(KylieT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Kylie Totals')
plt.show()


Laurel = {
    'silver_nine': [15],
    'silver_six': [15],
    'silver_three': [6],
    'silver_zero': [4],
    'gold_nine': [13],
    'gold_six': [6],
    'gold_three': [1],
    'gold_zero': [0]
}
colors = list(Laurel.keys())
occurrences = [sum(Laurel[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Laurel')
plt.show()

LaurelT = {
    'Nine': [28],
    'Six': [21],
    'Three': [7],
    'Zero': [4]
}
colors = list(LaurelT.keys())
occurrences = [sum(LaurelT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Laurel Totals')
plt.show()


dan = {
    'silver_nine': [13],
    'silver_six': [14],
    'silver_three': [7],
    'silver_zero': [6],
    'gold_nine': [7],
    'gold_six': [8],
    'gold_three': [2],
    'gold_zero': [3]
}
colors = list(dan.keys())
occurrences = [sum(dan[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Daniel')
plt.show()

danT = {
    'Nine': [20],
    'Six': [22],
    'Three': [9],
    'Zero': [9]
}
colors = list(danT.keys())
occurrences = [sum(danT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Daniel Totals')
plt.show()


danny = {
    'silver_nine': [7],
    'silver_six': [12],
    'silver_three': [10],
    'silver_zero': [11],
    'gold_nine': [4],
    'gold_six': [6],
    'gold_three': [7],
    'gold_zero': [3]
}
colors = list(danny.keys())
occurrences = [sum(danny[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Danny')
plt.show()

dannyT = {
    'Nine': [11],
    'Six': [18],
    'Three': [17],
    'Zero': [14]
}
colors = list(dannyT.keys())
occurrences = [sum(dannyT[color]) for color in colors]

plt.bar(colors, occurrences)
plt.xlabel('DB level')
plt.ylabel('Occurrences')
plt.title('Danny Totals')
plt.show()



df2 = pd.DataFrame(np.random.rand(10, 4), columns=["Dave", "Evie", "Kylie", "Daniela"])

#df2.plot.bar();
#df2.plot.bar(stacked=True);

labels = ["nine", "six", "three", "zero", "nine", "six", "three", "zero"]
labels_np = np.array(labels)
#df.hist()

emo = df.hist(column='Dave', ec='white', bins=range(8))
plt.grid(False, axis='x')
plt.xticks(ticks=np.arange(.5, 8, 1), labels=labels_np)
#plt.show()

# Creating histogram
#fig, ax = plt.subplots(figsize=(10, 7))
#ax.hist(marks, bins=["nine", "six", "three", "zero", "nine", "six", "three", "zero"])
