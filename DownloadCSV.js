import React from 'react';
import { saveAs } from 'file-saver';

function DownloadCSV({ data }) {
  const downloadCSV = () => {
    const csvData = [
      ['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'],
      ...data.map(({ group_id, hostel_name, room_number, members_allocated }) => [
        group_id,
        hostel_name,
        room_number,
        members_allocated,
      ]),
    ];

    const csvContent = csvData.map((row) => row.join(',')).join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8' });
    saveAs(blob, 'room_allocation.csv');
  };

  return (
    <div>
      <button onClick={downloadCSV}>Download CSV</button>
    </div>
  );
}

export default DownloadCSV;
