import unittest
from aws_iam_validator import validate_aws_iam_role_policy_resource


class TestJsonValidator(unittest.TestCase):
    
    def test_validate_aws_iam_role_policy_resource_valid_input(self):
        input_file = 'valid_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertFalse(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_empty_input(self):
        input_file = 'empty_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_no_asterisk_input(self):
        input_file = 'no_asterisk_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_misspelled_input(self):
        input_file = 'misspelled_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_too_nested_input(self):
        input_file = 'too_nested_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_not_single_asterisk_input(self):
        input_file = 'not_single_asterisk_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_missing_field_input(self):
        input_file = 'missing_field_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)

    def test_validate_aws_iam_role_policy_resource_not_valid_json_input(self):
        input_file = 'not_valid_json_input.txt'
        is_validated_json = validate_aws_iam_role_policy_resource(input_file)
        self.assertTrue(is_validated_json)


if __name__ == '__main__':
    unittest.main()
