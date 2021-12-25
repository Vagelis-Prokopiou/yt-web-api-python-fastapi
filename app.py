from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# def getUsers():
#     users = []
#     for index in range(1, 1001):
#         strIndex = str(index)
#         firstName = "FirstName" + strIndex
#         lastName = "LastName" + strIndex
#         framework = "Python (Flask)"
#         users.append({
#             "index": index,
#             "FirstName": firstName,
#             "LastName": lastName,
#             "age": 25,
#             "framework": framework,
#         })
#     return users
#
#
# @app.route("/users")
# def users():
#     return jsonify(getUsers())


if __name__ == "__main__":
    app.run()
