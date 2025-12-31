import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

# Page config
st.set_page_config(
    page_title="Stock Analysis AI",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)


# Initialize agent 
@st.cache_resource
def get_agent():
    return Agent(
        name="Stock Analysis Agent",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
                historical_prices=True,
            ),
            DuckDuckGo(),
        ],
        instructions=[
            "Use tables for financial data",
            "Include sources with dates",
            "Analyze trends and provide predictions",
            "Be specific with numbers",
            "Provide: Key metrics, trend analysis, news, short-term (1-3 mo) and long-term (6-12 mo) predictions, and Buy/Hold/Sell recommendation"
        ],
        show_tool_calls=False,
        markdown=True,
    )


def main():
    # Header
    st.title("📊 AI Stock Analysis & Prediction")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown("**Powered by:**")
        st.markdown("- 🤖 Groq AI (Llama 3.3)")
        st.markdown("- 📈 YFinance")
        st.markdown("- 🔍 DuckDuckGo")
        
        st.markdown("---")
        
        st.markdown("### 📝 Popular Stocks")
        popular_stocks = ["NVDA", "AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "META", "AMD"]
        
        cols = st.columns(2)
        for idx, stock in enumerate(popular_stocks):
            with cols[idx % 2]:
                if st.button(stock, key=f"btn_{stock}"):
                    st.session_state.ticker = stock
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.info("This AI-powered tool provides comprehensive stock analysis including current metrics, trends, news, and future predictions.")
    
    # Main content
    col1, col2 = st.columns([3, 1])
    
    with col1:
        ticker_input = st.text_input(
            "Enter Stock Ticker Symbol",
            value=st.session_state.get('ticker', ''),
            placeholder="e.g., NVDA, AAPL, TSLA",
            key="ticker_input"
        ).upper()
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("🔍 Analyze Stock", type="primary")
    
    # Analysis section
    if analyze_button or (ticker_input and ticker_input != st.session_state.get('last_analyzed', '')):
        if ticker_input:
            st.session_state.last_analyzed = ticker_input
            
            # Show loading
            with st.spinner(f"🔄 Analyzing {ticker_input}... This may take 30-60 seconds..."):
                try:
                    agent = get_agent()
                    
                    # Create placeholder for streaming response
                    response_placeholder = st.empty()
                    full_response = ""
                    
                    # Shorter, more focused prompt
                    prompt = f"""Analyze {ticker_input}:
1. Key metrics (table): price, change, market cap, P/E, 52-week range
2. Recent trend (1mo, 3mo, 6mo performance)
3. Top 2 news items with sources
4. Analyst targets
5. SHORT-TERM prediction (1-3 months): price range, confidence
6. LONG-TERM prediction (6-12 months): target, risks
7. RECOMMENDATION: Buy/Hold/Sell with reasoning"""
                    
                    # Get response
                    for response in agent.run(prompt, stream=True):
                        if hasattr(response, 'content') and response.content:
                            full_response += response.content
                            response_placeholder.markdown(full_response)
                    
                    # Success message
                    st.success(f"✅ Analysis complete for {ticker_input}!")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    if "rate_limit" in str(e).lower() or "413" in str(e):
                        st.warning("⚠️ Request too large. Try again in a moment or upgrade your Groq plan.")
                    else:
                        st.info("Please check your GROQ_API_KEY in .env file")
        else:
            st.warning("⚠️ Please enter a stock ticker symbol")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "💡 Tip: Analysis includes key metrics, trends, news, and AI-powered predictions"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    # Initialize session state
    if 'ticker' not in st.session_state:
        st.session_state.ticker = ''
    if 'last_analyzed' not in st.session_state:
        st.session_state.last_analyzed = ''
    
    main()