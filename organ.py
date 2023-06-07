import csv
from pydoc import describe

import pandas as pd

# making dataframe
from Tools.scripts.dutree import display

df = pd.read_csv("test_rock.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

datar = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


dr = pd.DataFrame(datar, index=['Rock'])


#print(df)

# print(df)

# output the dataframe


df = pd.read_csv("test_jazz.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

dataj = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


dj = pd.DataFrame(dataj, index=['Jazz'])




df = pd.read_csv("test_pop.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

datap = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


dp = pd.DataFrame(datap, index=['Pop'])




df = pd.read_csv("test_country.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

datac = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


dc = pd.DataFrame(datac, index=['Country'])




df = pd.read_csv("test_classic.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

datacl = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


dcl = pd.DataFrame(datacl, index=['Classical'])




df = pd.read_csv("test_rep_rock.csv")

x = df[df[['six_three']] != 0]
t = x.mean()
six_three = t['six_three']

x = df[df[['six_zero']] != 0]
t = x.mean()
six_zero = t['six_zero']

x = df[df[['three_zero']] != 0]
t = x.mean()
three_zero = t['three_zero']

x = df[df[['six_nine']] != 0]
t = x.mean()
six_nine = t['six_nine']

x = df[df[['three_nine']] != 0]
t = x.mean()
three_nine = t['three_nine']

x = df[df[['zero_nine']] != 0]
t = x.mean()
zero_nine = t['zero_nine']

# count occurrences a particular column
occur = df.groupby(['pick_1']).size()
occur2 = df.groupby(['pick_2']).size()
gold = df.groupby(['gold_pick']).size()

if 'three' in gold:
        gThree = gold['three']
else:
        gThree = 0
if 'nine' in gold:
        gNine = gold['nine']
else:
        gNine = 0
if 'six' in gold:
        gSix = gold['six']
else:
        gSix = 0
if 'zero' in gold:
        gZero = gold['zero']
else:
        gZero = 0


if 'three' in occur:
        three = occur['three']
else:
        three = 0
if 'three' in occur2:
        three2 = occur2['three']
else:
        three2 = 0

if 'six' in occur:
        six = occur['six']
else:
        six = 0
if 'six' in occur2:
        six2 = occur2['six']
else:
        six2 = 0

if 'nine' in occur:
        nine = occur['nine']
else:
        nine = 0
if 'nine' in occur2:
        nine2 = occur2['nine']
else:
        nine2 = 0

if 'zero' in occur:
        zero = occur['zero']
else:
        zero = 0
if 'zero' in occur2:
        zero2 = occur2['zero']
else:
        zero2 = 0

snine = nine + nine2
sSix = six + six2
sthree = three + three2
szero = zero + zero2

datarep = {
        'silver_nine': [snine],
        'silver_six': [sSix],
        'silver_three': [sthree],
        'silver_zero': [szero],
        'gold_nine': [gNine],
        'gold_six': [gSix],
        'gold_three': [gThree],
        'gold_zero': [gZero],
        'six_three': [six_three],
        'six_zero': [six_zero],
        'six_nine': [six_nine],
        'three_zero': [three_zero],
        'three_nine': [three_nine],
        'zero_nine': [zero_nine],
       }


drep = pd.DataFrame(datarep, index=['Country rep'])


df = pd.read_csv("test_stats.csv")
#print(df[0])
datarep = {
        'Knew song': ["no", 'no', 'yes', 'no', 'yes']
}



frames = [dr, dj, dp, dc, dcl]

#df = pd.DataFrame(frames)

#frames['Knew_song'] = datarep

#df.insert(5, "Knew song", ['no', 'no', 'yes', 'no', 'yes'], True)

repeat = [dc, drep]
res = pd.concat(repeat)

result = pd.concat(frames)
result.insert(0, "Knew song", ['no', 'no', 'yes', 'no', 'no'], True)
result.insert(15, "Volume", ['-14', '-14', '-14', '-14', '-14'], True)
#result['Knew_song'] = datarep
#df = pd.DataFrame(result)

print(result)
result.to_csv('file3.csv')
res.to_csv('fil
