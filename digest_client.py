
import requests

def main():
    url = "http://localhost:5001/api/v1/weekly-digest"
    params = {
        "userId":    "550e8400-e29b-41d4-a716-123456789",
        "weekStart": "2025-05-11",
        "weekEnd":   "2025-05-18",
    }

    # 1) Send request
    resp = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()

    # 2) Receive JSON response from the server
    # The JSON payload response is parsed into a Python Dictionary
    digest = resp.json()

    # 3) Displays the data from the response
    print("Full digest:", digest, "\n")

    print("Completed tasks:")
    for t in digest["completedTasks"]:
        print(f" {t['title']} at {t['completedAt']}")

    print("\nUpcoming tasks:")
    for t in digest["upcomingTasks"]:
        print(f" {t['title']} due {t['dueDate']}")

    print("\nOverdue tasks:")
    for t in digest["overdueTasks"]:
        print(f" {t['title']} due {t['dueDate']} ({t['daysOverdue']} days overdue)")

if __name__ == "__main__":
    main()