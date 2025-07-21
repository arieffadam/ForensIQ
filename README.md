# ForensIQ - Digital Forensics File Upload Tool

A simple and secure web application for uploading files for forensic analysis. Built with Flask, ForensIQ provides an intuitive interface for digital forensics professionals to upload evidence files.

## Features

- **Secure File Upload**: Support for multiple file types commonly used in digital forensics
- **File Type Validation**: Only allows approved file extensions for security
- **File Size Limits**: Configurable maximum file size (default: 100MB)
- **Unique File Naming**: Prevents file conflicts with timestamp and UUID-based naming
- **File Management**: View all uploaded files with details
- **Web Interface**: Clean, responsive design optimized for forensics workflows
- **API Endpoint**: RESTful API for programmatic file uploads
- **Drag & Drop**: Modern file upload interface with drag and drop support

## Supported File Types

### Documents
- PDF, DOC, DOCX, XLS, XLSX, TXT, CSV

### Images
- PNG, JPG, JPEG, GIF

### Archives
- ZIP, RAR, 7Z

### Forensic Evidence
- DD, IMG, RAW, ISO, MEM (memory dumps)
- PCAP, PCAPNG (network captures)

### Logs & Data
- LOG, JSON, XML

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arieffadam/ForensIQ.git
   cd ForensIQ
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface

1. **Upload Files**: Navigate to the home page and use the file upload form
2. **View Files**: Click "View Files" to see all uploaded files
3. **File Details**: After upload, view file information including size and timestamp

### API Usage

Upload files programmatically using the REST API:

```bash
curl -X POST -F "file=@evidence.pcap" http://localhost:5000/api/upload
```

Response:
```json
{
  "success": true,
  "message": "File uploaded successfully",
  "original_filename": "evidence.pcap",
  "saved_filename": "20250121_143022_a1b2c3d4_evidence.pcap",
  "file_size": 1048576,
  "upload_time": "2025-01-21T14:30:22.123456"
}
```

## Configuration

### Environment Variables

- `FLASK_ENV`: Set to `development` for debug mode
- `SECRET_KEY`: Change the secret key in production

### File Upload Settings

In `app.py`, you can modify:

- `MAX_CONTENT_LENGTH`: Maximum file size (default: 100MB)
- `UPLOAD_FOLDER`: Directory for uploaded files (default: 'uploads')
- `ALLOWED_EXTENSIONS`: Set of allowed file extensions

## Security Features

- **File Extension Validation**: Only approved file types are accepted
- **Secure Filename Handling**: Uses `secure_filename()` to prevent path traversal
- **Unique File Names**: Prevents file overwrites with timestamp and UUID
- **File Size Limits**: Prevents abuse with configurable size limits

## Directory Structure

```
ForensIQ/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore           # Git ignore rules
├── static/
│   └── style.css        # CSS styles
├── templates/
│   ├── base.html        # Base template
│   ├── index.html       # Upload form
│   ├── upload_success.html  # Success page
│   └── uploads_list.html    # File listing
└── uploads/             # Uploaded files directory
    └── .gitkeep
```

## Development

To contribute to ForensIQ:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, please open an issue on the GitHub repository.

---

**Note**: This tool is designed for forensic professionals. Always follow proper evidence handling procedures and legal requirements when processing digital evidence.