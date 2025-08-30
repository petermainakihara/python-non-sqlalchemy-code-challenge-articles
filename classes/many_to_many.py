# classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from classes.many_to_many import Article
        article = Article(self, magazine, title)
        if article not in self._articles:
            self._articles.append(article)
        if article not in magazine.articles():
            magazine.articles().append(article)
        return article

    def topic_areas(self):
        mags = self.magazines()
        return list({mag.category for mag in mags}) if mags else []


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else []

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or []


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Title must be a non-empty string")

        self._author = author
        self._magazine = magazine
        self._title = title

        # Link article to author and magazine
        if self not in author.articles():
            author.articles().append(self)
        if self not in magazine.articles():
            magazine.articles().append(self)

    @property
    def title(self):
        return self._title  # immutable, no setter

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
