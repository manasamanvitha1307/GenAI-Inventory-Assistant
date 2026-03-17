# 🚀 GenAI Inventory Decision-Support System

**PoC Version:** 1.0.0

**Target Goal:** Reducing operational reporting time from 30m to 3m.

 **📋Problem Statement**
Inventory managers currently spend significant time (averaging 30 minutes per report) manually cross-referencing structured stock data with unstructured company policies (shipping, safety, sustainability). This delay leads to:
**Inaccurate Reordering:** Increased stockout rates.
**Compliance Risks:** Failure to follow sustainability or climate-control guidelines.
**Operational Friction:** Slow decision-making during high-demand periods.

**💡Solution**
A full-stack GenAI Assistant that utilizes Retrieval-Augmented Generation (RAG) to provide instant, grounded insights. By connecting a reasoning engine (Llama 3.1) directly to our inventory database and policy documents, we enable:
**Instant Reporting:** Automated value calculations and stock health summaries.
**Policy-Grounded Advice:** Shipping and warehouse guidance based on internal documents.
**Automated Procurement:** Instant drafting of supplier emails and reorder lists.

**🎯Target Users**
**Warehouse Managers:** For real-time stock monitoring and climate safety compliance.
**Procurement Officers:** For automated reorder drafting and supplier communication.
**Operations Executives:** For high-level inventory value summaries and KPI tracking.

**🛠️AI Components Disclosure**
**Core Model:** llama-3.1-8b-instant (Meta)
**Inference Provider:** Groq Cloud (LPU - Language Processing Unit)
**Architecture:** 10-Layer GenAI Framework
**Pattern:** Retrieval-Augmented Generation (RAG)
**Data Sources:** Structured: Kaggle Electronics Inventory Dataset (CSV/JSON).
                  Unstructured: Internal PDF/Text Policies (Sustainability & Warehouse Safety).

**🚀Quick Start**
**Prerequisites:** Python 3.9+, Groq API Key.
**1.Clone the Repository:**
**Bash**
git clone https://github.com/manasamanvitha1307/GenAI-Inventory-Assistant
cd Inventory-Assistant-App
**2.Install Dependencies:**
**Bash** 
pip install -r requirements.txt
**3.Set Environment Variables:**
Create a .env file in the root directory:
**Plaintext**
AI_API_KEY=your_groq_api_key_here
**4.Run the Application:**
**Bash**
python app.py
**5.Access the Dashboard:**
Open http://127.0.0.1:5000 in your browser.

**🎥 Demo Link**
**Recorded Demo:** [Insert your YouTube/Vimeo/Google Drive link here]
**Media Disclosure:** This demo uses [List any tools used, e.g., OBS for recording, ElevenLabs for voiceover, or "No AI media tools used"].

**👥 Team Members**
Manasa Manvitha MUKKA - Lead Developer & AI Architect (ECE Paris)
