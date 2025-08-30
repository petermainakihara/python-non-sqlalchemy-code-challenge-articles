# lib/testing/author_test.py

import pytest
from classes.many_to_many import Author, Magazine, Article

class TestAuthor:

    def test_author_initialized_with_name(self):
        author = Author("Carry Bradshaw")
        assert author.name == "Carry Bradshaw"

    def test_name_is_immutable_string(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        # Expect AttributeError when trying to change name
        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_add_article_links_article(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "Fashion Tips")
        assert article in author.articles()
        assert article in magazine.articles()
