# Discord Web Scraping Bot

## Overview

This is a Discord bot designed to provide information about aircrafts using web scraping. The bot allows users to search for aircraft details directly within a Discord server.

## Features

- **Aircraft Search**: Users can search for aircraft information by typing a command.
- **Interactive Embeds**: The bot responds with rich embeds containing images and details.
- **Customizable**: Easily configurable via environment variables.

## Commands

### `$plane <aircraft_name>`
- **Description**: Fetches information about a specific aircraft.
- **Usage**: 
  ```
  $plane F-16
  ```
- **Example Response**:
  ![Example usage](/img/example_usage1.png)

## Setup

### Prerequisites
- Python 3.10 or higher
- Discord bot token
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/josue441/Web-scraping.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add the following:
   ```
   DISCORD_TOKEN=<your_discord_bot_token>
   DISCORD_CHANNEL_ID=<your_channel_id>
   ```

4. Run the bot:
   ```bash
   python bot/Discord_Bot.py
   ```

## File Structure

```
BOT/
├── bot/
│   ├── Discord_Bot.py       # Main bot logic
│   ├── scraping.py          # Web scraping logic
│   └── __pycache__/         # Compiled Python files
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
└── README.md                # Project documentation
```

## How It Works

1. The bot connects to Discord using the provided token.
2. Users can type `$plane <aircraft_name>` to search for aircraft details.
3. The bot scrapes the web for information and responds with an embed containing:
   - Aircraft name
   - Image
   - Additional details

## Example

![Bot Example](/img/example_usage2.png)

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!
