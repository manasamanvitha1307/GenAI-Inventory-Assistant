from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# --- LAYER 3: DATA LAYER (Kaggle Dataset) ---
INVENTORY = [
    {"item": "iPhone 15 Pro", "price": "$999", "stock": 8, "status": "Low Stock", "specs": "128GB, Titanium finish"},
    {"item": "Samsung Galaxy S24", "price": "$799", "stock": 31, "status": "In Stock", "specs": "256GB, Phantom Black"},
    {"item": "Dell XPS 15", "price": "$1299", "stock": 45, "status": "In Stock", "specs": "16GB RAM, 512GB SSD"},
    {"item": "Macbook Pro 14", "price": "$1999", "stock": 22, "status": "In Stock", "specs": "M3 Pro chip, 18GB RAM"},
    {"item": "Sony WH-1000XM5", "price": "$399", "stock": 67, "status": "In Stock", "specs": "30hr battery"},
    {"item": "iPad Air", "price": "$599", "stock": 28, "status": "In Stock", "specs": "10.9 inch display"},
    {"item": "LG Ultrawide 34", "price": "$499", "stock": 0, "status": "Out of Stock", "specs": "34-inch Curved"}
]

# --- LAYER 4: PROCESS LAYER (RAG Policies) ---
DOCS = [
    {"title": "Sustainability", "content": "Use recyclable padding and carbon-neutral carriers for shipping."},
    {"title": "Warehouse A", "content": "Keep humidity at 40% and temperature at 22°C for electronics."}
]

def get_context(query):
    query = query.lower()
    return "\n".join([f"Rule: {d['title']} - {d['content']}" for d in DOCS if any(w in d['content'].lower() for w in query.split())])

# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json.get("prompt", "")
    api_key = os.getenv("AI_API_KEY") 

    if not api_key:
        return jsonify({"response": "❌ Error: API Key is missing. Check terminal."})

    try:
        inv_context = "\n".join([f"- {i['item']}: {i['price']}, Stock: {i['stock']}" for i in INVENTORY])
        policy_context = get_context(user_prompt)

        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.1-8b-instant",  # <--- UPDATED MODEL NAME
            "messages": [
                {"role": "system", "content": f"You are a professional Inventory Manager. Data:\n{inv_context}\n\nPolicies:\n{policy_context}"},
                {"role": "user", "content": user_prompt}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()

        if 'choices' in response_data:
            bot_reply = response_data['choices'][0]['message']['content']
            return jsonify({"response": bot_reply})
        else:
            error_detail = response_data.get('error', {}).get('message', 'Unknown API Error')
            return jsonify({"response": f"⚠️ Groq API Error: {error_detail}"})

    except Exception as e:
        return jsonify({"response": f"❌ System Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)