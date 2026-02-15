from newspaper import Article
url =" "

article = Article(url, memoize_aricles=False)
article.download()
article.parse()

article.publish_date
article.authors
artticle.title

article.text.replace("\n", " ")