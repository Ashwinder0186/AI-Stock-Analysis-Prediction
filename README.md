# 📊 AI Stock Analysis & Prediction

An intelligent stock analysis tool powered by AI that provides comprehensive market analysis, trend predictions, and investment recommendations.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- 📈 **Real-time Stock Data** - Get current price, market cap, P/E ratio, and more
- 📊 **Historical Trend Analysis** - View performance over 1, 3, and 6 months
- 📰 **Latest News Integration** - Stay updated with recent developments and market sentiment
- 🔮 **AI-Powered Predictions** - Short-term (1-3 months) and long-term (6-12 months) forecasts
- 💡 **Investment Recommendations** - Clear Buy/Hold/Sell signals with reasoning
- 🎨 **Beautiful UI** - Clean, intuitive Streamlit interface
- ⚡ **Live Streaming** - Watch analysis generate in real-time

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq (Llama 3.3 70B)
- **Data Sources**: 
  - YFinance (Stock data)
  - DuckDuckGo (News & web search)
- **Framework**: Phidata Agent Framework

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get it free here](https://console.groq.com))

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/stock-analysis-ai.git
cd stock-analysis-ai
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Usage

1. **Run the application**
```bash
streamlit run app.py
```

Or:
```bash
python -m streamlit run app.py
```

2. **Open your browser**

Navigate to `http://localhost:8501`

3. **Analyze stocks**
   - Enter a stock ticker (e.g., NVDA, AAPL, TSLA)
   - Click "Analyze Stock" or press Enter
   - Or use quick select buttons for popular stocks

## 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
phidata>=2.0.0
groq>=0.4.0
yfinance>=0.2.0
duckduckgo-search>=3.9.0
python-dotenv>=1.0.0
```

## 🎯 What You Get

### Analysis Includes:

1. **Key Metrics Table**
   - Current price & day change
   - Market cap & P/E ratio
   - 52-week range
   - Volume analysis

2. **Trend Analysis**
   - Performance over 1, 3, and 6 months
   - Trend direction identification
   - Support and resistance levels

3. **Latest News**
   - Top recent developments
   - Sources with dates
   - Market sentiment analysis

4. **Analyst Insights**
   - Price targets
   - Buy/Hold/Sell ratings
   - Recent rating changes

5. **AI Predictions**
   - **Short-term (1-3 months)**: Expected price range with confidence level
   - **Long-term (6-12 months)**: Target price and growth potential

6. **Investment Recommendation**
   - Clear Buy/Hold/Sell verdict
   - Detailed reasoning
   - Risk assessment
   - Suitable investor profile

## 📸 Screenshots

### Main Interface
![Main Interface](main.png)

### Analysis Example
![Analysis](use1.png)

## 🔑 API Keys

### Get Your Free Groq API Key:

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to API Keys
4. Create a new API key
5. Copy and paste into your `.env` file

**Free Tier Limits:**
- 12,000 tokens per minute
- Perfect for personal use

## ⚠️ Important Notes

- **Rate Limits**: Free tier has request limits. Wait 60 seconds between analyses if you hit the limit.
- **Data Accuracy**: Stock data is for informational purposes only. Not financial advice.
- **Market Hours**: Best results during market hours for real-time data.

## 🐛 Troubleshooting

### "Streamlit not recognized"
```bash
python -m pip install streamlit
python -m streamlit run app.py
```

### "Rate limit exceeded"
- Wait 60 seconds and try again
- Or upgrade to Groq paid tier

### "Error loading stock data"
- Check your internet connection
- Verify the ticker symbol is correct
- Some stocks may not be available in YFinance

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Phidata](https://phidata.com) - Agent framework
- [Groq](https://groq.com) - Fast AI inference
- [Streamlit](https://streamlit.io) - Web framework
- [YFinance](https://pypi.org/project/yfinance/) - Stock data
- [DuckDuckGo](https://duckduckgo.com) - Search API

## ⭐ Star History

If you find this project useful, please consider giving it a star!

## 📧 Contact

Your Name - [@Ashwinder Singh](https://github.com/Ashwinder0186/)

Project Link: [https://github.com/Ashwinder0186/AI-Stock-Analysis-Prediction](https://github.com/Ashwinder0186/AI-Stock-Analysis-Prediction)

---
