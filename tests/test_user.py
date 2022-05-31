from ioet_coding_exercise.User import User


def test_user():
    new_user = User(name="Ariel")

    assert new_user.name == "Ariel"
    assert len(new_user.statements) == 0
