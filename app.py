import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Author, Article
from auth import AuthError, requires_auth
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        return response

    # ROUTES
    '''
        GET /home
    '''
    @app.route('/home')
    def hello():
        return jsonify({
            "message": "Welcome! to our e-magazine api"}), 200

    '''
        GET /authors
    '''
    @app.route('/authors')
    @requires_auth('get:authors')
    def retrieve_authors(payload):
        authors = Author.query.order_by(Author.id).all()
        formatedAuthors = [author.format() for author in authors]

        return jsonify({
            "success": True,
            "authors": formatedAuthors,
            'total_authorss': len(formatedAuthors)}), 200

    '''
        GET /articles
    '''
    @app.route('/articles')
    @requires_auth('get:articles')
    def retrieve_article(payload):
        articles = Article.query.order_by(Article.id).all()
        formatedArticles = [article.format() for article in articles]

        return jsonify({
            "success": True,
            "articles": formatedArticles,
            'total_authors': len(formatedArticles)}), 200

    '''
        POST /authors
    '''
    @app.route('/authors', methods=['POST'])
    @requires_auth('post:authors')
    def create_author(payload):

        body = request.get_json()

        if body is None:
            abort(400)

        try:
            new_author = Author(
                name=body.get('name'),
                gender=body.get('gender'),
                email=body.get('email'))
            new_author.insert()

            return jsonify({
                'success': True,
                'author': new_author.format()}), 200

        except Exception:
            abort(422)

    '''
        POST /articles
        searches for articles by searchTerm, if searchTerm post an article
    '''
    @app.route('/articles', methods=['POST'])
    @requires_auth('post:articles')
    def create_article(payload):

        body = request.get_json()

        if body is None:
            abort(400)

        if body.get('searchTerm'):
            articles = Article.query.order_by(
                Article.id).filter(
                Article.title.ilike(
                    '%{}%'.format(
                        body.get('searchTerm'))))
            search_results_formated = [article.format()
                                       for article in articles]

            if len(articles.all()) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'articles': search_results_formated,
                'total_articles': len(articles.all())}), 200

        try:
            new_article = Article(
                title=body.get('title'),
                date=body.get('date'),
                category=body.get('category'),
                content=body.get('content'),
                author_id=body.get('author_id'))
            new_article.insert()

            return jsonify({
                'success': True,
                'article': new_article.format()}), 200

        except Exception:
            abort(422)

    '''
        PATCH /authors/author_id
    '''
    @app.route('/authors/<int:author_id>', methods=['PATCH'])
    @requires_auth('patch:authors')
    def update_author(payload, author_id):

        # check author is present in the database
        author = Author.query.filter(Author.id == author_id).one_or_none()
        if author is None:
            abort(404)

        body = request.get_json()

        # make sure body is present
        if body is None:
            abort(400)

        if 'name' in body:
            author.name = body.get('name')
        if 'gender' in body:
            author.gender = body.get('gender')
        if 'email' in body:
            author.email = body.get('email')

        try:
            # Update author
            author.update()

            updated_author = Author.query.filter(
                Author.id == author_id).first()

            return jsonify({
                'success': True,
                'author': updated_author.format()}), 200

        except Exception:
            abort(422)

    '''
        PATCH /articles/artcile_id
    '''
    @app.route('/articles/<int:article_id>', methods=['PATCH'])
    @requires_auth('patch:articles')
    def update_article(payload, article_id):

        # check article is present in the database
        article = Article.query.filter(Article.id == article_id).one_or_none()
        if article is None:
            abort(404)

        body = request.get_json()

        # make body is present
        if body is None:
            abort(400)

        if 'title' in body:
            article.title = body.get('title')
        if 'date' in body:
            article.date = body.get('date')
        if 'category' in body:
            article.category = body.get('category')
        if 'content' in body:
            article.content = body.get('content')
        if 'author_id' in body:
            article.author_id = body.get('author_id')

        try:
            # Update article
            article.update()

            updated_article = Article.query.filter(
                Article.id == article_id).first()

            return jsonify({
                'success': True,
                'article': updated_article.format()}), 200

        except Exception:
            abort(422)

    '''
        DELET /authors/author_id
    '''
    @app.route('/authors/<int:author_id>', methods=['DELETE'])
    @requires_auth('delete:authors')
    def delete_author(payload, author_id):

        author = Author.query.filter(Author.id == author_id).one_or_none()

        if author is None:
            abort(404)

        try:
            author.delete()

            return jsonify({
                'success': True,
                'deleted': author_id}), 200

        except Exception:
            abort(422)

    '''
        DELET /articles/article_id
    '''
    @app.route('/articles/<int:article_id>', methods=['DELETE'])
    @requires_auth('delete:articles')
    def delete_article(payload, article_id):

        article = Article.query.filter(Article.id == article_id).one_or_none()

        if article is None:
            abort(404)

        try:
            article.delete()

            return jsonify({
                'success': True,
                'deleted': article_id}), 200

        except Exception:
            abort(422)

    '''
        GET /authors/author_id/articles
    '''
    @app.route('/authors/<author_id>/articles')
    @requires_auth('get:authors/<author_id>/articles')
    def retrive_articlesByauthorID(payload, author_id):
        current_author = Author.query.filter(
            Author.id == author_id).one_or_none()

        if current_author is None:
            abort(404)

        articles = Article.query.filter(Article.author_id == author_id).all()
        articles_formated = [article.format() for article in articles]

        if len(articles_formated) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'articles': articles_formated,
            'total_articles': len(articles_formated)}), 200

    # Error Handling

    '''
    error handler for AuthError

    '''
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    '''
    error handlers

    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
