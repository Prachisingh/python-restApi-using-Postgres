from sqlalchemy.orm import registry, relationship, Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# Connect to the database
engine = create_engine("postgresql+psycopg2://postgres:root@localhost/project_tracker", echo=True)
mapper_registry = registry()

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))

    def __repr__(self):
        return "<Project(project_id='{0}', title='{1}')>".format(self.project_id, self.title)
    

class Task(Base):
     __tablename__ = 'tasks'
     task_id = Column(Integer, primary_key=True)
     project_id = Column(Integer, ForeignKey('projects.project_id'))
     description = Column(String(length=50))

     project = relationship("Project")

     def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)
     

Base.metadata.create_all(engine)

with Session(engine) as session:
    clean_house_project = Project(title = "Clean House")
    session.add(clean_house_project)
    session.flush()

    task = Task(description = "Clean BedRoom", project_id = clean_house_project.project_id)
    session.add(task)
    session.commit()