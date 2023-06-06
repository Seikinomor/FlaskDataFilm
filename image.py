import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з файлу з правильним роздільником
data = pd.read_csv("film.csv", encoding='latin-1', delimiter=';')

# Обчислення кількості фільмів для кожного актора та актриси
actor_counts = data['Actor'].value_counts()
actress_counts = data['Actress'].value_counts()

# Об'єднання кількостей фільмів акторів та актрис у один DataFrame
actor_actress_counts = pd.concat([actor_counts, actress_counts], axis=1)
actor_actress_counts.columns = ['Actor', 'Actress']
actor_actress_counts = actor_actress_counts.fillna(0)

# Отримання топ-10 акторів та актрис за кількістю фільмів
top_actors = actor_actress_counts.nlargest(10, 'Actor')
top_actresses = actor_actress_counts.nlargest(10, 'Actress')

# Побудова графіка для акторів
plt.bar(top_actors.index, top_actors['Actor'])
plt.xlabel('Actor')
plt.ylabel('Number of Films')
plt.title('Top 10 Actors by Number of Films')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Побудова графіка для актрис
plt.bar(top_actresses.index, top_actresses['Actress'])
plt.xlabel('Actress')
plt.ylabel('Number of Films')
plt.title('Top 10 Actresses by Number of Films')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
