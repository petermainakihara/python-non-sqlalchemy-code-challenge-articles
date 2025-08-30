# lib/testing/article_test.py

import pytest
from classes.many_to_many import Author, Magazine, Article

class TestArticle:

    def test_article_initialized_with_title(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.title == "How to wear a tutu with style"
        assert article.author == author
        assert article.magazine == magazine

    def test_title_is_immutable_str(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        # Expect AttributeError when trying to assign to title
        with pytest.raises(AttributeError):
            article_1.title = 500

    def test_articles_linked_to_author_and_magazine(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "Fashion Tips")
        assert article in author.articles()
        assert article in magazine.articles()
