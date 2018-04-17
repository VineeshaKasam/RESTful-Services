from flask import Flask, request, abort, render_template
import json

from services.user_service import UserService

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('restfulServices.html')


@app.route('/getusers', methods=['GET'])
def get_users():
    users = UserService.get_users()
    if not users:
        abort(404)
    users_json = json.dumps(users, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return render_template("userProfileDetails.html ", users_json = users_json)


@app.route('/getuser', methods=['GET'])
def get_user():
    username = request.form.get("username")
    print username
    user = UserService.get_user(username)
    print "User is", user
    if user is None:
        abort(404)
    user_json = json.dumps(user, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print user_json
    return render_template("userProfileDetails.html ", user_json = user_json)


@app.route('/postuser', methods=['POST'])
def post_user():
    username = request.form.get("username")
    if username in UserService.users:
        print("User already exists")
        abort(409)
    displayName = request.form.get("displayName")
    department = request.form.get("department")
    username, displayName, department = UserService.add_user(username, displayName, department)
    return render_template("userProfileDetails.html ", name=username, displayName=displayName, department=department)


@app.route('/updateuser', methods=['PUT'])
def update_user():
    username = request.form.get("username")
    print username
    displayName = request.form.get("displayName")
    department = request.form.get("department")
    username = UserService.update_user(username, displayName, department)
    return render_template("userProfileDetails.html ", name=username)


@app.route('/deleteuser', methods=['GET', 'DELETE'])
def delete_user():
    username = request.form.get("username")
    print username
    user = UserService.get_user(username)
    print user
    if user is None or username not in UserService.users:
        print("User does not exist")
        abort(404)
    else:
        status = UserService.delete_user(username)
        if status:
            return render_template("userProfileDetails.html ", name=username)
        else:
            abort(404)


if __name__ == '__main__':

    app.run(debug=True)
