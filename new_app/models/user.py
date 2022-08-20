from models import UserModel, session


def create_test_users(n: int):
    '''Создадим users'''
    print(f'Create test user n={n}')
    for i in range(n):
        user = UserModel(name=f'user_{i}')
        session.add(user)
    session.commit()


def get_user(user_name: str):
    return session.query(UserModel).filter(UserModel.name == user_name).first()


def get_all_user():
    return session.query(UserModel).all()


def add_user(user_name: str):
    user = UserModel(name=user_name)
    session.add(user)
    session.commit()
