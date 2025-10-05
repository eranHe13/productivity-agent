# Productivity Agent

A comprehensive productivity management system that combines task management, focus tracking, and AI-powered coaching through both a REST API and Telegram bot interface.

## Overview

The Productivity Agent is designed to help users stay organized, focused, and motivated in their daily work. It provides a centralized platform for managing tasks, tracking focus sessions, setting daily goals, and receiving personalized coaching advice.

## Key Features

### 📋 Task Management
- Create, organize, and track tasks with completion status
- Categorize tasks for better organization
- Set due dates and track task creation timestamps
- Mark tasks as completed through the API or Telegram bot

### 🎯 Daily Goals
- Set and track daily objectives
- Monitor goal completion status
- Focus on daily productivity targets

### 🧘 Focus Sessions
- Start and stop focus sessions with different modes (25-minute Pomodoro, deep work)
- Track session duration and interruptions
- Monitor focus time patterns and productivity metrics

### 🤖 AI Coach
- Get personalized productivity advice and coaching
- Ask questions about time management, goal setting, and productivity strategies
- Powered by OpenAI's GPT models for intelligent, contextual responses
- Maintains conversation memory for better coaching continuity

### 📱 Telegram Bot Integration
- Access all features through a convenient Telegram interface
- Quick task management with simple commands
- Start/stop focus sessions directly from Telegram
- Get instant coaching advice on the go

### 🗂️ Category Management
- Organize tasks into custom categories
- Color-coded categorization system
- Easy category creation and management

## Architecture

The system consists of two main components:

- **Backend API**: FastAPI-based REST API providing core functionality
- **Telegram Bot**: Python bot that interfaces with the API for mobile access

The application uses SQLite for data persistence and integrates with OpenAI for AI coaching capabilities.
