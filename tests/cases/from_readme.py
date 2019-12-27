from jsonschema_typed.types import JSONSchema

data: JSONSchema["schema/readme_example.json"] = {"title": "baz"}
reveal_type(data)
data["description"] = "there is no description"
data["awesome"] = 42
data["awesome"] = None
