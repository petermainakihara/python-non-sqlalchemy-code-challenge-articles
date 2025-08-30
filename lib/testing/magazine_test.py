# lib/testing/magazine_test.py

import pytest
from classes.many_to_many import Author, Magazine, Article

class TestMagazine:

    def test_magazine_initialized_with_name_and_category(self):
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"
        assert magazine.category == "Fashion"

    def test_article_titles_returns_titles(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article1 = Article(author, magazine, "Fashion Tips")
        article2 = Article(author, magazine, "Tutu Trends")
        titles = magazine.article_titles()
        assert "Fashion Tips" in titles
        assert "Tutu Trends" in titles

    def test_contributors_returns_authors(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "Fashion Tips")
        contributors = magazine.contributors()
        assert author in contributors
