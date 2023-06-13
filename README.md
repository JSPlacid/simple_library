# Simple Library Project
A simple library management system built with Django.
simple library is home for scholars and readers, where patrons can browse and read books that interest them.

## Table of Contents
- [Introduction](introduction)
- Installation
- Usage
- Features
- Configuration
- Contributing
- Testing
- License
- Credits
- Support and Contact
- [Authors](Authors)

## Introduction
The Simple Library Project is a web-based application that helps manage a library's books, authors, and library members. It provides a user-friendly interface for librarians to perform various tasks, including adding, editing, delete books and authors, manage library members and handling book borrowing and returning.

Key features of the Django Simple Library Project:

- Book management: Add, edit, and delete books with details such as title, author, publication date, and ISBN.
- Author management: Add, edit, and delete authors with information such as name and biography.
- Library member management: Manage library members and their borrowing history.
- Book borrowing: Allow library members to borrow and return books.
This project aims to implement a straightforward solution for small libraries or personal book collections.

## Installation
To install and set up the Django Simple Library Project, follow these steps:

1 Clone the repository:
from your command line or terminal
```
git clone https://github.com/JSPlacid/simple_library.git
```
2. Navigate to the project directory:
from your command line or terminal

`cd simple_library`
3. Create a virtual environment:
from your command line or terminal
```
pipenv venv
or
mkdir virtualenv
```

4. Activate the virtual environment:
On Windows:
`venv\Scripts\activate`

On macOS/Linux:
`source venv/bin/activate`

5. Install the dependencies:
`pip install -r requirements.txt`

6. Run database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
n.b: python3 manage.py for macOS

7. Start the development server:
`python manage.py runserver 8080`

8. Access the application at http://localhost:8080 in your browser.

## Usage
Once the Simple Library Project is set up, follow these steps to use it:

1. Create an admin user:
`python manage.py createsuperuser`

2. Log in to the admin dashboard at http://localhost:8000/admin using the created admin credentials.

3. From the admin dashboard, you can perform the following actions:
   - Manage Books: Add, edit, and delete books. Enter details such as title, author, publication date, and ISBN.
   - Manage Authors: Add, edit, and delete authors. Provide information such as name and biography.
   - Manage Library Members: Add, edit, and delete library members. Keep track of their borrowing history.

## Features
The Django Simple Library Project offers the following features:

- Book Management:
   - Add, edit, and delete books with attributes such as title, author, publication date, and ISBN.
- Author Management:
   - Add, edit, and delete authors with details like name and biography.
- Library Member Management:
   - Add, edit, and delete library members. Track their borrowing history.
- Book Borrowing:
   - Allow library members to borrow and return books.

## Configuration
The simple Library Project uses the default Django settings. If you need to customize any settings, modify the `settings.py` file located in the project's root directory. Refer to the Django documentation for more information on configuration options.

## Contributing
Contributions to the Simple Library Project are welcome!  To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch on your forked repository: git push origin feature-name.
5. Submit a pull request describing your changes.
Please follow the coding style and conventions already established in the project.

## Testing
the catalog/test/ directory contains all test modules implemented in the project.
To run the test suite for the Django Simple Library Project, execute the following command:

`python manage.py test`
You can also contribute to the test suite by adding new test cases or improving existing ones. Make sure to run the tests and ensure they pass before submitting a pull request.

## License
This project is licensed under the MIT License.
Public domain.

## Credits
The Simple Library Project utilizes the following technologies:

- Django: The web framework used to build the application.
- Python: The programming language in which the  project is developed.
- mysqlite3: The database tool used for storing and quering data in development stage.
- postgresql: to host databases in production for interacting with project.
- APIs and web services: enables communications and data exchange between different software systems.

## Support and Contact
For any questions, issues, or support related to the Django Simple Library Project, please contact the project maintainer at ojoolusegun17@gmail.com. You can also open an issue on the project's GitHub repository for bug reports or feature requests.

## Authors
Olusegun Ojo - [Github](github.com/JSPlacid)