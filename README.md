# SRS Document Generator

## 🛠️ Tech Stack

- **Backend**: Google Cloud SDK
- **Database**: Google Cloud Firestore
- **Testing**: pytest, pytest-cov
- **Code Quality**: flake8, black
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Main CI/CD pipeline
├── src/                       # Source code
├── tests/                     # Tests (add your test files here)
├── requirements.txt          # All dependencies
└── pyproject.toml           # All configurations (pytest, flake8, black)
```

## 🔐 Secrets Required

Configure these secrets in GitHub repository settings:

- `GCP_SA_KEY`: Google Cloud service account key (JSON)
- `GCP_PROJECT_ID`: Google Cloud project ID
