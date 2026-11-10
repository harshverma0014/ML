import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Sample Bank Loan Dataset (from console output)
data = {
    'Income': [25000, 30000, 75000, 80000, 45000, 60000, 20000, 90000, 35000, 85000],
    'CreditScore': [550, 600, 750, 800, 650, 710, 500, 820, 580, 790],
    'LoanAmount': [200000, 250000, 300000, 400000, 150000, 280000, 100000, 350000, 180000, 320000],
    'Experience': [1, 2, 8, 10, 4, 6, 1, 12, 3, 9],
    'LoanStatus': ['Reject', 'Reject', 'Approve', 'Approve', 'Reject', 'Approve', 'Reject', 'Approve', 'Reject', 'Approve']
}

df = pd.DataFrame(data)

print("Bank Loan Dataset:")
print(df.head(2))
print()

# Split features and target
X = df[['Income', 'CreditScore', 'LoanAmount', 'Experience']]
y = df['LoanStatus']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train Random Forest Classifier
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Display Actual vs Predicted Results
print("\nActual Results:")
print(y_test.tolist())

print("\nPredicted Results:")
print(y_pred.tolist())

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Predict for a new customer
new_customer = pd.DataFrame({
    'Income': [75000],
    'CreditScore': [820],
    'LoanAmount': [300000],
    'Experience': [8]
})

new_pred = model.predict(new_customer)
print("\nNew Customer Loan Status:", new_pred[0])