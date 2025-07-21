#!/usr/bin/env python3
"""
ForensIQ - Digital Forensics File Upload Tool
A simple web application for uploading files for forensic analysis.
"""

import os
import uuid
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Allowed file extensions for security
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 
    'xls', 'xlsx', 'zip', 'rar', '7z', 'log', 'csv', 'json',
    'xml', 'pcap', 'pcapng', 'mem', 'raw', 'dd', 'img', 'iso'
}

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ensure_upload_folder():
    """Ensure the upload folder exists."""
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    """Main page with file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    ensure_upload_folder()
    
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        # Generate a unique filename to prevent conflicts
        original_filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{timestamp}_{unique_id}_{original_filename}"
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Get file info
        file_size = os.path.getsize(file_path)
        
        flash(f'File "{original_filename}" uploaded successfully!')
        return render_template('upload_success.html', 
                             filename=original_filename,
                             saved_filename=filename,
                             file_size=file_size,
                             upload_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        flash('File type not allowed. Please upload a valid file.')
        return redirect(url_for('index'))

@app.route('/uploads')
def list_uploads():
    """List all uploaded files."""
    ensure_upload_folder()
    
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_time = datetime.fromtimestamp(os.path.getctime(file_path))
            files.append({
                'name': filename,
                'size': file_size,
                'upload_time': file_time.strftime('%Y-%m-%d %H:%M:%S')
            })
    
    # Sort by upload time (newest first)
    files.sort(key=lambda x: x['upload_time'], reverse=True)
    
    return render_template('uploads_list.html', files=files)

@app.route('/api/upload', methods=['POST'])
def api_upload():
    """API endpoint for file upload (JSON response)."""
    ensure_upload_folder()
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # Generate unique filename
    original_filename = secure_filename(file.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_id = str(uuid.uuid4())[:8]
    filename = f"{timestamp}_{unique_id}_{original_filename}"
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    file_size = os.path.getsize(file_path)
    
    return jsonify({
        'success': True,
        'message': 'File uploaded successfully',
        'original_filename': original_filename,
        'saved_filename': filename,
        'file_size': file_size,
        'upload_time': datetime.now().isoformat()
    })

if __name__ == '__main__':
    ensure_upload_folder()
    app.run(debug=True, host='0.0.0.0', port=5000)