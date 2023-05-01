from faker import Faker


def build_custom_form_schema_request() -> dict:
    """
    Builds a custom form schema.
    returns:
        dict: custom form schema.
    """
    return {
        "name": f"{Faker().name()} form",
        "description": f"{Faker().sentence()}",
        "fields": [
            {
                "type": "text",
                "field_title": "First Name",
                "required": True,
                "rules": ["min:3", "max:10"],
            },
            {
                "type": "text",
                "field_title": "Last Name",
                "required": True,
                "rules": ["min:3", "max:10"],
            },
        ],
    }
