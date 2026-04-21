import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

print("Program Started")

# Load dataset
data = pd.read_csv("phishing.csv", header=None)
data.columns = ["url", "label"]

# Convert label (bad=1, good=0)
data['label'] = data['label'].map({'bad': 1, 'good': 0})

# Convert URL text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['url'])

# Target
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Test prediction
test_url = ["example.com/login"]
test_data = vectorizer.transform(test_url)

prediction = model.predict(test_data)

if prediction[0] == 1:
    print("Phishing Website Detected")
else:
    print("Safe Website")