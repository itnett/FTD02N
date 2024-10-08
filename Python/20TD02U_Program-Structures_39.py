python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True, nullable=False)
    done = db.Column(db.Boolean, default=False)

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    task = Task(content=request.json['content'])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

# Route to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    task.content = request.json['content']
    task.done = request.json['done']
    db.session.commit()
    return jsonify(task.to_dict())

# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task.query.filter_by(id=task_id).delete()
    db.session.commit()
    return '', 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)