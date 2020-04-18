from flask import Flask

from web_service.routes.routes_manager import define_routes


def create_app():
    app = Flask('Your flask server')
    return app


def main():
    app = create_app()
    define_routes(app)

    flask_host = '0.0.0.0'
    flask_port = 3333
    app.run(host=flask_host, port=flask_port, threaded=False, debug=True)

if __name__ == '__main__':
    main()