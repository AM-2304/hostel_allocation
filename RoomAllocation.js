// RoomAllocation.js
import React from 'react';
import { saveAs } from 'file-saver';

function RoomAllocation({ data }) {
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
      <h2>Room Allocation</h2>
      <table>
        <thead>
          <tr>
            <th>Group ID</th>
            <th>Hostel Name</th>
            <th>Room Number</th>
            <th>Members Allocated</th>
          </tr>
        </thead>
        <tbody>
          {data.map((allocation, index) => (
            <tr key={index}>
              <td>{allocation.group_id}</td>
              <td>{allocation.hostel_name}</td>
              <td>{allocation.room_number}</td>
              <td>{allocation.members_allocated}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={downloadCSV}>Download CSV</button>
    </div>
  );
}

export default RoomAllocation;
