from flask_login import login_user
from extensions import db


class CRUDMixin:
    """Custom mixin to add repetitive CRUD methods to an extended model."""
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    num_visits = db.Column(db.Integer, default=0)

    @classmethod
    def get_by_id(cls, id):
        if isinstance(id, str):
            id = int(id)
        return cls.query.get(id)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def _update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save(commit=commit) or self

    def update(self, commit=True, **kwargs):
        return self._update(commit=commit, **kwargs)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    def increment_visits(self):
        self._update(num_visits=self.num_visits + 1)


def login_and_increment_visits(user):
    user.increment_visits()
    login_user(user)
