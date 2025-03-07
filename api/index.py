from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all origins (to allow GET requests from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Student marks data
STUDENT_MARKS = [
    {"name":"riUrgLw","marks":5},{"name":"gJfqNemwRp","marks":93},{"name":"B0rI","marks":21},{"name":"ezl1","marks":68},{"name":"IEV","marks":91},{"name":"4wO","marks":21},{"name":"W37F","marks":0},{"name":"x","marks":91},{"name":"Vf1Y7ZyzA","marks":57},{"name":"v","marks":51},{"name":"t","marks":78},{"name":"pnNLOJ5jV","marks":9},{"name":"yuCOZogAIl","marks":44},{"name":"bCy","marks":52},{"name":"7IfI","marks":6},{"name":"EJr","marks":74},{"name":"jgrS1GcpP","marks":49},{"name":"yjBMe0pf","marks":82},{"name":"UlJ31","marks":30},{"name":"hjaNr4By","marks":4},{"name":"3Xgxynu","marks":98},{"name":"DGrmx","marks":32},{"name":"tLscHvKqA","marks":13},{"name":"qjWu4","marks":78},{"name":"NMR9AQ89","marks":49},{"name":"1","marks":62},{"name":"kE","marks":13},{"name":"4JMOhI","marks":58},{"name":"FDSv","marks":86},{"name":"Mxz","marks":10},{"name":"8cWuSjFxO","marks":71},{"name":"jaXHqN7glh","marks":62},{"name":"21","marks":90},{"name":"E","marks":70},{"name":"KP5xnDtGHg","marks":9},{"name":"nk","marks":72},{"name":"h19xVptC","marks":65},{"name":"BkS","marks":59},{"name":"rSGhW","marks":60},{"name":"EAyODWw","marks":57},{"name":"Z","marks":94},{"name":"IFVsxROhAq","marks":33},{"name":"W6fR5m0y","marks":12},{"name":"j0","marks":30},{"name":"EhCXHOw","marks":30},{"name":"iFvtR","marks":9},{"name":"xQE","marks":42},{"name":"rT","marks":35},{"name":"Y","marks":9},{"name":"uoZ","marks":71},{"name":"Vs0QVG84Lf","marks":22},{"name":"zA1bKLlSy","marks":85},{"name":"ggwSavq","marks":31},{"name":"ACttL","marks":64},{"name":"ZsTeDzS","marks":2},{"name":"P5uyIT80QD","marks":31},{"name":"eg","marks":95},{"name":"BL","marks":88},{"name":"ylr6TW0","marks":26},{"name":"d4BOMhHzu","marks":26},{"name":"qU0ASu9","marks":23},{"name":"d","marks":97},{"name":"WyJto6","marks":5},{"name":"4WO8vR","marks":87},{"name":"uxoKFPu6","marks":84},{"name":"LC8YK","marks":58},{"name":"VFw1shpYrw","marks":73},{"name":"Uw","marks":23},{"name":"r3RF","marks":13},{"name":"Z2WzNKkGnD","marks":93},{"name":"QFyhuS","marks":25},{"name":"ACgP3QOdd","marks":28},{"name":"vwE1UFJ","marks":37},{"name":"M9mF6l9g","marks":80},{"name":"cW","marks":97},{"name":"4i83Qiyd","marks":13},{"name":"g","marks":64},{"name":"KKhgbfN","marks":69},{"name":"xjP","marks":75},{"name":"jx","marks":52},{"name":"0M5UqCA","marks":47},{"name":"JGXFye","marks":67},{"name":"yScLIH1G","marks":99},{"name":"lRaswr6","marks":2},{"name":"aBWp4bmp","marks":91},{"name":"gqARq","marks":95},{"name":"Xzm7F","marks":55},{"name":"WDHZWa","marks":47},{"name":"cIm0Y8SzU","marks":50},{"name":"ZwwJ","marks":82},{"name":"XjkNxDxV6K","marks":73},{"name":"EhSRPgYu","marks":78},{"name":"iwejh0N3R","marks":57},{"name":"D","marks":42},{"name":"Q","marks":58},{"name":"P0YX69JcO","marks":69},{"name":"3i","marks":21},{"name":"5KVE","marks":80},{"name":"msv","marks":93},{"name":"nqJZQbl","marks":34}
]

@app.get("/api")
def get_marks(name: List[str] = []):
    """
    Get marks for the requested names.
    Example request: /api?name=riUrgLw&name=B0rI
    Response: {"marks": [5, 21]}
    """
    marks_list = [student["marks"] for student in STUDENT_MARKS if student["name"] in name]
    return {"marks": marks_list}
