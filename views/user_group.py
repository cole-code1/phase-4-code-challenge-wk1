from flask import jsonify , request , Blueprint
from models import db, UserGroup , User


user_group_bp = Blueprint('user_group_bp', __name__)

@user_group_bp.route('/user_group', methods=['POST'])
def create_user_group():
    data = request.get_json()
    group_name = data['group_name']
    

    check_group = UserGroup.query.filter_by(group_name=group_name).first()
    if check_group:
        return jsonify({"error":"Group name already exists"}), 406
    
    else:
        new_group = UserGroup(group_name=group_name)
        db.session.add(new_group)
        db.session.commit()


        return jsonify({"success":"Added successfully"}), 201
    

@user_group_bp.route('/get_user_group/<int:group_id>', methods=['GET'])
def get_user_group(group_id):
    group = UserGroup.query.get(group_id)

    if group:
        return jsonify({"group": group.group_name}), 200
    else:
        return jsonify({"error":"Group not found"}), 404
    
@user_group_bp.route('/delete-user_group/<int:group_id>', methods=['DELETE'])
def delete_user_group(group_id):
    group = UserGroup.query.get(group_id)
    db.session.delete(group)
    db.session.commit()
    return jsonify({"success":"Group deleted successfully"}), 200

@user_group_bp.route('/update-user_group/<int:group_id>', methods=['PATCH'])
def update_user_group(group_id):
    group = UserGroup.query.get(group_id)
    data = request.get_json()
    group_name = data.get('group_name')

    if group_name:
        group.group_name = group_name
        
        check_group = UserGroup.query.filter_by(group_name=group_name).first()

        if check_group and check_group.id != group_id:
            return jsonify({"error":"Group name already exists"}), 406
        else:
            group.group_name = group_name
            db.session.add(group)
            db.session.commit()
            return jsonify({"success":"Group updated successfully"}), 200