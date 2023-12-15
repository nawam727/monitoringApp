import boto3

def create_ecr_repository(repository_name):
    # Create an ECR client
    ecr_client = boto3.client('ecr', region_name='us-east-1')

    # Create ECR repository
    response = ecr_client.create_repository(repositoryName=repository_name)

    # Display the repository URI and other information
    repository_uri = response['repository']['repositoryUri']
    repository_name = response['repository']['repositoryName']
    repository_uri = response['repository']['repositoryUri']
    created_at = response['repository']['createdAt']

    print(f"ECR repository '{repository_name}' created successfully.")
    print(f"Repository URI: {repository_uri}")
    print(f"Created at: {created_at}")

if __name__ == "__main__":
    repository_name = "monitoring-app"

    # Call the function to create the ECR repository
    create_ecr_repository(repository_name)
