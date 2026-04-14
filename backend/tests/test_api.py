from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_courses():
    res = client.get('/api/courses')
    assert res.status_code == 200
    assert res.json()['total'] >= 2


def test_lab_run_grade_flow():
    run = client.post('/api/labs/lab-linux-1/runs').json()['runId']
    grade = client.post(f'/api/lab-runs/{run}/grade')
    assert grade.status_code == 200
    assert grade.json()['status'] == 'passed'
