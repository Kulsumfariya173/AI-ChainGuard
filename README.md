# AI-ChainGuard: Intelligent Blockchain-Based Cyber Threat Detection

## Project Overview

AI-ChainGuard is a mini-project that combines Machine Learning and Blockchain technology to identify suspicious network activities and maintain tamper-evident security logs.

The system uses a Random Forest classification model to analyse network traffic features and classify activities as Normal or Suspicious. When suspicious activity is detected, the corresponding security alert is recorded in a blockchain structure using SHA-256 hashing.

The blockchain integrity verification mechanism checks whether stored records have been modified.

## Objectives

- Detect suspicious network activities using Machine Learning.
- Classify network traffic as Normal or Suspicious.
- Record suspicious security alerts in a blockchain.
- Maintain hash-linked security records.
- Detect unauthorized modifications through blockchain integrity verification.

## Key Features

- **User Login:** Provides a login interface for accessing the application.
- **Threat Detection:** Analyses network traffic using a Random Forest classifier.
- **Risk Classification:** Displays the predicted threat category and risk level.
- **Blockchain Logging:** Stores suspicious security alerts in hash-linked blocks.
- **Integrity Verification:** Checks blockchain records for unauthorized modifications.
- **Threat History:** Displays previously recorded security alerts.
- **CSV Export:** Allows users to download threat history.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Random Forest Classifier
- Blockchain
- SHA-256 Hashing

## Project Structure

```text
AI-ChainGuard/
│
├── app.py
├── requirements.txt
│
├── dataset/
│   └── network_traffic.csv
│
├── ai_model/
│   └── threat_detection.py
│
└── blockchain/
    ├── __init__.py
    ├── blockchain.py
    └── test_blockchain.py
```

## System Workflow

1. The user logs into the Streamlit application.
2. Network traffic features are entered into the threat detection interface.
3. The Random Forest model analyses the input data.
4. The system predicts whether the activity is Normal or Suspicious.
5. Suspicious alerts are recorded in the blockchain.
6. SHA-256 hashing links the blocks together.
7. The integrity verification function checks whether blockchain records have been altered.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-ChainGuard.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-ChainGuard
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Machine Learning Component

The project uses a Random Forest classification algorithm to analyse network traffic features such as:

- Connection duration
- Source bytes
- Destination bytes
- Failed login attempts
- Connection count
- Login success status

The model predicts whether the supplied network activity is Normal or Suspicious.

## Blockchain Component

The blockchain module maintains security alerts using:

- Block index
- Timestamp
- Alert data
- Previous block hash
- Current block hash

SHA-256 hashing is used to generate block hashes. The integrity verification function checks the relationship between blocks and identifies modifications to stored records.

## Limitations

- The current prototype uses a small sample network traffic dataset.
- Network traffic features are entered manually through the application.
- The system is a demonstration prototype and is not connected to live network monitoring infrastructure.
- Model predictions require further evaluation using larger and more diverse datasets.

## Future Enhancements

- Integration with real-time network traffic monitoring.
- Training with larger cybersecurity datasets.
- Improved threat classification and evaluation.
- Integration with additional blockchain platforms.
- Email or dashboard-based security notifications.

## Project Information

**Project Name:** AI-ChainGuard

**Project Type:** Blockchain and Machine Learning Mini-Project

**Domain:** Cybersecurity, Machine Learning and Blockchain

**Purpose:** Cyber threat detection and tamper-evident security logging.

---

*Developed as an academic mini-project.*
