# Images Telegram Bot

A Telegram bot designed to interact with users, handle images, and provide various functionalities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Image Search**: Fetch images from Yandex.Search API based on user input.
- **Adjustable Delay**: Users can set a delay for sending images.
- **Help and Commands**: Provides help messages and command support.

## Installation

To install and run the bot locally, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/yourusername/cats-telegram-bot.git
cd cats-telegram-bot
```

### Configure the Environment

Create a .env file in the .env/ directory and add the necessary environment variables. Example:

```env
DEBUG=False
API_TOKEN = "YOUR TELEGRAM API" 
FOLDER_ID = "YOUR YANDEX SERVICE ACCOUNT" 
API_YANDEX = "YOUR YANDEX SEARCH API"
LOGGING_PATH="logs/log.log"
REDIS_HOST=redis
REDIS_PORT=6379
```

See Yandex.Search API docs at [Documentation Yandex Search API](https://yandex.cloud/en/docs/search-api/concepts/pic-search?utm_referrer=https%3A%2F%2Fyandex.ru%2F)

You need yandex.cloud account + service account(FOLDER_ID) + API(API_YANDEX).

## Configuration
### Setting Up the Bot
- Telegram Token: Obtain a bot token from BotFather and add it to your .env file.
- Yandex API Key: Get your API key from Yandex API and set it in the .env file.
- Folder ID: Set your folder ID in the .env file where images are stored.

## Usage
To start the bot, run the following command:

```bash
docker compose -f docker/docker-compose.yml up --build
```