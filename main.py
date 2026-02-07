from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Python Learning Helper API")

# In-memory storage
topics = []

# Models
class Topic(BaseModel):
    name: str
    description: str

class Example(BaseModel):
    content: str

class Quiz(BaseModel):
    question: str
    answer: str


# ---------------- TOPICS ----------------
@app.post("/topics")
def create_topic(topic: Topic):
    topic_id = len(topics) + 1
    topics.append({"id": topic_id, "name": topic.name, "description": topic.description, "examples": [], "quiz": []})
    return {"message": "Topic created", "topic": topics[-1]}


@app.get("/topics")
def get_topics():
    return topics


@app.get("/topics/{topic_id}")
def get_topic(topic_id: int):
    for topic in topics:
        if topic["id"] == topic_id:
            return topic
    raise HTTPException(status_code=404, detail="Topic not found")


# ---------------- EXAMPLES ----------------
@app.post("/topics/{topic_id}/examples")
def add_example(topic_id: int, example: Example):
    for topic in topics:
        if topic["id"] == topic_id:
            topic["examples"].append(example.content)
            return {"message": "Example added", "examples": topic["examples"]}
    raise HTTPException(status_code=404, detail="Topic not found")


# ---------------- QUIZ ----------------
@app.post("/topics/{topic_id}/quiz")
def add_quiz(topic_id: int, quiz: Quiz):
    for topic in topics:
        if topic["id"] == topic_id:
            topic["quiz"].append({"question": quiz.question, "answer": quiz.answer})
            return {"message": "Quiz question added", "quiz": topic["quiz"]}
    raise HTTPException(status_code=404, detail="Topic not found")


@app.get("/topics/{topic_id}/quiz/random")
def get_random_quiz(topic_id: int):
    """
    Advanced feature: Get a random quiz question for a topic
    """
    for topic in topics:
        if topic["id"] == topic_id:
            if not topic["quiz"]:
                raise HTTPException(status_code=404, detail="No quiz available for this topic")
            return random.choice(topic["quiz"])
    raise HTTPException(status_code=404, detail="Topic not found")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Python Learning Helper API")

# In-memory storage
topics = []

# Models
class Topic(BaseModel):
    name: str
    description: str

class Example(BaseModel):
    content: str

class Quiz(BaseModel):
    question: str
    answer: str


# ---------------- TOPICS ----------------
@app.post("/topics")
def create_topic(topic: Topic):
    topic_id = len(topics) + 1
    topics.append({"id": topic_id, "name": topic.name, "description": topic.description, "examples": [], "quiz": []})
    return {"message": "Topic created", "topic": topics[-1]}


@app.get("/topics")
def get_topics():
    return topics


@app.get("/topics/{topic_id}")
def get_topic(topic_id: int):
    for topic in topics:
        if topic["id"] == topic_id:
            return topic
    raise HTTPException(status_code=404, detail="Topic not found")


# ---------------- EXAMPLES ----------------
@app.post("/topics/{topic_id}/examples")
def add_example(topic_id: int, example: Example):
    for topic in topics:
        if topic["id"] == topic_id:
            topic["examples"].append(example.content)
            return {"message": "Example added", "examples": topic["examples"]}
    raise HTTPException(status_code=404, detail="Topic not found")


# ---------------- QUIZ ----------------
@app.post("/topics/{topic_id}/quiz")
def add_quiz(topic_id: int, quiz: Quiz):
    for topic in topics:
        if topic["id"] == topic_id:
            topic["quiz"].append({"question": quiz.question, "answer": quiz.answer})
            return {"message": "Quiz question added", "quiz": topic["quiz"]}
    raise HTTPException(status_code=404, detail="Topic not found")


@app.get("/topics/{topic_id}/quiz/random")
def get_random_quiz(topic_id: int):
    """
    Advanced feature: Get a random quiz question for a topic
    """
    for topic in topics:
        if topic["id"] == topic_id:
            if not topic["quiz"]:
                raise HTTPException(status_code=404, detail="No quiz available for this topic")
            return random.choice(topic["quiz"])
    raise HTTPException(status_code=404, detail="Topic not found")
