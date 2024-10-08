# blogcategory
This is a Django-based blog application that allows users to classified the blogs by there category blog posts. The project is set up to run on a virtual environment.

# Requirements
Before starting, make sure you have the following installed:

Python (version 3.x)
pip (Python package manager)
Django (latest version)
Virtualenv

# Installation
Follow these steps to get the project running on your local machine.

# 1. Clone the repository

git clone <your-repository-url>

# 2. Navigate to the project directory

cd blog_project

# 3. Create a virtual environment
To isolate dependencies for this project, it's recommended to use a virtual environment.

python -m venv connectfd

# 4. Activate the virtual environment
For Windows:

connectfd\Scripts\activate

For macOS/Linux:

source connectfd/bin/activate


# 5. Install required dependencies
Install the necessary Python packages specified in the requirements.txt file:

pip install -r requirements.txt


If a requirements.txt file is not provided, ensure that at least the following dependencies are installed:

pip install Django


# 6. Apply database migrations
Run the following command to apply the necessary migrations to the database:

python manage.py migrate


# 7. Run the development server
Now, you can start the development server by running the following command:

python manage.py runserver


# 8. Open the application
Once the server is running, open your web browser and go to:

http://127.0.0.1:8000/blogs/
