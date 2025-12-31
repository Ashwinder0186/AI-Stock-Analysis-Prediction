
import os
import phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

load_dotenv()

# Set PHI API Key for Playground
phi.api = os.getenv("PHI_API_KEY")


# Stock Analysis Agent
stock_analyzer = Agent(
    name="Stock Analysis Agent",
    role="Provide comprehensive stock analysis with trend predictions",
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
        "Always include sources for web searches with dates",
        "Use tables to display financial data clearly",
        "Analyze historical trends and patterns",
        "Provide data-driven predictions with reasoning",
        "Be specific with numbers and percentages",
        """
        For each stock analysis, provide:
        
        KEY METRICS (in table):
        - Current price & day change
        - Market cap & P/E ratio
        - 52-week range
        - Analyst consensus rating
        
        TREND ANALYSIS:
        - Recent performance (1 month, 3 months, 6 months)
        - Current trend direction
        - Key support/resistance levels
        
        IMPORTANT NEWS:
        - Top 2-3 major recent developments (with sources)
        - Overall market sentiment
        
        WHAT MATTERS:
        - Key strengths and concerns
        - Main catalysts affecting price
        - Analyst price targets
        
        FUTURE PREDICTION:
        
        SHORT-TERM (1-3 months):
        - Expected price movement and range
        - Confidence level: High/Medium/Low
        - What to watch for
        
        LONG-TERM (6-12 months):
        - Target price range
        - Growth potential
        - Major risks and opportunities
        
        RECOMMENDATION:
        - Buy/Hold/Sell with clear reasoning
        - Entry price suggestion
        - Risk level
        - Who should invest
        
        Keep it focused on what really matters for investment decisions.
        """
    ],
    show_tool_calls=True,
    markdown=True,
)


# Create Playground App
app = Playground(agents=[stock_analyzer]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)