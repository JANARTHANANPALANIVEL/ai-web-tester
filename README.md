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
