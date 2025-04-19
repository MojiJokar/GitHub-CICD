"""
minimal example of how to use GitHub Actions secrets and workflow inputs in a Python script.
"""
secret_key = os.environ.get("SECRET_KEY")
import os

def main():
    # Access secrets and workflow inputs from environment variables
    api_key = os.environ.get("API_KEY")
    user_input = os.environ.get("INPUT_USER_INPUT")
    

    print(f"API_KEY: {api_key}")
    # print(f"SECRET_KEY: {secret_key}")
    print(f"Workflow Input: {user_input}")

if __name__ == "__main__":
    main()
