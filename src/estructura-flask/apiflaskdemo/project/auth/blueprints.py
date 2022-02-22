from apiflaskdemo.project.models import User
from apiflask import APIBlueprint, abort, input, output
from apiflask.fields import String
from apiflaskdemo.project.auth.schemas import LoginSchema
from flask import session, g

auth_bp = APIBlueprint("auth_bp", __name__)

@auth_bp.before_app_request
def user_checkout():
    user_id = session.get("user_id")
    if user_id is None:
        g.user =None
    else:
        g.user = User.query.filter_by(id=user_id).first()

@auth_bp.post("/login")
@input(LoginSchema)
def login(data):
    user = User.query.filter_by(username=data["username"]).one_or_none()
    if user and user.password == data["password"]:
        session.clear()
        session["user_id"] = user.id
        return {'msg': 'logged in'}
    else:
        abort(403)

@auth_bp.get("/logout")
def logout():
    session.clear()
    return {"msg": "logged out"}