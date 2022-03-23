import enum
from app import db


class ApplicationHubStatus(enum.Enum):
    in_preparation = 1
    ready_for_submission = 2
    resubmit_in_progress = 3
    resubmitted = 4
    applied = 5


class AchievementGroup(enum.Enum):
    awards_and_recognitions = 1
    course_and_certificates = 2
    experience_and_volunteering = 3


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    grading_schema = db.Column(db.String)
    value = db.Column(db.String)
