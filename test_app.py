import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Author, Article

editorToken = os.environ['EDITOR']
directorToken = os.environ['DIRECTOR']


class EMagazineTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_e_magazine_db"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_article = {
            "title": "How to Achieve Holistic Health and Fitness",
            "date": "2020-06-15",
            "category": "lifestyle",
            "content": """ Fortunately, our health and fitness routines are
            salvageable. To that end,
            I recently spoke with two wellness experts""",
            "author_id": 1}

        self.update_article = {"category": "Health"}

        self.search_term = {"searchTerm": "health"}

        self.new_author = {
            "name": "Jane Doe",
            "gender": "female",
            "email": "janedoe@gmail.com"}

        self.update_author = {"email": "alaamalhazmi@gmail.com"}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # """
    # Test get/home
    # success
    # """

    def test_home(self):
        res = self.client().get('/home')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Welcome! to our e-magazine api')

    # """
    # Test post/authors/
    # success
    # """
    def test_add_author(self):
        res = self.client().post(
            '/authors',
            json=self.new_author,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['author']))

    # """
    # Test post/authors/
    # failure
    # """
    def test_add_author_unauthorized(self):
        res = self.client().post(
            '/authors',
            json=self.new_author,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    # """
    # Test post/articles/
    # success
    # """
    def test_add_article(self):
        res = self.client().post(
            '/articles',
            json=self.new_article,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['article']))

    # """
    # Test post/articles/
    # success
    # """
    def test_Search_articles(self):
        res = self.client().post(
            '/articles',
            json=self.search_term,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['articles']))

    # """
    # Test post/articles/
    # failure
    # """
    def test_add_article_bad_request(self):
        res = self.client().post(
            '/articles',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')

    # """
    # Test get/authors
    # success
    # """
    def test_retrive_authors(self):
        res = self.client().get(
            '/authors',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['authors']))

    # """
    # Test get/authors
    # failure
    # """
    def test_retrive_authors_authorization_missing(self):
        res = self.client().get('/authors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # """
    # Test get/articles
    # success
    # """

    def test_retrive_articles(self):
        res = self.client().get(
            '/articles',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['articles']))

    # """
    # Test get/articles
    # failure
    # """
    def test_retrive_articles_authorization_missing(self):
        res = self.client().get('/articles')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # """
    # Test patch/authors/
    # success
    # """

    def test_update_authors(self):
        res = self.client().patch(
            '/authors/1',
            json=self.update_author,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['author']))

    # """
    # Test patch/authors/
    # failure
    # """
    def test_update_authors_authorization_missing(self):
        res = self.client().patch('/authors/1', json=self.update_author)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # """
    # Test patch/articles/
    # success
    # """

    def test_update_article(self):
        res = self.client().patch(
            '/articles/1',
            json=self.update_article,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['article']))

    # """
    # Test post/articles/
    # failure
    # """
    def test_update_article_authorization_missing(self):
        res = self.client().patch('/articles/1', json=self.update_article,
                                  headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # """
    # Test delete/authors/2
    # success
    # """

    def test_delete_author(self):
        res = self.client().delete(
            '/authors/2',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        author = Author.query.filter(Author.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)

    # """
    # Test delete/authors/100
    # failure
    # """
    def test_delete_author_not_exist(self):
        res = self.client().delete(
            '/authors/100',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(directorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')

    # """
    # Test delete/articles/2
    # success
    # """
    def test_delete_article(self):
        res = self.client().delete(
            '/articles/2',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        author = Article.query.filter(Article.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)

    # """
    # Test delete/authors/100
    # failure
    # """
    def test_delete_article_not_exist(self):
        res = self.client().delete(
            '/Article/100',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')

    # """
    # Test get/authors/author_id/articles
    # success
    # """
    def test_retrive_articles_by_authorID(self):
        res = self.client().get(
            '/authors/1/articles',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_articles'])

    # """
    # Test get/authors/author_id/articles
    # success
    # """
    def test_retrive_articles_by_authorID_not_found(self):
        res = self.client().get(
            '/authors/100/articles',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(editorToken)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
