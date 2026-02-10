# Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop application for visualizing and analyzing chemical equipment data with a modern, fully responsive interface.

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

- `POST /api/token/` - Obtain authentication token
- `POST /api/upload/` - Upload CSV file
- `GET /api/summary/<id>/` - Get dataset summary
- `GET /api/history/` - Get last 5 uploads
- `GET /api/report/<id>/` - Download PDF report

### 📋 Required CSV Columns

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

A sample CSV file is provided: `sample_euipment_data.csv`

This file contains chemical equipment data with the required columns for testing the application.

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

**Built with ❤️ for Chemical Equipment Analysis**
