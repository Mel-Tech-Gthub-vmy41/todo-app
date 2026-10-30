# Cloud Task Tracker API

A REST API built with Python and Flask, backed by AWS DynamoDB for cloud data persistence.

## Features
- Full CRUD operations (Create, Read, Delete tasks)
- NoSQL cloud storage with AWS DynamoDB
- Deployed to AWS Elastic Beanstalk
- Secured with IAM and environment variables

## Tech Stack
- Python 3, Flask
- AWS DynamoDB (NoSQL)
- AWS Elastic Beanstalk
- boto3 (AWS SDK)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a new task |
| DELETE | /tasks/<task_id> | Delete a task |

## How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask boto3
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
python3 app.py
```

## Example Usage
```bash
# Create a task
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task"}'

# Get all tasks
curl http://127.0.0.1:5000/tasks
```
