
# Swagger settings
swagger_conf = {
    'swagger': '2.0',
    'basePath': '/',
    'tags': [
        {
        'name': "Svátky",
        },
    ],
    'info': {
        'title': 'API pro české svátky',
        'version': '1.0.0',

        'description': 'Api poskytuje endpointy pro vyhledávání českých svátků podle různých parametrů. Pro používání není potřeba autentizace.<br>Source code [(Github)](https://github.com/david-bl/api-svatky).',
    },
    "license": {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    'components': {
        'schemas': {
            'user': {
                'type': 'object',
                'properties': {
                    'msg': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'data': {
                        'type': 'object',
                        'properties': {
                            '2024-01-01': {
                                'type': 'object',
                                'properties': {
                                    'date_format_cz': {
                                        'type': 'string',
                                        'description': 'Datum ve formátu DD. MM. YYYY',
                                        'example': '1. 1. 2024'
                                    },
                                    'date_format_iso': {
                                        'type': 'string',
                                        'description': 'Datum ve formátu YYYY-MM-DD',
                                        'example': '2024-01-01'
                                    },
                                    'date_name': {
                                        'type': 'string',
                                        'example': '1. Ledna'
                                    },
                                    'day_in_year': {
                                        'type': 'integer',
                                        'example': 1
                                    },
                                    'day_name': {
                                        'type': 'string',
                                        'example': 'Pondělí'
                                    },
                                    'names': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'string',
                                            'example': 'Jarmila'
                                        }
                                    },
                                    'timestamp': {
                                        'type': 'integer',
                                        'example': 1704063600
                                    },
                                    'week': {
                                        'type': 'integer',
                                        'example': 1
                                    },
                                }
                            }
                        }
                    }
                }
            },
        }
    }
}

# Swagger routes settings
swag_route_all = {
    'summary': 'Získání všechn záznamů',
    'description': 'Vrací všechny záznamy svátků v aktuálním roce.',
    'operationId': 'getAll',
    'produces': ['application/json'],
    'tags': ['Svátky'],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_today = {
    'summary': 'Dnešní svátek',
    'description': 'Vrací záznam pro dnešní den.',
    'operationId': 'getToday',
    'tags': ['Svátky'],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_name = {
    'summary': 'Podle jména',
    'description': 'Vrací záznamy na základě zadaného jména.',
    'operationId': 'getByName',
    'tags': ['Svátky'],
    'parameters': [
        {
            'name': 'name',
            'description': 'Hledané jméno',
            'in': 'path',
            'type': 'string',
            'required': True,
        }
    ],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_date = {
    'summary': 'Podle datumu',
    'description': 'Vrací záznamy na základě zadaného data. <strong>Podporované formáty [DD.MM.], [MM-DD], [YYYY-MM-DD]</strong>',
    'operationId': 'getByDate',
    'tags': ['Svátky'],
    'parameters': [
        {
            'name': 'date_format',
            'description': 'Hledané datum',
            'in': 'path',
            'type': 'string',
            'required': True,
        }
    ],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_day = {
    'summary': 'Podle dne v roce',
    'description': 'Vrací záznamy na základě zadaného dne v roce <strong>(1-366)</strong>.',
    'operationId': 'getByDay',
    'tags': ['Svátky'],
    'parameters': [
        {
            'name': 'day_number',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Den v roce',
            'minimum': 1,
            'maximum': 366,
        }
    ],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_week = {
    'summary': 'Podle týdne v roce',
    'description': 'Vrací záznamy na základě zadaného týdne v roce <strong>(1-53)</strong>.',
    'operationId': 'getByWeek',
    'tags': ['Svátky'],
    'parameters': [
        {
            'name': 'week_number',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Týden v roce',
            'minimum': 1,
            'maximum': 53,
        }
    ],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}

swag_route_month = {
    'summary': 'Podle měsíce v roce',
    'description': 'Vrací záznamy na základě zadaného měsíce v roce <strong>(1-12)</strong>.',
    'operationId': 'getByMonth',
    'tags': ['Svátky'],
    'parameters': [
        {
            'name': 'month_number',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Měsíc v roce',
            'minimum': 1,
            'maximum': 12,
        }
    ],
    'responses': {
        200: {
            'description': 'OK',
            'schema': { "$ref": "#/components/schemas/user" }
        },
    },
}
