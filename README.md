# Cuba Educational Travel - Flask Web Application

A complete, production-ready Flask recreation of the Cuba Educational Travel website (cubaeducationaltravel.com) with improved text contrast and professional design.

## 🚀 Features

- **Complete Website**: All pages fully implemented with professional content - no placeholders
- **Improved Accessibility**: Enhanced text contrast for better readability (dark text on light backgrounds)
- **Responsive Design**: Bootstrap 5 with Cuban-inspired color palette
- **Professional Content**: Comprehensive information about CET's services, testimonials, and resources
- **Production Ready**: Security features, error handling, and deployment configuration
- **SEO Optimized**: Meta tags, semantic HTML, and clean URLs

## 📁 Project Structure

```
cuba_educational_travel/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore file
├── Procfile                       # Heroku deployment file
├── README.md                      # This file
├── static/
│   ├── css/
│   │   └── style.css             # Custom CSS with improved contrast
│   ├── js/
│   │   └── main.js               # Custom JavaScript
│   └── images/                   # Placeholder for images
├── templates/
│   ├── base.html                 # Base template with navigation
│   ├── index.html                # Homepage
│   ├── contact.html              # Contact page
│   ├── blog.html                 # Cuba Blog page
│   ├── cuba_travel/              # Cuba Travel pages
│   │   ├── people_to_people.html
│   │   ├── private_trips.html
│   │   ├── academic_programs.html
│   │   ├── cet_luxury.html
│   │   ├── corporate_travel.html
│   │   └── events_cuba.html
│   ├── about/                    # About CET pages
│   │   ├── story.html
│   │   ├── testimonials.html
│   │   ├── impact.html
│   │   └── news.html
│   ├── resources/                # Resources pages
│   │   ├── business.html
│   │   ├── faqs.html
│   │   └── newsletter.html
│   └── errors/                   # Error pages
│       ├── 404.html
│       └── 500.html
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### 1. Clone and Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Run the Application

```bash
# Run Flask application
python app.py

# Access at: http://localhost:5000
```

## 📊 Complete Page List

### ✅ **All Pages Implemented** (No Placeholders)

**Main Pages:**
- Homepage (/) - Complete hero section, services overview, testimonials
- Contact (/contact) - Full contact form with validation

**Cuba Travel Programs:**
- People to People (/cuba-travel/people-to-people)
- Private Trips (/cuba-travel/private-trips)  
- Academic Programs (/cuba-travel/academic-programs)
- CET Luxury (/cuba-travel/cet-luxury)
- Corporate Travel (/cuba-travel/corporate-travel)
- Events in Cuba (/cuba-travel/events-in-cuba)

**About CET:**
- The CET Story (/about/the-cet-story)
- Our Impact (/about/impact)
- In the News (/about/in-the-news)
- Testimonials (/about/testimonials)

**Resources:**
- Business in Cuba (/resources/business-in-cuba)
- FAQs (/resources/faqs)
- The Newsletter (/resources/newsletter)

**Additional:**
- The Cuba Blog (/blog)
- 404 Error Page
- 500 Error Page

## 🎨 Design Features

### Improved Text Contrast
- **Body Text**: Dark charcoal (#333333) for excellent readability
- **Headings**: Dark blue-gray (#2c3e50) for clear hierarchy
- **Links**: Darker teal (#1e5f6f) for better visibility
- **WCAG Compliant**: Meets accessibility guidelines

### Cuban-Inspired Color Palette
```css
:root {
    --cuba-blue: #1b4d6b;
    --cuba-teal: #2b8ca3;
    --cuba-gold: #d4af37;
    --cuba-coral: #ff6b5b;
    --cuba-cream: #f8f5f0;
    --body-text: #333333;
    --heading-text: #2c3e50;
}
```

### Responsive Design
- Mobile-first Bootstrap 5 framework
- Professional typography with Inter font family
- Smooth animations and hover effects
- Card-based layouts with shadow effects

## 🔧 Key Components

### Flask Application (app.py)
- **Complete Routing**: All pages with proper URL structure
- **CSRF Protection**: Form security with Flask-WTF
- **Error Handling**: 404 and 500 error pages
- **Context Processors**: Global template variables
- **Form Validation**: Contact form processing

### Template System
- **Jinja2 Templates**: Modular, extensible design
- **Base Template**: Consistent navigation and footer
- **Component Reuse**: Cards, forms, buttons
- **SEO Ready**: Meta tags and semantic HTML

### Static Assets
- **Custom CSS**: Enhanced styling with Cuban theme
- **JavaScript**: Form validation and animations
- **Bootstrap 5**: Responsive framework
- **Font Awesome**: Professional icons

## 🚀 Deployment Options

### 1. Heroku Deployment

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set FLASK_ENV=production

# Deploy
git add .
git commit -m "Initial deployment"
git push heroku main
```

### 2. Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t cuba-educational-travel .
docker run -p 5000:5000 cuba-educational-travel
```

### 3. Traditional Server Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🔒 Security Features

- **CSRF Protection**: All forms protected against CSRF attacks
- **Input Validation**: Server-side form validation
- **SQL Injection Prevention**: Using parameterized queries (when database added)
- **XSS Protection**: Jinja2 auto-escaping enabled
- **Secure Headers**: Ready for production security middleware

## 🎯 Integration Ready

### Database Integration
```python
# Add to app.py for database support
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### Email Integration
```python
# Add email functionality
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
mail = Mail(app)

def send_contact_email(form_data):
    msg = Message('New Contact Form Submission',
                  recipients=[app.config['ADMIN_EMAIL']])
    msg.body = f"Name: {form_data['name']}\nMessage: {form_data['message']}"
    mail.send(msg)
```

### User Authentication
```python
# Add user system
from flask_login import LoginManager, UserMixin

login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
```

## 📝 Content Management

### Adding New Pages
1. Create template in appropriate directory
2. Add route in `app.py`
3. Update navigation in base template
4. Test all links and forms

### Updating Content
- Company information in `app.py` COMPANY_INFO
- Testimonials in `app.py` TESTIMONIALS
- FAQs in `app.py` FAQS
- Navigation structure in `app.py` NAVIGATION

## 🧪 Testing

```bash
# Run basic tests
python -c "import app; print('Flask app loads successfully')"

# Test all routes
python -c "
from app import app
with app.test_client() as client:
    routes = ['/', '/contact', '/about/the-cet-story']
    for route in routes:
        response = client.get(route)
        print(f'{route}: {response.status_code}')
"
```

## 📚 Additional Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Jinja2 Documentation**: https://jinja.palletsprojects.com/
- **Bootstrap 5 Documentation**: https://getbootstrap.com/docs/5.3/
- **Original Website**: https://cubaeducationaltravel.com/

## 🆘 Support

For questions about the Flask application:
1. Check this README for common issues
2. Review Flask documentation for framework questions
3. Examine the code comments for implementation details

## 📄 License

This project is created for educational and demonstration purposes.
