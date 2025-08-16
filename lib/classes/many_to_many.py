class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # immutable: ignore reassignment
        pass

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # immutable: ignore reassignment
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # mutable, but only if valid
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value
        # ignore invalid values

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # mutable, but only if valid
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # ignore invalid values

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None
