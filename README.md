# Torino_Finalcial_Adviser
This is the Script for Torino, the AI Agente Financial Advisor :)

## Overview
The Torino Financial Advisor is a real-time stock analysis application that leverages AI agents to provide insights and visualizations for investors. The application utilizes Yahoo Finance for data extraction and employs various plotting techniques to visualize stock performance..

===========================================================================================================================================
## How to Run it
It runs locally, (because I don't want to spend too much money on cloud haha).

You will need to have a Groq API Key (you can find more info here -> https://groq.com/) - add it on your .env file as GROQ_API_KEY = "your_key"

In order to run it, follow the below steps:

1- Open the terminal, go to your local folder, where you cloned this repository.

2- Create the environment and install the requirements.

    #Creates the Env
    conda create --name deployai python=3.12
    #Activates the Env.
    conda activate deployai
    #Install all the required libs
    pip install -r requirements.txt 
    
3- Run the app locally and get all the info you want!

    streamlit run main.py

============================================================================================================================================
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
============================================================================================================================================
## Features
- **Data Extraction**: Fetches historical stock data from Yahoo Finance.
- **Visualizations**: Displays stock prices, candlestick charts, moving averages, and trading volume.
- **AI Agents**: Provides real-time analysis and recommendations using AI models.
