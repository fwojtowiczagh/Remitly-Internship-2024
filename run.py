import argparse
from aws_iam_validator import validate_aws_iam_role_policy_resource


def main(input_file):
    is_validated_json = validate_aws_iam_role_policy_resource(input_file)
    print(is_validated_json)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate AWS::IAM::Role policy, Resource field")
    parser.add_argument("input_file", help="Name of input file")
    args = parser.parse_args()
    main(args.input_file)
