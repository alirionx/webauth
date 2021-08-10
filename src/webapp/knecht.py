from main import db, User, Roles

myUser = User.query.filter_by(email="dquilitzsch@outlook.de").first()
myUser.generate_password_hash("Oviss1234!")
print(myUser.password_hash)

usrRole = Roles.query.filter_by(name="user").first()

res = myUser.verify_password("Oviss1234!")
print(res)

db.session.commit()