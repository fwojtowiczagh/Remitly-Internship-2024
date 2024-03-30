# Remitly-Internship-2024

Home exercise for Remitly - Summer Internship 2024. Script for verifying the input JSON data. Input data format is defined as AWS::IAM::Role Policy - definition and example ([AWS IAM Role JSON definition and example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html))

## Installation

1. Clone the repository:
```
git clone https://github.com/fwojtowiczagh/Remitly-Internship-2024.git
```

2. Open up the root folder and install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Place your input file (`input_file.txt`) in `data` folder or use already existing file.

2. Run the script in the terminal with the following command:
```
python run.py input.txt
```

Example:
```
python run.py valid_input.txt
```

## Testing

1. Run tests from root directory:
```
python -m tests.test_json_validator
```