{
    'name': 'indufix_custom',
    'version': '1.0',
    'description': 'Training module for Odoo',
    'summary': 'Training module for Odoo',
    'author': 'Guilherme',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/meu_primeiro_modelo_views.xml',
        'views/estate_property_views.xml',
    ],
    # 'application': True,  # Adiciona esta linha para indicar que é uma aplicação web
    # 'installable': True,
    # 'auto_install': False,
    # 'qweb': [],
    # 'route': '/api/bitrix/',  # Adiciona esta linha para definir a rota da sua API
}
