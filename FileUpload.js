// FileUpload.js
import React from 'react';

function FileUpload({ onGroupFileChange, onHostelFileChange, onUpload }) {
  const handleGroupFileChange = (event) => {
    onGroupFileChange(event.target.files[0]);
  };

  const handleHostelFileChange = (event) => {
    onHostelFileChange(event.target.files[0]);
  };

  return (
    <div>
      <h2>Upload Files</h2>
      <input type="file" onChange={handleGroupFileChange} />
      <input type="file" onChange={handleHostelFileChange} />
      <button onClick={onUpload}>Upload and Allocate Rooms</button>
    </div>
  );
}

export default FileUpload;

