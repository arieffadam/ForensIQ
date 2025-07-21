import React, { useState, useEffect } from 'react';

function Home() {
  const [file, setFile] = useState(null);
  const [cases, setCases] = useState([]);
  const [message, setMessage] = useState('');

  // Replace with your backend API endpoint
  const apiEndpoint = process.env.REACT_APP_API_ENDPOINT || 'http://localhost:3001';

  useEffect(() => {
    // Fetch case status from backend (stub example)
    async function fetchCases() {
      // TODO: Replace with real API call
      setCases([
        { case_id: 'sample-case', filename: 'sample-file.txt', status: 'Analyzed', yara_result: ['SuspiciousExe'] }
      ]);
    }
    fetchCases();
  }, []);

  const handleFileChange = e => setFile(e.target.files[0]);

  const handleUpload = async e => {
    e.preventDefault();
    if (!file) return;

    // Upload file to backend or S3 (stub example)
    setMessage('Uploading...');
    // TODO: Replace with real upload logic
    setTimeout(() => setMessage('Upload complete!'), 1000);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>ForensIQ MVP Dashboard</h1>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload Evidence</button>
      </form>
      <p>{message}</p>
      <h2>Case Status</h2>
      <table border="1" cellPadding="6">
        <thead>
          <tr>
            <th>Case ID</th>
            <th>Filename</th>
            <th>Status</th>
            <th>YARA Result</th>
          </tr>
        </thead>
        <tbody>
          {cases.map((c, i) => (
            <tr key={i}>
              <td>{c.case_id}</td>
              <td>{c.filename}</td>
              <td>{c.status}</td>
              <td>{c.yara_result.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Home;