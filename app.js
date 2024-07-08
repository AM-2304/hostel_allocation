// App.js
import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './components/FileUpload';
import RoomAllocation from './components/RoomAllocation';

function App() {
  const [groupFile, setGroupFile] = useState(null);
  const [hostelFile, setHostelFile] = useState(null);
  const [roomAllocation, setRoomAllocation] = useState([]);

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append('group_file', groupFile);
    formData.append('hostel_file', hostelFile);

    try {
      const response = await axios.post('/api/upload', formData);
      setRoomAllocation(response.data.allocation);
    } catch (error) {
      console.error('Error uploading files:', error);
    }
  };

  return (
    <div>
      <h1>Digitalization of the Hospitality Process</h1>
      <FileUpload
        onGroupFileChange={setGroupFile}
        onHostelFileChange={setHostelFile}
        onUpload={handleFileUpload}
      />
      <RoomAllocation data={roomAllocation} />
    </div>
  );
}

export default App;

