# -*- coding: utf-8 -*-
{
    'name': "student_management",   

    'description': """
        Management of students record
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequ.xml',
        'views/views.xml',
        
    ],
    'installable': True,   
}
