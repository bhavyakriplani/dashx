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
- [License](#license)

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
