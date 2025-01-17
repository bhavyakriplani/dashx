# Uptime Monitor with Discord Notifications

## Project Overview

This project is a simple service that monitors website availability and sends notifications through Discord webhooks when a site goes down or recovers.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Guide](#setup-guide)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Bonus Features](#bonus-features)
- [Design Decisions](#design-decisions)

## Features

- **Website Monitoring**: Add and remove websites to monitor.
- **HTTP Requests**: Check website status periodically.
- **Track History**: Log uptime/downtime history.
- **Discord Integration**: Send notifications when a site goes down or recovers.
- **Basic Features**:
  - Endpoint to add/remove websites to monitor.
  - Store website check interval (default: 5 minutes).
  - Track uptime/downtime history.

## Setup Guide

### Prerequisites

- **Python 3.8+**
- **pip**

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/bhavyakriplani/dashx
   cd your-repository

python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

uvicorn app.main:app --reload


POST/sites/
Request Body
{
  "url": "https://example.com",
  "check_interval_seconds": 300,
  "name": "My Website",
  "expected_status_code": 200
}


}
DELETE /sites/{id}: Remove site from monitoring.

GET /sites/: List all monitored sites.

GET /sites/{id}/history: Get status history for a site.

POST /webhook/{site_id}: Configure Discord webhook.

Query Parameter: webhook_url

Database Schema
Tables
sites:

id: INTEGER PRIMARY KEY

url: VARCHAR

check_interval_seconds: INTEGER DEFAULT 300

name: VARCHAR

expected_status_code: INTEGER DEFAULT 200

webhook_url: VARCHAR

site_status_history:

id: INTEGER PRIMARY KEY

site_id: INTEGER

status: VARCHAR

response_time_ms: INTEGER

last_checked: DATETIME

last_status_change: DATETIME

Testing
Run Tests
Write Tests: Include tests for core monitoring logic and Discord notifications.

Run Tests:
pytest

Bonus Features
Multiple Discord Webhooks: Different channels for different sites.

Basic Authentication: For API endpoints.

Retry Logic: For failed checks before alerting.

Design Decisions
Framework: FastAPI for building the API.

Database: SQLite for data persistence.

HTTP Requests: requests library for HTTP requests.

Background Tasks: Asyncio for handling background tasks.

Notifications: Discord webhooks for real-time alerts.

