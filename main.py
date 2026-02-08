import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. טעינת נתונים ---
file_path = 'data/Bacteria_resistance_data.csv'
df = pd.read_csv(file_path)

# --- 2. פונקציות ניקוי ועיבוד ---
def standardize_bacteria(name):
    name = str(name).lower()
    if 'coli' in name: return 'Escherichia coli'
    if 'mirabilis' in name: return 'Proteus mirabilis'
    if 'pneumoniae' in name: return 'Klebsiella pneumoniae'
    return 'Other/Unknown'

def get_age(val):
    try: return float(str(val).split('/')[0])
    except: return None

# החלת הניקוי
df['Unified_Bacteria'] = df['Souches'].apply(standardize_bacteria)
df['Age'] = df['age/gender'].apply(get_age)

# --- 3. חישוב עמידות (MDR/XDR) ---
antibiotics = ['AMX/AMP', 'AMC', 'CZ', 'FOX', 'CTX/CRO', 'IPM', 'GEN', 'AN', 'CIP', 'colistine']
df['R_Count'] = (df[antibiotics] == 'R').sum(axis=1)

def define_risk(count):
    if count == 0: return 'Sensitive'
    if count <= 2: return 'Low Resistance'
    if count <= 5: return 'MDR (Multi-Drug Resistant)'
    return 'XDR (Extensively Resistant)'

df['Risk_Level'] = df['R_Count'].apply(define_risk)

# --- 4. יצירת הגרפים (מוצגים אחד אחרי השני) ---

# גרף 1: התפלגות חיידקים
plt.figure(figsize=(10, 5))
df['Unified_Bacteria'].value_counts().plot(kind='barh', color='teal')
plt.title('Bacterial Distribution')
plt.tight_layout()
plt.show()

# גרף 2: עוגת רמות סיכון
plt.figure(figsize=(8, 8))
df['Risk_Level'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Antibiotic Resistance Risk Levels')
plt.show()

# גרף 3: מפת חום (Correlation)
plt.figure(figsize=(10, 8))
df_num = df[antibiotics].apply(lambda x: x.map({'R': 1, 'S': 0}))
sns.heatmap(df_num.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Antibiotic Correlation Map')
plt.show()

# --- 5. הדפסת מסקנות סופיות ---
print("--- סיכום מחקר עמידות חיידקים ---")
print(f"סה\"כ דגימות שנותחו: {len(df)}")
print(f"החיידק הנפוץ ביותר: {df['Unified_Bacteria'].value_counts().idxmax()}")
print(f"אחוז חיידקים עמידים מאוד (MDR+XDR): {((df['R_Count'] >= 3).mean()*100):.1f}%")