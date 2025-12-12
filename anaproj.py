import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

#데이터 로드/전처리
df = pd.read_csv('StudentPerformanceFactors.csv')
df = df.dropna()

numeric_df = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Student Performance Factors')
plt.tight_layout()
plt.savefig('advanced_graph1_heatmap.png') 
plt.show()


df['Pass'] = df['Exam_Score'].apply(lambda x: 1 if x >= 65 else 0)

le = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

X = df.drop(['Exam_Score', 'Pass'], axis=1)
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

results = {}
print("\n[모델 성능 비교 결과]")
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    results[name] = acc
    print(f"{name}: {acc:.4f}")


plt.figure(figsize=(8, 5))
sns.barplot(x=list(results.keys()), y=list(results.values()), palette='viridis')
plt.title('Model Accuracy Comparison')
plt.ylim(0.8, 1.0) 
plt.ylabel('Accuracy')
plt.savefig('advanced_graph2_model_compare.png')
plt.show()


best_model = models["Gradient Boosting"]
importances = best_model.feature_importances_
feature_names = X.columns


feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False).head(10) # 상위 10개만


plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_imp_df, palette='magma')
plt.title('Top 10 Key Factors Influencing Exam Score')
plt.tight_layout()
plt.savefig('advanced_graph3_feature_importance.png') 
plt.show()