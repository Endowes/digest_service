# Weekly Digest Notification Service
This a guide on how to programmatically REQUEST and RECEIVE DATA from this microservice.

## Prerequisites & Installation:

- **Python 3.12+**
- **pip** (Python package installer)
- VSCode (But you can use any IDE)

To install the HTTP client library used in the examples, request and receive below:

```bash
pip install requests
```
If you want to run the microservice locally yourself, you can also install Flask (will probably have to install this since the teammate has to write their own code and run it locally aswell):

 ```bash
pip install flask
```

## Requesting Data:

Send an HTTP GET to `/api/v1/weekly-digest` with the following three query parameters:

- `userId`    - UID of the user
- `weekStart` - Start Date (Format: `YYYY-MM-DD`)
- `weekEnd`   - End Date   (Format: `YYYY-MM-DD`)

### Example Request:
```
import requests
url = "http://localhost:5001/api/v1/weekly-digest"
params = {
    "userId":    "550e8400-e29b-41d4-a716-123456789",
    "weekStart": "2025-05-12",
    "weekEnd":   "2025-05-19",
}

resp = request.get(url, params=params, timeout=5)
resp.raise_for_status()
```

## Receiving Data:

After the client issues a successful request of HTTP 200, the service returns a JSON payload in the format of:
```
{
  "userId": "550e8400-e29b-41d4-a716-123456789",
  "period": {
    "start": "2025-05-12",
    "end":   "2025-05-19"
  },
  "completedTasks": [ /* ... */ ],
  "upcomingTasks":  [ /* ... */ ],
  "overdueTasks":   [ /* ... */ ]
}
```

### Example Response:


```
digest = resp.json() # We convert the JSON payload into a Python Dictionary
# The keys are completedTasks, upcomingTasks, and overdueTasks
completed = digest["completedTasks"]
upcoming  = digest["upcomingTasks"]
overdue   = digest["overdueTasks"]

# Iterate over the completed tasks
for task in completed:
    print(f"{task['title']} (completed at {task['completedAt']})")
```

After the above code runs, the client will have access to the JSON payload and have a response like this for completedTasks:
```
 "completedTasks": [
    {
      "id":          "a1",
      "title":       "Buy Groceries",
      "completedAt": "2025-05-03T14:22:00Z"
    }
  ],
```
## UML Diagram:
![DigestSequenceDiagram](https://github.com/user-attachments/assets/000a28ac-4eb2-476a-a8ff-1d97c764df3a)

