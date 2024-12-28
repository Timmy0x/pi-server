
from flask import Flask, Blueprint, jsonify, send_file, request, Response

import requests
from groq import Groq

from dotenv import load_dotenv

import os

load_dotenv()
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

app = Flask(__name__)
markdowner_bp = Blueprint("markdowner_bp", __name__, url_prefix="/api/markdowner")

@markdowner_bp.route("/scrape")
def scrape():
    url = request.args.get("url")
    html = requests.get(url).text
    
    completion = groq_client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": """
You are an AI markdown assistant. Convert HTML content to valid markdown.
"""
            },
            {
                "role": "user",
                "content": f"Convert this HTML to valid, readable markdown, decipering the content: {html}"
            }
        ]
    )

    output = completion.choices[0].message.content
    if "```" in output:
        output = output.split("```")[1]
    if output.startswith("markdown"):
        output = output.replace("markdown", "", 1).strip()

    return Response(output, mimetype="text/txt")