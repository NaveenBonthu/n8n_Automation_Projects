# AI Email Triage & Summary System

An AI-powered automation workflow that processes incoming emails, classifies them, and stores structured data.

## Features
- Reads emails from Gmail
- Cleans and prepares email content
- Uses AI (Gemini) to classify:
  - Urgent
  - Follow-up
  - FYI
- Generates short summaries
- Stores structured data in Google Sheets

## Tech Stack
- n8n
- Google Gemini API
- Gmail API
- Google Sheets

## Workflow
Gmail → Data Cleaning → AI Classification → Data Merge → Google Sheets

## How to Use
1. Import `email-triage-ai-workflow.json` into n8n
2. Configure Gmail credentials
3. Add Gemini API key
4. Connect Google Sheets

## Output
Structured email logs with:
- Subject
- Sender
- Category
- Summary
- Metadata

---
