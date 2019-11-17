#!backend/env/Scripts/python
from flask import Flask, abort, jsonify

"""rrm - roommate resource manager
    wersja do nauki, narazie bez bazy danych - dane na sztywno"""

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Zrob zakupy',
        'description': u'Mleko, Alko, Maslo, Chleb', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Wynies smieci',
        'description': u'serio wywal bo wali juz', 
        'done': False
    }
]


@app.route('/rrm/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/rrm/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
 

if __name__ == '__main__':
    app.run(debug = True)
