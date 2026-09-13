from flask import Flask, render_template, request, jsonify
from error_detector import detect_errors
from ai_helper import ask_gemini

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_code():
    data = request.get_json()
    code = data.get("code", "")

    if not code.strip():
        return jsonify({
            "success": False,
            "message": "Please enter C code.",
            "errors": [],
            "ai_explanation": ""
        })

    # Step 1: Detect basic syntax errors
    errors = detect_errors(code)

    # Step 2: If errors exist, ask Gemini for an explanation
    if errors:
        try:
            ai_explanation = ask_gemini(code, errors)
        except Exception as error:
            ai_explanation = (
                "The syntax error was detected, but AI explanation "
                "could not be generated at this time."
            )
            print("AI Error:", error)

        return jsonify({
            "success": False,
            "message": "Syntax errors detected.",
            "errors": errors,
            "ai_explanation": ai_explanation
        })

    # Step 3: No basic errors found
    return jsonify({
        "success": True,
        "message": "No basic syntax errors detected.",
        "errors": [],
        "ai_explanation": ""
    })


if __name__ == "__main__":
    import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
