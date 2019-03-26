from flask import Flask, request,  make_response, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

#########################################

    @app.route('/')
    def index():
        return render_template('index.html')

#########################################

    @app.route('/task', methods=['GET', 'POST'])
    def add_task():
        if request.method == 'POST':
            task = request.form['task']
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            return render_template('list.html', task=task, timestamp=timestamp)



    return app
