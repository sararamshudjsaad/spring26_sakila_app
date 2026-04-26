"""
config.py - Application configuration module.
Reads all settings from environment variables with sensible defaults.
See README.md for deployment-specific hostname configurations.
"""
# Author: Sara Haider
# Date: 2026-04-26
# Team Member: Ali Hassan
# Date: 2026-04-26
# Description: Updated database host, added timeout and health check settings

import os

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-in-production')