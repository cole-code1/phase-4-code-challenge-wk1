from flask import jsonify , request , Blueprint
from werkzeug.security import generate_password_hash
from models import db, User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data["email"]
    password = generate_password_hash(data["password"])

    check_username = User.query.filter_by(username=username).first()
    check_email = User.query.filter_by(email=email).first()
    
    print("Email",check_email)
    print("Username",check_username)
    if check_username or check_email:
        return jsonify({"error":"Username/email already exists"}), 406

    else:
        new_user = User(username=username, email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success":"Added successfully"}),201
\
@user_bp.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify({"user": user.username, "email": user.email}), 200
    else:
        return jsonify({"error":"User not found"}), 404



@user_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"success":"User deleted successfully"}), 200


@user_bp.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.get_json()
    username = data.get('username')

    if username:
        check_username = User.query.filter_by(username=username).first()

        if check_username and check_username.id != user_id:
            return jsonify({"error":"Username already exists"}), 406
        else:
            user.username = username
            db.session.add(user)
            db.session.commit()
            return jsonify({"success":"User updated successfully"}), 200
    else:
        return jsonify({"error": "user not found"}),404