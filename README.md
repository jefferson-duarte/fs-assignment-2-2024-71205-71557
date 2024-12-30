# Project: Nutrition Management System

This project is a full-stack application with a Django-based back-end and a Vue.js front-end, allowing users and nutritionists to manage profiles, appointments, and health-related data.

---

## **Getting Started**

Follow the steps below to set up and run the project locally.

### **Prerequisites**

Make sure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv
- Node.js and npm

---
## **Back-end (Django)**

### **Installation Steps**

#### 1. Clone the Repository
```bash
git clone https://github.com/jefferson-duarte/fs-assignment-2-2024-71205-71557
cd backend
```

#### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure the Database

```
- The database we are using is SQLite, it is created automatic when run the step 5.
```

#### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

#### 7. Run the Development Server
```bash
python manage.py runserver
```

---

## **Front-end (Vue.js)**

### **Installation Steps**

#### 1. Navigate to the Front-end Directory
If the front-end code is in a separate directory, navigate to it:
```bash
cd frontend
```

#### 2. Install Dependencies
```bash
npm install
```

#### 3. Run the Development Server
```bash
npm run serve
```

The application will be available at:
```
http://localhost:8080
```

---

## **Accessing the Application**

- Back-end: `http://127.0.0.1:8000`
- Front-end: `http://localhost:8080` - the application is running here.

---

## **Project Structure**

```
fs-assignment-2-2024-71205-71557/
├── backend/
│   ├── authentication/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── auth_jwt.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── core/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── manage.py
│   ├── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   │   ├── styles/
│   │   │   │   ├── global.css
│   │   ├── components/
│   │   │   ├── NavBar.vue
│   │   ├── router/
│   │   │   ├── router.js
│   │   ├── views/
│   │   │   ├── AvailableNutritionists.vue
│   │   │   ├── ClientsNutritionist.vue
│   │   │   ├── DashboardPage.vue
│   │   │   ├── LoginPage.vue
│   │   │   ├── MainPage.vue
│   │   │   ├── NutritionistRegister.vue
│   │   │   ├── UserRegister.vue
│   │   ├── App.vue
│   │   ├── axios.js
│   │   ├── main.js
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package.json
│   ├── package-lock.json
│   ├── vue.config.js
```

---

## **Acknowledgments**

- [Django Documentation](https://docs.djangoproject.com/)
- [Vue.js Documentation](https://vuejs.org/)

