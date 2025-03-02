# AI Web Auditor 🤖

An AI-powered web testing platform that performs automated functional, performance, and security audits using Google Gemini, Selenium, Lighthouse, and OWASP ZAP.



## Features ✨

- **AI-Powered Testing**: Generate test cases using Google Gemini
- **Self-Healing Tests**: Automatic locator repair with Healenium
- **Performance Metrics**: Lighthouse integration for core web vitals
- **Security Scanning**: OWASP ZAP vulnerability detection
- **Real-Time Dashboard**: Live progress tracking and results display
- **Multi-Tool Reports**: Allure, Lighthouse, and ZAP reporting

## Prerequisites 📋

- Python 3.9+
- Node.js 16+
- Docker
- Google Chrome
- ChromeDriver
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

## Installation 🛠️

```bash
# Clone repository
git clone https://github.com/yourusername/ai-web-auditor.git
cd ai-web-auditor

# Create virtual environment
python -m venv venv

# Activate environment
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Lighthouse
npm install -g lighthouse

# Pull OWASP ZAP Docker image
docker pull owasp/zap2docker-stable
