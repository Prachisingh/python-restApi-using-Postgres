from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:root@localhost/project_tracker"
app.config["SECRET_KEY"] = b'\xb0\x08Q\xd7\xb4+\xa9\xa7\x1e-\x13k\xcc\x18\x17\xc9 \x08p-\xdb\x917\x87'

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))
    task = db.relationship("Task", back_populates="project", cascade="all, delete-orphan")

    
class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(length=50))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))

    project = db.relationship("Project", back_populates="task")

# Define a route

@app.route("/")
def  show_projects():
    return render_template("index.html", projects=Project.query.all())

@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project=Project.query.filter_by(project_id=project_id).first(),
                           tasks=Task.query.filter_by(project_id=project_id).all())

@app.post("/add/project")
def add_project():
    if not request.form['project-title']:
        flash("Enter a title for your new project", "red")

    else:
        project = Project(title=request.form['project-title'])
        db.session.add(project)
        db.session.commit()
        flash("Project added successfully", "green")

    return redirect(url_for('show_projects'))

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
    if not request.form['task-name']:
        flash("Enter task of this project", "red")
    else:
        task = Task(description=request.form['task-name'], project_id=project_id)
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully", "green")

    return  redirect(url_for('show_tasks', project_id=project_id))


@app.post("/delete/task/<task_id>")
def delete_task(task_id):
        
        # delete task

        task=Task.query.filter_by(task_id=task_id).first()
        original_project_id = task.project.project_id
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully", "green")

        return redirect(url_for('show_tasks', project_id=original_project_id))

@app.post("/delete/project/<project_id>")
def delete_Project(project_id):
        
        # delete task

        project_to_delete=Project.query.filter_by(project_id=project_id).first()   
        db.session.delete(project_to_delete)
        db.session.commit()
        flash("Project deleted successfully", "red")

        return redirect(url_for('show_projects'))


app.run(debug=True, host="127.0.0.1", port=3000)