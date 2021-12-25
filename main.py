# Run: uvicorn main:app --host 0.0.0.0 --port 8080

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def getUsers():
    users = []
    for index in range(1, 1001):
        strIndex = str(index)
        firstName = "FirstName" + strIndex
        lastName = "LastName" + strIndex
        framework = "Python (FastAPI)"
        users.append({
            "index": index,
            "FirstName": firstName,
            "LastName": lastName,
            "age": 25,
            "framework": framework,
        })
    return users


@app.get("/users")
def users():
    return getUsers()


if __name__ == "__main__":
    app.run()
