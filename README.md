# DevOps Pipeline Setup with Jenkins, SonarQube, and Docker on AWS EC2 Instances

## Introduction

This guide provides step-by-step instructions to set up a DevOps pipeline on AWS using Jenkins for continuous integration, SonarQube for code quality analysis, and Docker for containerization. The pipeline is orchestrated on three EC2 instances.

### Prerequisites

1. **GitHub Repository:**
   - Create a GitHub repository to host your code.

2. **AWS Account:**
   - Set up an AWS account with the necessary permissions to create EC2 instances.

3. **SSH Key Pair:**
   - Generate an SSH key pair for securely connecting to the EC2 instances.

## Step 1: Create EC2 Instances

1. Launch three EC2 instances for Jenkins, SonarQube, and Docker.
2. Connect to each instance using the generated SSH key:
    ```bash
    chmod 400 YOUR-EC2-KEY.pem
    ssh -i YOUR-EC2-KEY.pem ubuntu@<INSTANCE-IP>
    ```

## Step 2: Jenkins Setup

### Install Java Runtime Environment on Jenkins Instance

```bash
sudo apt update
sudo apt install openjdk-11-jre
```

### Install Jenkins

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

### Verify Jenkins Installation

```bash
sudo systemctl status jenkins
```

### Access Jenkins

1. Get the EC2 instance's public IP address.
2. Access Jenkins using `http://<INSTANCE-IP>:8080/`.
3. Retrieve the Jenkins secret key from the instance.

### Create Jenkins Pipeline

1. Create a new pipeline in Jenkins.
2. Configure the pipeline with the GitHub repository link.
3. Set up a webhook for automatic triggering.

## Step 3: SonarQube Setup

### Install Java Runtime Environment on SonarQube Instance

```bash
sudo apt install openjdk-17-jre
```

### Install SonarQube

```bash
./sonar.sh console
```

### Configure SonarQube

1. Access SonarQube using `http://<SONARQUBE-INSTANCE-IP>:9000/`.
2. Generate a token for authentication.

## Step 4: Docker Setup

### Install Docker on Docker EC2 Instance

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Configure Docker

```bash
sudo usermod -aG docker $USER
docker --version
docker run hello-world
```

## Conclusion

Your DevOps pipeline with Jenkins, SonarQube, and Docker is now set up on AWS EC2 instances. Ensure to adapt the configurations according to your project requirements. For further details on integrating Jenkins, SonarQube, and Docker into your development workflow, refer to their official documentation.