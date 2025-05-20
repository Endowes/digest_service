from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1/weekly-digest")
def digest():
    # Read query parameters
    user_id   = request.args.get("userId")
    week_start= request.args.get("weekStart")
    week_end  = request.args.get("weekEnd")

    # Example data (change this if you are using a DB)
    completed = [
        {"id":"a1","title":"Buy Groceries","completedAt":"2025-05-03T14:22:00Z"}
    ]
    upcoming = [
        {"id":"b1","title":"Complete CS361 Assignment","dueDate":"2025-05-19"}
    ]
    overdue = [
        {"id":"c1","title":"Renew Subscription for Discord","dueDate":"2025-05-16","daysOverdue":3}
    ]
    
    # Creates and return a JSON response
    # Response is sent back to digest_client
    return jsonify({
        "userId": user_id,
        "period": {"start": week_start, "end": week_end},
        "completedTasks": completed,
        "upcomingTasks": upcoming,
        "overdueTasks": overdue
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)