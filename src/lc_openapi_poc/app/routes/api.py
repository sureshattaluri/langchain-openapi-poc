# app/api.py
from flask import Blueprint, request, jsonify

from src.lc_openapi_poc.core.chat_engine import agent_with_history

api_bp = Blueprint('api', __name__)


@api_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400

    try:
        config = {"configurable": {"session_id": "session-id-123"}}

        result = agent_with_history.invoke({"input": query}, config=config)
        print(result)

        return jsonify({"query": query, "result": result['output']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
