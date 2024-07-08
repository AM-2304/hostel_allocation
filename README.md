# Hostel Allocation Project

## Overview
The Hostel Allocation project is a web application built using Flask, a popular Python web framework. The application helps streamline the process of allocating students to rooms in a hostel based on their group information and the available hostel data.

## Features
- **Automated Allocation**: The application uses an intelligent algorithm to efficiently assign students to rooms based on their preferences and group information.
- **Real-Time Monitoring**: Users can track the allocation process and view the updated room assignments in real-time.
- **Customizable Settings**: The application allows administrators to tailor the allocation rules and preferences to fit their institution's specific needs.
- **User-Friendly Interface**: The project features a clean and modern user interface designed by a top designer and software engineer, providing an intuitive experience for users.

## Usage
1. **File Upload**: Users can upload the necessary CSV files containing group information and hostel information through the file upload section of the application.
2. **Allocation Process**: Once the files are uploaded, the application's algorithm will process the data and automatically assign students to rooms.
3. **Allocation Display**: The assigned room allocations will be displayed in a tabular format, allowing users to view the results.

## Technical Details
The project is structured as follows:

hostel_allocation/
├── app.py
├── models.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/
└── index.html


1. **app.py**: This is the main Flask application file, where the routes and server-side logic are defined.
2. **models.py**: This file contains the database models for the project, such as `GroupInfo` and `HostelInfo`.
3. **static/ directory**: This directory holds the CSS and JavaScript files used in the project.
   - `css/`: Contains the CSS file(s) for styling the application.
   - `js/`: Contains the JavaScript file(s) for adding interactivity to the application.
4. **templates/ directory**: This directory holds the HTML template(s) used by the Flask application.
   - `index.html`: The main HTML template for the application's user interface.

The application's logic is divided between the server-side (Flask) and the client-side (JavaScript):

- **Server-side Logic**: The Flask application handles the file upload, data processing, and room allocation logic. It also provides the necessary API endpoints for the client-side to interact with.
- **Client-side Logic**: The JavaScript code in the `script.js` file handles the user interface interactions, such as file uploads, progress tracking, and displaying the allocation results.

## Installation and Setup
1. Clone the repository: `git clone https://github.com/your-username/hostel-allocation.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`
6. Open your web browser and navigate to `http://localhost:5000`

## Contributing
If you would like to contribute to the project, please follow these steps:
1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push to the branch
5. Submit a pull request

## License
This project is licensed under the [MIT License](LICENSE).
