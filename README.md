# Taskify  

Taskify is a simple Django-based to-do application with multi-user support. Each user can log in, manage their own tasks, and perform basic task operations such as adding, updating, and deleting tasks.  

## Features  

- **User Authentication** – Login and logout functionality.  
- **Multi-User Support** – Each user has their own separate tasks.  
- **Add Tasks** – Users can create new tasks by providing a task name.  
- **View Tasks** – Displays all tasks added by the logged-in user.  
- **Update Tasks** – Users can rename their tasks.  
- **Delete Tasks** – Remove tasks when no longer needed.  

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database)

## Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/iamshammas/Taskify.git
   ```  

2. **Navigate to the project directory**:  
   ```bash
   cd Taskify
   ```  

5. **Apply database migrations**:  
   ```bash
   python manage.py migrate  
   ```  

7. **Run the development server**:  
   ```bash
   python manage.py runserver  
   ```  

The application should now be running at `http://127.0.0.1:8000/`.  

## Usage  

1. **Register/Login** – New users can register, or existing users can log in.  
2. **Add a Task** – Enter a task name and save it.  
3. **View Tasks** – The dashboard shows all tasks for the logged-in user.  
4. **Update a Task** – Click on a task to rename it.  
5. **Delete a Task** – Remove tasks when they are no longer needed.  
6. **Logout** – Securely log out of your account.  

---

For more details, visit the [Taskify GitHub repository](https://github.com/iamshammas/Taskify).  
