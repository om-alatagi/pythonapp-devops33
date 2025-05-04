from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        print("inside home function")
        return 'bye1234567890heyeyeyeyeyeyeGFG-33123123'

    @app.route('/test')
    def test():
        return 'Hi Sudhanshu test'
    @app.route('/test1')
    def test():
        return 'Hi Sudhanshu test1'
    @app.route('/test2')
    def test():
        x=10
        return 'Hi Sudhanshu test2'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
