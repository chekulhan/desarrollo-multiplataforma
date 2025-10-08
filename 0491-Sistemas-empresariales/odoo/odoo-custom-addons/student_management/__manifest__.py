{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage Students',
    'sequence': -100,
    'description': """Student Management System""",
    'category': 'Education',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],  # optional
}