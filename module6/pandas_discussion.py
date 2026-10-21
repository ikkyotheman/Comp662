import pandas as pd

movies = pd.DataFrame({
'name': ['Spirited Away', 'Lawrence of Arabia', 'Pulp Fiction'],
'minutes': [125, 216, 154]
})

print(movies)
print("Average length:", movies['minutes'].mean())