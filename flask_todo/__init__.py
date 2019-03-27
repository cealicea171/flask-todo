
from flask import Flask, request,  render_template
import time
import datetime



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

    @app.route('/task', methods=['POST', 'GET'])
    def create_task():

        if request.method == 'GET':
            return render_template('task.html', task=None)

        elif  request.method == 'POST':

            task = request.form['task']


            if not task:
                return 'Error'

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            return render_template('task.html', timestamp=timestamp, task=task)


        return render_template('task.html')

    @app.route('/update', methods=['GET', 'POST'])
    def update_task():

        if request.method == 'POST':
            task = request.form['task']

            if not task:
                return 'Error'


                return render_template('update.html')

    return app
