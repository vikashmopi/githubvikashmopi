import pandas as pd
from sklearn.tree import DecisionTreeClassifier



music_data = pd.read_csv("music_preferences.csv")

print(music_data)
X= music_data.drop(columns=['genre'])

y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)

prediction = model.predict([[49,1]])

print(prediction)

