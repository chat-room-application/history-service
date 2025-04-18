import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://devuser:devpass@localhost:5432/chat_history")
