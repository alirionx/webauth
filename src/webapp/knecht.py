from main import db, User

myUser = User.query.filter_by(email="dquilitzsch@outlook.de").first()
myUser.generate_password_hash("Oviss1234!")

print(myUser.password_hash)

res = myUser.verify_password("Oviss1234!")
print(res)

db.session.commit()