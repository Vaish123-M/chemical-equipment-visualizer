# Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop application for visualizing and analyzing chemical equipment data.

## Tech Stack
- Backend: Django + Django REST Framework
- Web Frontend: React + Chart.js
- Desktop App: PyQt5 + Matplotlib
- Database: SQLite
- Data Analysis: Pandas

## Features
- CSV upload and parsing
- Equipment statistics and summaries
- Data visualization (Web & Desktop)
- Dataset history (last 5 uploads)
- PDF report generation
- Basic authentication

## Project Structure
backend/        - Django REST API  
web-frontend/  - React web dashboard  
desktop-app/   - PyQt5 desktop application  

## Note
The PyQt5 desktop application runs locally and consumes the same backend API.

## Backend Setup
1. Create a virtual environment and install dependencies:
	- `python -m venv .venv`
	- `.venv\Scripts\activate`
	- `pip install -r requirements.txt`
2. Run migrations:
	- `cd backend`
	- `python manage.py makemigrations`
	- `python manage.py migrate`
3. Create a user and token:
	- `python manage.py createsuperuser`
	- Start the server: `python manage.py runserver`
	- Get a token via POST `/api/token/` with username/password.

### Required CSV Columns
The backend expects the CSV columns: `flowrate`, `pressure`, `temperature`, `type`.

## Web Frontend Setup
1. `cd web-frontend`
2. `npm install`
3. `npm run dev`
4. Paste your backend URL and token in the UI.

## Desktop App Setup
1. Ensure backend is running.
2. `python desktop-app/main.py`
3. Configure backend URL + token in the app.
