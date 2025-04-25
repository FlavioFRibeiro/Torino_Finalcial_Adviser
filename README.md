# Torino Financial Advisor

## Overview
The Torino Financial Advisor is a real-time stock analysis application that leverages AI agents to provide insights and visualizations for investors. The application utilizes Yahoo Finance for data extraction and employs various plotting techniques to visualize stock performance.

## Project Structure
```
Torino_Financial_Advisor
├── analytics
│   ├── __init__.py
│   ├── data_extraction.py
│   ├── plot_utils.py
├── ai_agents
│   ├── __init__.py
│   ├── agents.py
├── web_app
│   ├── __init__.py
│   ├── app.py
│   ├── sidebar.py
├── main.py
└── README.md
```

## Installation
To set up the project, ensure you have Python installed on your machine. Then, clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the application using the following command:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to `http://localhost:8501` to access the Torino Financial Advisor interface.
3. Enter the stock ticker symbol in the input field and click on the "Analyze" button to fetch and visualize the stock data.

## Features
- **Data Extraction**: Fetches historical stock data from Yahoo Finance.
- **Visualizations**: Displays stock prices, candlestick charts, moving averages, and trading volume.
- **AI Agents**: Provides real-time analysis and recommendations using AI models.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
