"""
this script is   a test to  acquire the message_id of customer saved in secrets ,Actions in GitHub
could be for  other  stuff  like   getting Authorization and permissin and etc  in Azure
"""
import os
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import SubscriptionClient

# MESSAGE_ID = os.environ.get("message_id")
# def main():
#     # Get message_id from environment variable
#     MESSAGE_ID = os.environ.get("message_id")
#     if not MESSAGE_ID:
#         print("Environment variable 'message_id' not set.")
#         return

#     print("GitHub Action test 1...")

#     # Authenticate using DefaultAzureCredential
#     credential = DefaultAzureCredential()
#     try:
#         # Initialize Azure Subscription client to check authorization
#         subscription_client = SubscriptionClient(credential)
#         subscriptions = list(subscription_client.subscriptions.list())
#         print(f"Authorized! Found {len(subscriptions)} subscriptions.")
#         for sub in subscriptions:
#             print(f"Subscription ID: {sub.subscription_id}, Display Name: {sub.display_name}")
#     except Exception as e:
#         print(f"Authorization failed: {e}")

# if __name__ == '__main__':
#     main()
