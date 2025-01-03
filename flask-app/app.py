from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import os


app = Flask(__name__)


metrics = PrometheusMetrics(app, group_by='endpoint')
metrics.info('app_info', 'Application info', version='1.0.3')




@app.route('/', methods=['GET'])
@metrics.histogram(
    'home_requests', 'Request latencies by status and path', labels={
        'status': lambda r: r.status_code, 'path': lambda: request.path})
def home():
    return {"request": "GET", "path": "home page"}

@app.route('/about')
@metrics.histogram(
    'about_requests', 'Request latencies by status and path', labels={
        'status': lambda r: r.status_code, 'path': lambda: request.path})
def about():
    return {"request": "GET", "path": "about", "description": "very simple app for testing github action runners"}



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=False)
