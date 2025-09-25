# app.py
from flask import Flask, request, jsonify
from solvers import solve_with_ai

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "RailNova Backend is running 🚆"})

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        # Parse input JSON
        scenario = request.get_json(force=True, silent=True)
        if not scenario:
            return jsonify({
                "error": "Invalid or missing JSON in request."
            }), 400

        # Run solver
        ai_result = solve_with_ai(scenario)

        return jsonify({
            "status": "success",
            "data": ai_result
        }), 200

    except Exception as e:
        print(f"[ERROR] Optimization failed: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)

