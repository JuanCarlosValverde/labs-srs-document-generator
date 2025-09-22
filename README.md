# SRS Document Generator


## 🛠️ Tech Stack

- **Backend**: Google ADK
- **Database**: Google Cloud Firestore
- **Testing**: pytest, pytest-cov
- **Code Quality**: flake8, black
- **Deployment**: Google Cloud Run
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Main CI/CD pipeline
├── src/                       # Source code
├── tests/                     # Tests (add your test files here)
├── requirements.txt          # All dependencies
├── pyproject.toml           # All configurations (pytest, flake8, black)
├── Dockerfile               # Container configuration
└── .dockerignore            # Docker ignore file
```

### **Manual Deploy**
```bash
# Build locally
docker build -t srs-document-generator .

# Run locally
docker run -p 8080:8080 srs-document-generator

# Test locally
curl http://localhost:8080
```