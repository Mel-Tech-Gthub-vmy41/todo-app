from flask import Flask, request, jsonify
import boto3
import uuid
import os

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-2',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

table = dynamodb.Table('Tasks')
@app.route('/tasks', methods=['GET'])
def get_tasks():
    result = table.scan()
    return jsonify(result['Items'])
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {'task_id': str(uuid.uuid4()), 'title': data['title'], 'done': False}
    table.put_item(Item=new_task)
    return jsonify(new_task), 201
if __name__ == '__main__':
    app.run(debug=True)
