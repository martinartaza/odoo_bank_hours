{
    'name': 'Bank Hours (Argentina)',
    'version': '17.0.1.0',
    'category': 'Human Resources',
    'summary': 'Time banking management for Argentina Labor Law (Free Version)',
    'countries': ['AR'],
    'description': open('README.rst', 'r', encoding='utf-8').read(),
    'author': 'Sebastian Martin, Artaza Saade',
    'website': 'https://www.sebastianartaza.com/bank_hours.html',
    'license': 'LGPL-3',
    'depends': ['hr_attendance', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_leave_type_data.xml',
        'views/res_config_settings_views.xml',
        'views/bank_hours_log_views.xml',
    ],
    'demo': [
        'data/bank_hours_demo.xml',
    ],
    'images': [
        'static/description/image001.png',
        'static/description/image002.png',
        'static/description/image003.png',
        'static/description/image004.png',
        'static/description/image005.png',
        'static/description/image006.png',
    ],
    'assets': {
        'web.assets_backend': [
            'bank_hours/static/src/js/bank_hours_tour.js',
        ],
    },
    'installable': True,
    'application': True,
    'maintainers': ['Sebastian Martin Artaza Saade'],
    'post_init_hook': 'post_init_hook',
}
