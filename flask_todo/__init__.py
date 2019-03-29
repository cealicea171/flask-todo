
from flask import Flask, request,  render_template
import time
import datetime


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_NAME='flasktodo',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

#########################################
    from . import db
    db.init_app(app)
    #EXAMPLE FROM BLOG.PY TUTORIAL
        #else:
        #    db = get_db()
        #    db.execute(
            #    'UPDATE post SET title = ?, body = ?'
            #    ' WHERE id = ?',
            #    (title, body, id)

            #db.commit()
            #return redirect(url_for('blog.index'))

#    return render_template ('blog/update.html', post=post)

    @app.route('/', methods=['POST','GET'])
    def index():
        if request.method == 'POST':
            task_id = request.form["id"]

            if task_id:
                con = db.get_db()
                cur = con.cursor()
                cur.execute("SELECT * FROM tasks;")
                tasks = cur.fetchall()
                #method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
                con.close()
                cur.close()
                

        return render_template('index.html')

#########################################

    @app.route('/create', methods=['GET', 'POST'])
    def create_task():


        if request.method == 'GET':
            return render_template('create.html')


        elif request.method == "POST":

            new_task = request.form["task"]


            if new_task:
                date = datetime.datetime.now()
                con = db.get_db()
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO tasks(task, created_at, completed) VALUES (%s, %s, %s);",
                    (new_task, date, False))

                con.commit()
                cur.close()


                if not new_task:
                    return 'Error'

#time stamp is fucking shit up so took out for the moment..
            #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            return render_template('create.html', date, task=task)




        return render_template('create.html')



    @app.route('/update', methods=['GET', 'POST'])
    def update_task():

        if request.method == 'POST':
            update = request.form['update']

            if not update:
                return 'Error'


        return render_template('update.html')

    return app
