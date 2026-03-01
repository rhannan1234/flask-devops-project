# Flask DevOps Project

A demonstration of modern DevOps practices including containerization, CI/CD automation, and infrastructure as code.

## 🛠️ Technologies

- **Application**: Python/Flask
- **Containerization**: Docker (multi-stage builds)
- **CI/CD**: GitHub Actions
- **Registry**: Docker Hub
- **Infrastructure as Code**: Dockerfile, GitHub Actions workflows

## 🔄 CI/CD Pipeline

On every push to main branch:
- Automated build of multi-stage Docker image
- Semantic versioning with commit hash tags
- Secure push to Docker Hub using GitHub Secrets
- Layer caching for optimized build times

## 📊 What This Demonstrates

| Skill | Implementation |
|-------|----------------|
| **Containerization** | Multi-stage builds, non-root user, slim base images |
| **CI/CD** | Automated pipelines, secret management, caching |
| **Security** | Rootless Docker, no sensitive data in images |
| **IaC** | Version-controlled infrastructure configs |

## 🛡️ Security Features

- Non-root user in containers
- Rootless Docker configuration
- Minimal base images
- Secrets managed via CI/CD variables

## 📁 Project Structure

├── app.py # Flask application
├── Dockerfile # Multi-stage build config
├── requirements.txt # Python dependencies
└── .github/workflows/
└── docker-build.yml # CI/CD pipeline

## 🚀 Key Endpoints

- `GET /` - Returns app info with hostname
- `GET /health` - Health check endpoint

## 💡 Why This Matters

This foundation scales to microservices, orchestration (Kubernetes), and cloud deployments. It demonstrates automation-first thinking, security awareness, and infrastructure as code principles.

---

*Built to showcase DevOps best practices for production-ready applications.*
