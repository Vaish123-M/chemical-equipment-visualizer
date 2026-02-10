# Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop application for visualizing and analyzing chemical equipment data with a modern, fully responsive interface.

---

## 🎓 For Evaluators: Quick Start Guide

This project implements all required features for the intern screening task. Follow these steps to evaluate:

### ⚡ Quick Setup (5 minutes)

1. **Install Python dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Setup database and create admin user:**
   ```bash
   cd backend
   python manage.py migrate
   python manage.py createsuperuser
   # Enter username, email (optional), password when prompted
   ```

3. **Generate API token (copy the token shown):**
   ```bash
   python manage.py shell -c "from rest_framework.authtoken.models import Token; from django.contrib.auth.models import User; user = User.objects.first(); token, _ = Token.objects.get_or_create(user=user); print('TOKEN:', token.key)"
   ```
   **Important**: The token is dynamically generated and unique to your installation. Copy it for use in step 5.

4. **Start backend server:**
   ```bash
   python manage.py runserver
   # Backend runs at http://127.0.0.1:8000
   ```

5. **Start web frontend (new terminal):**
   ```bash
   cd web-frontend
   npm install
   npm run dev
   # Frontend runs at http://localhost:5173
   ```

6. **Test the application:**
   - Open browser to `http://localhost:5173`
   - Enter backend URL: `http://127.0.0.1:8000`
   - Paste your generated token from step 3
   - Upload `sample_euipment_data.csv` (provided in root folder)
   - Verify: Summary cards, type distribution chart, averages chart appear
   - Check history section shows the uploaded dataset
   - Test PDF download: `http://127.0.0.1:8000/api/report/1/` (after first upload)

7. **Test desktop app (optional):**
   ```bash
   python desktop-app/main.py
   ```
   - Configure backend URL and token in the GUI
   - Upload CSV and verify Matplotlib charts render

### ✅ Requirements Verification Checklist

**Functional Requirements:**
- ✅ **CSV Upload**: Web UI uploads CSV to Django REST backend (`POST /api/upload/`)
- ✅ **Data Summary**: Backend returns total count, avg flowrate/pressure/temperature, type distribution
- ✅ **Visualization**: Chart.js used for bar (type distribution) and line (averages) charts
- ✅ **History Management**: Last 5 datasets stored in database, displayed in web UI
- ✅ **PDF Report**: API endpoint `/api/report/<id>/` generates PDF with ReportLab
- ✅ **Authentication**: Token-based auth (Django REST Framework), client sends `Authorization: Token <key>` header

**Tech Stack:**
- ✅ **React.js** - Web frontend (React 18.2.0)
- ✅ **Chart.js** - Data visualization (v4.4.1 with react-chartjs-2)
- ✅ **Django + DRF** - Backend API (Django 4.2+, djangorestframework 3.14+)
- ✅ **Pandas** - CSV parsing and analytics (pandas 2.1+)
- ✅ **SQLite** - Database (configured in settings.py)

**Bonus Features:**
- ✅ PyQt5 desktop application with Matplotlib charts
- ✅ Fully responsive web design (mobile to desktop)
- ✅ Modern UI with gradients and animations
- ✅ Case-insensitive CSV column matching
- ✅ Comprehensive error handling

---

## 🎯 Overview

Chemical Equipment Parameter Visualizer is a hybrid web and desktop application that enables users to upload chemical equipment data in CSV format and instantly view key analytics. The platform provides summary statistics, interactive charts, and dataset history through a shared backend, making equipment monitoring and analysis simple and efficient.

## ✨ Key Features

### 📤 CSV Upload
- Web and Desktop interfaces for seamless file uploads
- Automatic parsing with Pandas
- Support for custom column names (case-insensitive)

### 📊 Data Summary API
- Django REST API returns real-time statistics
- Total count, averages (flowrate, pressure, temperature)
- Equipment type distribution analysis

### 📈 Visualization
- **Web**: Interactive charts using Chart.js with gradients
- **Desktop**: Professional Matplotlib charts
- Type distribution bar charts
- Trend analysis line charts

### 🗂️ History Management
- Stores last 5 uploaded datasets
- Quick access to previous analyses
- Summary statistics for each upload

### 📄 PDF Reports
- Generate comprehensive PDF reports
- Include statistics and visualizations
- Download via API endpoint (`/api/report/<id>/`)

### 🔐 Authentication
- Token-based authentication (Django REST Framework)
- Secure API access
- User management via Django admin

## 🛠 Tech Stack

### Backend
- **Django 4.2+** - Web framework
- **Django REST Framework** - API development
- **Pandas** - CSV parsing and data analysis
- **ReportLab** - PDF generation
- **SQLite** - Database (easily switchable)

### Web Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Chart.js** - Data visualization
- **CSS3** - Modern styling with gradients and animations

### Desktop App
- **PyQt5** - GUI framework
- **Matplotlib** - Data visualization
- **Requests** - API communication

## 📱 Responsive Design

The web application is fully responsive and optimized for all devices:

### 📱 Mobile Devices (< 480px)
- Single column layout
- 2x2 card grid for summary statistics
- Stack feature cards vertically
- Touch-friendly buttons (48px minimum)
- Optimized font sizes and spacing

### 📱 Tablets (481px - 768px)
- 2-column layout for features and cards
- Single column for main charts
- Balanced spacing and readability

### 💻 Small Laptops (769px - 1024px)
- 3-column feature grid
- 2-column chart layout
- 4-column summary cards

### 🖥️ Desktops (1025px+)
- Full 3-column grid layout
- 4-column summary cards
- Optimal spacing and visual hierarchy

### 🖥️ Large Displays (> 1440px)
- Max-width container with centered content
- Enhanced spacing for better readability
- Large typography for comfortable viewing

## 📂 Project Structure

```
chemical-equipment-visualizer/
├── backend/                          # Django REST API
│   ├── chemical_visualizer_backend/  # Project settings
│   ├── api/                          # API application
│   │   ├── models.py                 # EquipmentDataset model
│   │   ├── views.py                  # API endpoints
│   │   ├── serializers.py            # DRF serializers
│   │   └── urls.py                   # API routes
│   └── manage.py                     # Django management
├── web-frontend/                     # React web app
│   ├── src/
│   │   ├── components/               # React components
│   │   ├── App.jsx                   # Main app component
│   │   ├── api.js                    # API client
│   │   └── styles.css                # Global styles
│   ├── index.html                    # HTML template
│   └── package.json                  # Dependencies
├── desktop-app/                      # PyQt5 desktop app
│   └── main.py                       # Desktop application
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🚀 Backend Setup

1. **Create virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create superuser and get token:**
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
   ```

4. **Get authentication token:**
   ```bash
   python manage.py shell -c "from rest_framework.authtoken.models import Token; from django.contrib.auth.models import User; user = User.objects.first(); token, _ = Token.objects.get_or_create(user=user); print('TOKEN:', token.key)"
   ```

### ⚙️ API Endpoints

All endpoints require authentication via `Authorization: Token <your-token>` header.

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| `POST` | `/api/token/` | Obtain authentication token | `username`, `password` | `{"token": "abc123..."}` |
| `POST` | `/api/upload/` | Upload CSV file | FormData with `file` | Dataset summary object |
| `GET` | `/api/summary/<id>/` | Get dataset summary | - | Dataset object with statistics |
| `GET` | `/api/history/` | Get last 5 uploads | - | Array of dataset summaries |
| `GET` | `/api/report/<id>/` | Download PDF report | - | PDF file download |

**Response Example** (`POST /api/upload/`):
```json
{
  "id": 1,
  "upload_time": "2026-02-10T14:30:00Z",
  "total_count": 100,
  "avg_flowrate": 112.5,
  "avg_pressure": 6.8,
  "avg_temperature": 98.2,
  "type_distribution": {
    "Pump": 35,
    "Compressor": 25,
    "Valve": 20,
    "Heat Exchanger": 20
  }
}
```

### � Authentication Token Notes

**Important for Evaluators:**
- The authentication token is **NOT hardcoded** in the application
- Each installation generates its own unique token
- You must generate a token after creating your superuser (see step 3 in Quick Start)
- The token is tied to your user account in the database
- Store the token securely - you'll need it for both web and desktop clients

**Token Generation Command:**
```bash
python manage.py shell -c "from rest_framework.authtoken.models import Token; from django.contrib.auth.models import User; user = User.objects.first(); token, _ = Token.objects.get_or_create(user=user); print('TOKEN:', token.key)"
```

This command will output something like: `TOKEN: 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

Copy this token and use it in the web frontend or desktop app configuration.

### �📋 Required CSV Columns

The backend expects CSV files with these columns (case-insensitive):
- `flowrate` - Equipment flow rate
- `pressure` - Operating pressure
- `temperature` - Operating temperature
- `type` - Equipment type/category

**Example:**
```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110
Compressor-1,Compressor,95,8.4,95
```

### ✔️ Expected Results After Upload

When you upload a CSV file successfully, you should see:

1. **Summary Cards (4 cards displaying):**
   - Total Equipment Count (e.g., "100")
   - Average Flowrate (e.g., "112.5")
   - Average Pressure (e.g., "6.8")
   - Average Temperature (e.g., "98.2")

2. **Type Distribution Chart:**
   - Colorful bar chart showing equipment types on X-axis
   - Count of each type on Y-axis
   - Bars with different colors and rounded corners

3. **Trend Analysis Chart:**
   - Line chart with three data points (Flowrate, Pressure, Temperature)
   - Shows average values for each parameter
   - Filled area under the line

4. **Recent Uploads Section:**
   - List of up to 5 most recent uploads
   - Shows Dataset ID and upload timestamp
   - Click any item to reload that dataset's summary

5. **Status Messages:**
   - "Upload complete." after successful upload
   - "Loading history..." while fetching data
   - Error messages if something goes wrong

**Verification Commands:**

```bash
# Check database has data
cd backend
python manage.py shell -c "from api.models import EquipmentDataset; print(f'Datasets in DB: {EquipmentDataset.objects.count()}')"

# Download PDF report directly
curl -H "Authorization: Token YOUR_TOKEN_HERE" http://127.0.0.1:8000/api/report/1/ --output report.pdf

# Test API endpoints
curl -H "Authorization: Token YOUR_TOKEN_HERE" http://127.0.0.1:8000/api/history/
```

## 🌐 Web Frontend Setup

1. **Install dependencies:**
   ```bash
   cd web-frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

3. **Access the application:**
   - Open browser to `http://localhost:5173` (or shown URL)
   - Enter backend URL: `http://127.0.0.1:8000`
   - Paste your API token
   - Upload a CSV file to get started

### 🏗️ Build for Production

```bash
npm run build
npm run preview  # Test production build
```

## 🖥️ Desktop App Setup

1. **Ensure backend is running**

2. **Launch desktop application:**
   ```bash
   python desktop-app/main.py
   ```

3. **Configure in the app:**
   - Backend URL: `http://127.0.0.1:8000`
   - API Token: (paste your token)
   - Upload CSV and view results

### 🎨 Desktop Features
- File upload dialog
- Summary statistics display
- Matplotlib charts (type distribution + averages)
- History list with click-to-load
- Settings persistence (QSettings)

## 🧪 Testing with Sample Data

A ready-to-use sample CSV file is provided in the root directory: **`sample_euipment_data.csv`**

### Sample Data Details:
- **100 rows** of chemical equipment data
- **Columns**: Equipment Name, Type, Flowrate, Pressure, Temperature
- **Equipment Types**: Pump, Compressor, Valve, Heat Exchanger
- **Realistic values** for testing visualizations

### Testing Steps:
1. Start both backend and frontend servers
2. Enter your API token in the web UI
3. Click "Choose File" and select `sample_euipment_data.csv`
4. Click "Upload CSV"
5. Observe the summary statistics and charts populate
6. Check the "Recent Uploads" section shows your upload
7. Test PDF download: Navigate to `http://127.0.0.1:8000/api/report/1/` (or use the ID shown)

**Creating Your Own Test CSV:**
```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Test-Pump-1,Pump,150.5,7.2,105.3
Test-Valve-1,Valve,85.0,3.5,75.8
Test-Compressor-1,Compressor,200.0,12.1,120.5
```

Minimum requirements: Include columns `flowrate`, `pressure`, `temperature`, `type` (case-insensitive).

## 🔒 Security Notes

- **Development Mode**: Uses `DEBUG = True` and `SECRET_KEY` is exposed
- **Production**: 
  - Set `DEBUG = False`
  - Use environment variables for `SECRET_KEY`
  - Configure `ALLOWED_HOSTS`
  - Use HTTPS
  - Enable CORS only for trusted domains
  - Consider database authentication

## 🎨 Design Features

### Modern UI/UX
- Gradient backgrounds and glassmorphism effects
- Smooth animations (fade-in, slide-up, hover effects)
- Professional color palette (blue/green scientific theme)
- Responsive typography with `clamp()` functions
- Dark mode support (system preference)

### Accessibility
- Touch-friendly UI elements (min 48px touch targets)
- Keyboard navigation support
- Reduced motion support for accessibility
- High contrast colors
- Semantic HTML structure

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available for educational and commercial use.

## 🐛 Troubleshooting

### Django Import Error
```bash
# Make sure Django is installed
pip install -r requirements.txt
```

### Token Required Error
```bash
# Generate a new token
python manage.py shell -c "from rest_framework.authtoken.models import Token; from django.contrib.auth.models import User; user = User.objects.first(); token, _ = Token.objects.get_or_create(user=user); print(token.key)"
```

### CSV Column Error
- Ensure CSV has columns: `flowrate`, `pressure`, `temperature`, `type`
- Column names are case-insensitive
- Check for typos or extra spaces

### Port Already in Use
```bash
# Backend
python manage.py runserver 8001

# Frontend
# Vite will automatically try alternative ports
```

## 📞 Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

## 📋 Evaluator Summary

### Project Compliance

This project **fully implements** all requirements for the Chemical Equipment Visualizer intern screening task:

**✅ Functional Requirements Met:**
1. **CSV Upload** - Web UI with file upload, FormData POST to Django backend
2. **Data Summary** - Backend calculates and returns total count, 3 averages, type distribution
3. **Visualization** - Chart.js Bar chart (type distribution) + Line chart (averages)
4. **History** - Database-backed last 5 uploads, displayed in UI with click-to-load
5. **PDF Report** - ReportLab generates PDF, served via Django API endpoint
6. **Authentication** - Token-based auth using DRF, tokens attached in Authorization header

**✅ Technology Requirements Met:**
1. **React.js** - Version 18.2.0 for web frontend
2. **Chart.js** - Version 4.4.1 for data visualization
3. **Django + DRF** - Backend framework with RESTful APIs
4. **Pandas** - CSV parsing and statistical calculations
5. **SQLite** - Database for dataset persistence

**🎁 Additional Features:**
- PyQt5 desktop application with Matplotlib visualizations
- Fully responsive design (mobile to 4K displays)
- Modern UI with gradients, animations, and accessibility features
- Case-insensitive CSV column parsing for flexibility
- Automatic cleanup of old datasets (keeps last 5)
- Comprehensive error handling and validation
- PDF report generation with detailed statistics

### Key Files for Review:
- **Backend API**: [backend/api/views.py](backend/api/views.py) - All endpoints with Pandas processing
- **Frontend**: [web-frontend/src/App.jsx](web-frontend/src/App.jsx) - React main component
- **Charts**: [web-frontend/src/components/TypeDistributionChart.jsx](web-frontend/src/components/TypeDistributionChart.jsx), [AveragesChart.jsx](web-frontend/src/components/AveragesChart.jsx)
- **Model**: [backend/api/models.py](backend/api/models.py) - Database schema
- **Auth**: [backend/chemical_visualizer_backend/settings.py](backend/chemical_visualizer_backend/settings.py) - Token authentication config

### Time to Evaluate: ~10 minutes
- Setup: 5 minutes (install dependencies, create user, generate token)
- Testing: 5 minutes (upload CSV, verify all features work)

---

**Built with ❤️ for Chemical Equipment Analysis**
