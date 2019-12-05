
import matplotlib.pyplot as plt

labels = ['Positif', 'Negatif']
sizes = ['411','589']
colors = ['blue', 'red']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


