import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

//

df = pd.read_csv("/content/emails.csv")   # change filename if needed
df.head()


//

selected_features = ['the', 'you', 'and', 'free', 'credit', 'offer']

X = df[selected_features]
y = df['Prediction']

//

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

//

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)


//


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred_knn = knn.predict(X_test_scaled)


//

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

svm = SVC(kernel='linear', probability=True)
svm.fit(X_train_scaled, y_train)


//


evaluate("KNN", y_test, y_pred_knn)
evaluate("SVM", y_test, y_pred_svm)
def evaluate(model_name, y_true, y_pred):
    print(f"\n===== {model_name} =====")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))



//✅ Best advice ⭐ YES — you can enter random numbers ⭐ Keep them between 0 and 20 ⭐ Use more non-zero values → model predicts SPAM ⭐ Use mostly zeros → model predicts NOT SPAM



print("\nEnter values for the following 6 features:\n")

input_data = {}

for col in selected_features:
    val = float(input(f"Enter value for '{col}': "))
    input_data[col] = val

new_df = pd.DataFrame([input_data])
new_scaled = scaler.transform(new_df)

pred_knn = knn.predict(new_scaled)[0]
pred_svm = svm.predict(new_scaled)[0]

label_knn = "SPAM" if pred_knn == 1 else "NOT SPAM"
label_svm = "SPAM" if pred_svm == 1 else "NOT SPAM"

print("\n========== RESULT ==========")
print(f"KNN Prediction : {label_knn}")
print(f"SVM Prediction : {label_svm}")
print("=================================\n")