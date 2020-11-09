from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "price": {
            "type": "string",
            "pattern": "^[0-9,]+"
        }
    },
    "required": ["name", "price"]
}

validate({
    'name': 'ぶどう',
    'price': '3,000'
}, schema)

validate({
    'name': 'ぶどう',
    'price': '無料'
}, schema)
