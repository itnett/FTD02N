python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import subprocess
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scans.db'
db = SQLAlchemy(app)

class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    result = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    criticality = db.Column(db.String(20), default='Medium')
    comments = db.Column(db.Text, default='No comments')

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_scan', methods=['POST'])
def start_scan():
    target = request.form['target']
    method = request.form['method']
    language = request.form['language']
    
    if language == 'bash':
        script_path = f'scans/{method}.sh'
        result = subprocess.run([script_path, target], capture_output=True, text=True)
    elif language == 'python':
        script_path = f'scans/{method}.py'
        result = subprocess.run(['python3', script_path, target], capture_output=True, text=True)
    elif language == 'java':
        compile_result = subprocess.run(['javac', f'scans/{method}.java'], capture_output=True, text=True)
        if compile_result.returncode != 0:
            output = compile_result.stdout + compile_result.stderr
            new_scan = ScanResult(target=target, method=method, language=language, result=output)
            db.session.add(new_scan)
            db.session.commit()
            return redirect(url_for('view_results'))
        
        result = subprocess.run(['java', '-cp', 'scans', method[:-5], target], capture_output=True, text=True)

    output = result.stdout
    
    new_scan = ScanResult(target=target, method=method, language=language, result=output)
    db.session.add(new_scan)
    db.session.commit()
    
    return redirect(url_for('view_results'))

@app.route('/results')
def view_results():
    scans = ScanResult.query.order_by(ScanResult.date.desc()).all()
    return render_template('results.html', scans=scans)

@app.route('/update_scan', methods=['POST'])
def update_scan():
    scan_id = request.form['scan_id']
    criticality = request.form['criticality']
    comments = request.form['comments']
    
    scan = ScanResult.query.get(scan_id)
    scan.criticality = criticality
    scan.comments = comments
    db.session.commit()
    
    return redirect(url_for('view_results'))

@app.route('/report/<int:scan_id>')
def report(scan_id):
    scan = ScanResult.query.get(scan_id)
    return render_template('report.html', scan=scan)

if __name__ == '__main__':
    app.run(debug=True)