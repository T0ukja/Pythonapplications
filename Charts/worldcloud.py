from wordcloud import WordCloud
import matplotlib.pyplot as plt
from random_word import RandomWords
#pip install random-word
#pip install pyyaml

r=RandomWords()


text=("")
for x in range(1,15):
    text+=str(r.get_random_word())
    text+=str(" ")
    
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
