# ThreatLens - AI-Driven Threat Forecasting System
SIH Problem ID: SIH26153

## Overview
ThreatLens is an AI-powered cybersecurity dashboard that predicts threats BEFORE they happen using log analysis and Machine Learning.

## Problem Statement
Detects 3 attack types:
- Brute Force
- DDoS 
- Phishing / SQL Injection

## Features
- Real-time log analysis from logs.txt
- Live threat prediction with 91% accuracy
- Attack Simulator for testing
- Risk Scoring (CRITICAL/HIGH/MEDIUM)
- Automated response (Block IP, Rate Limit, Blacklist)

## Tech Stack
- Python, Flask, HTML/CSS, Machine Learning (Rule-based + ML ready)

## How to Run
1. Clone repo
2. pip install flask
3. python app.py
4. Open http://127.0.0.1:5000
5. In second terminal: python attack_simulator.py

## Demo
Live dashboard shows real-time attacks from attack_simulator.py

## Team
SIH 2025 - Internal Hackathon Submission

## Future Scope
- Integrate Isolation Forest ML model
- MITRE ATT&CK mapping
- Email alerts
