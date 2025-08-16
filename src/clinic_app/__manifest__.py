{
    'name': "Clinic Management",
    'summary': "Manage patients, doctors, appointments, prescriptions",
    'description': "Clinic Management App",
    'author': "Jamoliddin aka",
    'category': 'Clinic',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/treatment_views.xml',
        'views/diagnosis_views.xml',
        'views/medicine_views.xml',
        'views/prescription_views.xml',
    ],

    'installable': True,
    'application': True,
}
