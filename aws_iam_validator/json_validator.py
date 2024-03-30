import os
import json
from jsonschema import validate, exceptions


AWS_IAM_ROLE_POLICY_SCHEMA = {
    "type": "object",
    "properties": {
        "PolicyName": {"type": "string"},
        "PolicyDocument": {
            "type": "object",
            "properties": {
                "Statement": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Resource": {"type": "string", "enum": ["*"]}
                            
                        },
                        "required": ["Resource"]
                    }
                }
            },
            "required": ["Statement"]
        }
    },
    "required": ["PolicyDocument"]
}


def validate_aws_iam_role_policy_resource(file: str, schema: dict = AWS_IAM_ROLE_POLICY_SCHEMA) -> bool:
    data_path = "data"
    folder_path = os.path.abspath(data_path)
    input_dir = os.path.join(folder_path, file)

    json_data = None

    with open(input_dir) as f:
        try:
            json_data = json.load(f)
        except json.JSONDecodeError:
            return True

    if not json_data:
        return True
        
    try: 
        validate(instance=json_data, schema=schema)
        return False
    except exceptions.ValidationError:
        return True
