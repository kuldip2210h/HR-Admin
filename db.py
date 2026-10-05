from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://admin:admin@cluster.hmqekcb.mongodb.net/?appName=Cluster"

client = AsyncIOMotorClient("mongodb+srv://admin:admin@cluster.hmqekcb.mongodb.net/?appName=Cluster")

database = client["HR_ADMIN"]

user_collection = database["users"]
employee_collection = database["employees"]
department_collection = database["departments"]
attendance_collection = database["attendance"]
leave_collection = database["leaves"]
salary_collection = database["salary"]
notice_collection = database["notices"]
