# AI Web Auditor 🤖

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)

Automated website testing platform combining AI-powered test generation (Google Gemini), functional testing (Selenium), performance analysis (Lighthouse), and security scanning (OWASP ZAP).

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker
- Google Chrome
- [Gemini API Key](https://aistudio.google.com/app/apikey)

### Installation
```bash
# Clone & setup
git clone https://github.com/JANARTHANANPALANIVEL/ai-web-auditor.git
cd ai-web-auditor
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
npm install -g lighthouse
docker pull owasp/zap2docker-stable

# Start ZAP proxy
docker run -d -p 8080:8080 -i owasp/zap2docker-stable zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.disablekey=true

# Configure environment
echo "GEMINI_API_KEY=your_key_here" > .env
echo "SELENIUM_DRIVER_PATH=$(which chromedriver)" >> .env
Here's a concise, single-file README.md for your project:

```markdown

### Usage
```bash
# Run application
python app.py

# Access UI at http://localhost:5000
# Example API call:
curl -X POST -d "url=https://example.com" http://localhost:5000/start-audit
```
### Usage
```bash
# Run application
python app.py

# Access UI at http://localhost:5000
# Example API call:
curl -X POST -d "url=https://example.com" http://localhost:5000/start-audit
```

## 📊 Features
| Component          | Technology Stack      |
|--------------------|-----------------------|
| AI Test Generation | Google Gemini         |
| Functional Testing | Selenium + Healenium  |
| Performance Audit  | Lighthouse            |
| Security Scanning  | OWASP ZAP             |
| Reporting          | Allure + JSON exports |

## 🔧 Configuration
```env
# .env file
GEMINI_API_KEY=your_api_key
SELENIUM_DRIVER_PATH=/path/to/chromedriver
ZAP_PROXY=http://localhost:8080
ALLURE_DIR=reports/
```

## 📍Troubleshooting
**1. ChromeDriver Issues**
```bash
export PATH=$PATH:/path/to/chromedriver
chromedriver --version  # Verify installation
```

**2. ZAP Connection Problems**
```bash
docker ps  # Check running containers
curl http://localhost:8080/JSON/core/view/version/
```

**3. Gemini API Errors**
```bash
python -c "import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); print(genai.list_models())"
```

## 📂 Generated Reports
```bash
# View reports
allure serve reports/  # Functional tests
cat reports/lighthouse_report.json  # Performance metrics
cat reports/zap_report.json  # Security findings
```

## 📜 License


---
