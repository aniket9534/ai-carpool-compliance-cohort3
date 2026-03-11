.
🚗 AI Carpool Compliance System

An AI-powered traffic monitoring system that detects single-occupant vehicles in carpool lanes using computer vision. The system processes traffic camera footage, identifies violations, and tracks repeat offenders to generate warnings and simulated challans.

📌 Project Overview

Many cities implement carpool lanes where vehicles must carry two or more occupants. Manual enforcement is inefficient and resource-intensive.

This system automates the process by:

Detecting vehicles from traffic camera feeds

Counting the number of occupants inside vehicles

Identifying license plates

Tracking repeat offenders

Generating warnings and simulated challans

The system can process live or recorded traffic footage and provide analytics through a dashboard.

⚙️ Key Features

🚘 Vehicle Detection
Detects vehicles in traffic footage using YOLOv8 object detection.

🔄 Vehicle Tracking
Tracks vehicles across frames using DeepSORT to maintain consistent vehicle IDs.

👥 Occupant Detection
Counts the number of people inside vehicles using MediaPipe-based face detection.

🔢 License Plate Recognition
Extracts vehicle license plate numbers using OCR (EasyOCR).

⚠️ Violation Detection
Flags vehicles with only one occupant as potential carpool violations.

📊 Analytics Dashboard
Displays violation statistics, repeat offenders, and camera activity.

🧠 System Architecture

The system processes traffic footage through a multi-stage AI pipeline:

Traffic Camera Feed
        ↓
Frame Extraction (OpenCV)
        ↓
Vehicle Detection (YOLOv8)
        ↓
Vehicle Tracking (DeepSORT)
        ↓
Occupant Detection (MediaPipe)
        ↓
Violation Detection
        ↓
License Plate Detection + OCR
        ↓
Backend Processing (FastAPI)
        ↓
Database Storage
        ↓
Analytics Dashboard

🛠 Tech Stack
Programming

Python 3.10+

Computer Vision

OpenCV

YOLOv8

DeepSORT

MediaPipe

EasyOCR

Backend

FastAPI

SQLAlchemy

Database

PostgreSQL / SQLite (for development)

DevOps

Docker (for containerization)

⚡ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/aniket9534/ai-carpool-compliance-cohort3-system.git
cd ai-carpool-compliance-system
2️⃣ Create virtual environment
python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
