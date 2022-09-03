from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.azure_storage import AzureStorage
import environ
env = environ.Env(DEBUG=(bool, False))


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "private"

class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "private"
    file_overwrite = False

# class AzureStaticStorage(AzureStorage):
#     account_name = "saperastaticstorage"
#     account_key = env("AZURE_KEY")
#     azure_container = "static"
#     expiration_secs = None
#
# class AzureMediaStorage(AzureStorage):
#     account_name = "saperastaticstorage"
#     account_key = env("AZURE_KEY")
#     azure_container = "media"
#     expiration_secs = None



