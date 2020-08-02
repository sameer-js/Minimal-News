from . import db


categories = {
    'politics': 1,
    'sports': 2,
    'finance': 3,
    'lifestyle': 4,
}


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    preferred_time = db.Column(db.String(8), index=True)
    subscriptions = db.Column(db.Integer)
    verified = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.subscriptions is None:
            self.subscriptions = 0

    def __repr__(self):
        return f'User {self.email}'

    def add_subscription(self, category):
        if not self.is_subscribed(category):
            self.subscriptions += category

    def remove_subscription(self, category):
        if self.is_subscribed(category):
            self.subscriptions -= category

    def is_subscribed(self, category):
        return self.subscriptions & category == category

    def list_subscriptions(self):
        subscription_list = list()
        for category in categories:
            if self.is_subscribed(categories[category]):
                subscription_list.append(category)
        return subscription_list