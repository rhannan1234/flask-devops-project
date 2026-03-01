markdown
# Flask DevOps Project 🚀

A simple Flask web application with Docker containerization and automated CI/CD pipeline using GitHub Actions.

## 📋 Project Overview

This project demonstrates a complete DevOps workflow:
- **Flask** - Python web framework
- **Docker** - Containerization
- **GitHub Actions** - CI/CD automation
- **Docker Hub** - Container registry

## 🏗️ Architecture
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ GitHub │────▶│GH Actions │────▶│ Docker Hub │
│ Repository │ │ CI/CD │ │ Registry │
└─────────────┘ └─────────────┘ └─────────────┘
│ │ │
│ git push │ build │ push
▼ ▼ ▼
Flask App Docker Image Container
(app.py) (Dockerfile) Registry

text

## ✨ Features

- **Simple Flask App**: "Hello DevOps World!" endpoint with health check
- **Docker Container**: Multi-stage build for smaller image size
- **Automated CI/CD**: Builds and pushes on every git push to main
- **Rootless Docker**: Secure container execution on NixOS
- **Health Check**: `/health` endpoint for monitoring

## 🛠️ Technologies Used

| Component | Technology |
|-----------|------------|
| Web Framework | Flask 2.3.3 |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| Version Control | Git/GitHub |
| OS | NixOS (with rootless Docker) |

## 📁 Project Structure
flask-devops-project/
├── app.py # Flask application
├── Dockerfile # Multi-stage Docker build
├── requirements.txt # Python dependencies
├── .github/
│ └── workflows/
│ └── docker-build.yml # GitHub Actions pipeline
└── README.md # This file

text

## 🚀 Getting Started

### Prerequisites

- Docker (rootless mode on NixOS)
- GitHub account
- Docker Hub account

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/rhannan1234/flask-devops-project.git
   cd flask-devops-project
Build the Docker image

bash
docker build -t flask-devops-app .
Run the container

bash
docker run -d -p 5000:5000 --name my-flask-app flask-devops-app
Test the application

bash
curl http://localhost:5000
curl http://localhost:5000/health
Clean up

bash
docker stop my-flask-app
docker rm my-flask-app
🔄 CI/CD Pipeline
The GitHub Actions workflow automatically:

Checks out code on push to main branch

Sets up Docker Buildx

Logs in to Docker Hub using secrets

Builds the Docker image

Pushes to Docker Hub with tags:

latest

sha-<commit-hash>

Required GitHub Secrets
Secret Name	Description
DOCKER_USERNAME	Your Docker Hub username
DOCKER_PASSWORD	Your Docker Hub Personal Access Token
🐳 Docker Configuration
Multi-stage Dockerfile
dockerfile
# Build stage
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Final stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
USER 1001
EXPOSE 5000
CMD ["python", "app.py"]
📊 API Endpoints
Endpoint	Method	Description	Response
/	GET	Main page	HTML with hostname info
/health	GET	Health check	{"status": "healthy"}
🧪 Testing
bash
# Test locally with curl
curl http://localhost:5000/health

# Expected response:
# {"status": "healthy", "message": "App is running smoothly!"}
📦 Docker Hub Image
The automated build pushes to:

text
docker pull rhannan1234/flask-devops-app:latest
🔧 NixOS Configuration (Rootless Docker)
If you're on NixOS like me, here's the config used:

nix
{
  virtualisation.docker = {
    enable = false;
    rootless = {
      enable = true;
      setSocketVariable = true;
    };
  };
}
📝 Environment Variables
Variable	Default	Description
FLASK_ENV	production	Flask environment
FLASK_APP	app.py	Flask entry point
🚦 CI/CD Status
https://github.com/rhannan1234/flask-devops-project/actions/workflows/docker-build.yml/badge.svg

📈 Future Improvements
Add unit tests with pytest

Implement blue-green deployment

Add monitoring with Prometheus

Deploy to Kubernetes

Add docker-compose for local dev

Implement caching in CI/CD

🤝 Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Open a Pull Request

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Flask documentation

Docker documentation

GitHub Actions documentation

NixOS community

📬 Contact
Project Link: https://github.com/rhannan1234/flask-devops-project

Built with ❤️ using NixOS, Docker, and GitHub Actions
