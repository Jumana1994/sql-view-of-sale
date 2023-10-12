{
    'name': 'sale order details',
    "version": "16.0.1.0.0",
    'description': 'sale order details through sql view',
    'summary': 'sale order details through sql form view',
    "author": 'Cybrosys',
    'license': 'LGPL-3',
    'category': 'Sales',
    "depends": [
        "base",
        'sale',
    ],
    "data": [
        "security/ir.model.access.csv",
        'views/sale_order_details_view.xml',

    ],
    "auto-install": True,
    # "application": True,
    "installable": True,

}
