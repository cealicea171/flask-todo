
from flask import Flask, request,  render_template
#import time
#import datetime



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

    @app.route('/create', methods=['POST', 'GET'])
    def create_task():


        if request.method == 'GET':
            return render_template('create.html')


        elif request.method == "POST":

            add_item = request.form["text"]

            if add_item:
                print("Create New Task: ", add_item)

            if not add_item:
                return 'Cannot Add Task'

#time stamp is fucking shit up so took out for the moment..
            #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            ##return render_template('create.html', timestamp=timestamp)




        return render_template('create.html')



    @app.route('/update', methods=['GET', 'POST'])
    def update_task():

        if request.method == 'POST':
            update = request.form['update']

            if not update:
                return 'Error'


        return render_template('update.html')

    return app
