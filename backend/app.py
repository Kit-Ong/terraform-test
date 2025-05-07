from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    message = data.get("message", "No message")

    try:
        sns = boto3.client("sns", region_name="eu-west-2")
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message)
        return jsonify(status="Message sent"), 200
    except Exception as e:
        return jsonify(status="Error", error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
