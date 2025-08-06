# Healthcare Management System API

A comprehensive Django REST API for managing healthcare operations including patient records, doctor information, and patient-doctor assignments.

## 🚀 Features

- **User Authentication**: JWT-based authentication system
- **Patient Management**: Complete CRUD operations for patient records
- **Doctor Management**: Full doctor profile management
- **Patient-Doctor Mapping**: Assign and manage doctor-patient relationships
- **RESTful API**: Clean, intuitive API endpoints
- **PostgreSQL Database**: Robust data storage
- **Environment Configuration**: Secure configuration management

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **API Framework**: Django REST Framework 3.16.0
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL 14
- **Environment**: Python 3.12
- **Configuration**: python-decouple

## 📋 Prerequisites

- Python 3.12+
- PostgreSQL 14+
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Healthcare
```

### 2. Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
cd healthcare_backend
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL
```bash
# Create PostgreSQL user (if not exists)
psql postgres -c "CREATE USER postgres WITH SUPERUSER PASSWORD 'postgres';"

# Create database
psql -U postgres -h localhost -c "CREATE DATABASE healthcare_db;"
```

### 5. Environment Configuration
Create a `.env` file in the `healthcare_backend` directory:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Settings
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/api/
```

### Authentication
All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

### 1. Authentication APIs

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### Login User
```http
POST /api/auth/login/
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. Patient Management APIs

#### Create Patient
```http
POST /api/patients/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30,
  "gender": "Male"
}
```

#### Get All Patients
```http
GET /api/patients/
Authorization: Bearer <token>
```

#### Get Patient by ID
```http
GET /api/patients/1/
Authorization: Bearer <token>
```

#### Update Patient
```http
PUT /api/patients/1/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "John Smith",
  "age": 31,
  "gender": "Male"
}
```

#### Delete Patient
```http
DELETE /api/patients/1/
Authorization: Bearer <token>
```

### 3. Doctor Management APIs

#### Create Doctor
```http
POST /api/doctors/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Dr. Jane Smith",
  "specialization": "Cardiology"
}
```

#### Get All Doctors
```http
GET /api/doctors/
Authorization: Bearer <token>
```

#### Get Doctor by ID
```http
GET /api/doctors/1/
Authorization: Bearer <token>
```

#### Update Doctor
```http
PUT /api/doctors/1/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Dr. Jane Smith",
  "specialization": "Neurology"
}
```

#### Delete Doctor
```http
DELETE /api/doctors/1/
Authorization: Bearer <token>
```

### 4. Patient-Doctor Mapping APIs

#### Assign Doctor to Patient
```http
POST /api/mappings/
Authorization: Bearer <token>
Content-Type: application/json

{
  "patient": 1,
  "doctor": 1
}
```

#### Get All Mappings
```http
GET /api/mappings/
Authorization: Bearer <token>
```

#### Get Mappings for Specific Patient
```http
GET /api/mappings/1/
Authorization: Bearer <token>
```

#### Remove Doctor from Patient
```http
DELETE /api/mappings/delete/1/
Authorization: Bearer <token>
```

## 🗄️ Database Schema

### User Model
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password`: Hashed password
- `is_active`: Account status
- `date_joined`: Registration date

### Patient Model
- `id`: Primary key
- `name`: Patient's full name
- `age`: Patient's age
- `gender`: Patient's gender
- `created_by`: User who created the record
- `created_at`: Record creation timestamp

### Doctor Model
- `id`: Primary key
- `name`: Doctor's full name
- `specialization`: Medical specialization
- `created_by`: User who created the record
- `created_at`: Record creation timestamp

### PatientDoctorMapping Model
- `id`: Primary key
- `patient`: Foreign key to Patient
- `doctor`: Foreign key to Doctor
- `assigned_at`: Assignment timestamp

## 🔧 Configuration

### Django Settings
- **Database**: PostgreSQL with environment variables
- **Authentication**: JWT tokens
- **Permissions**: IsAuthenticated by default
- **CORS**: Configured for development

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `DB_NAME`: PostgreSQL database name
- `DB_USER`: PostgreSQL username
- `DB_PASSWORD`: PostgreSQL password
- `DB_HOST`: PostgreSQL host
- `DB_PORT`: PostgreSQL port

## 🧪 Testing

### Manual Testing
Use curl or any API client to test endpoints:

```bash
# Register a user
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'

# Login and get token
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "testpass123"}'

# Use token for authenticated requests
curl -X GET http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <your-token-here>"
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False` in environment
- [ ] Use strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Set up proper CORS settings
- [ ] Configure static files
- [ ] Set up SSL/TLS certificates
- [ ] Configure logging
- [ ] Set up monitoring

### Docker Deployment (Optional)
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the Django documentation


**Built with ❤️ using Django and Django REST Framework** 