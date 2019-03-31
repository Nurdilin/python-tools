from flask import Flask
from flask import jsonify

app = Flask(__name__)



usersdata = [
        {
            'id': 1,
            'username': u'test',
            'active': True
        },
        {
           'id': 2,
            'username': u'test2',
            'active': False
        }
]



@app.route('/')
def index():
    return "Hello"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': usersdata})

@app.route('/users/<int:id>/', methods=['GET'])
def get_user(id):
    for user in usersdata:
        if user.get("id") == id:
            return jsonify({'users': user})
        abort(404)


@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)
    



if __name__ == '__main__':
    app.run(debug=True)
