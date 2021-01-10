from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wikipedia

# Search the keyword in wikipedia
wiki = wikipedia.search('artificial inteligence')
# Specify the title of the Wikipedia page
wiki = wikipedia.page(wiki[0])
# Extract the plain text content of the page
text = wiki.content

stopwords=set(STOPWORDS)

wordcloud = WordCloud(background_color='white', colormap='winter', stopwords=stopwords).generate(text)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
