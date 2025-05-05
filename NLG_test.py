import json

data = {        #임의의 json 데이터터
    "name":"sycho73",
    "age":26,
    "job":"학생",
    "career":["java","javascript"],
    "certificate" : ["정보처리기사","SQLD"]
}

def json_to_naturalsentence(data):
    name=data.get("name","미상")
    age=data.get("age","미상")
    job=data.get("job","없음")
    career=", ".join(data.get("career",[])) or "없음"
    certificate=", ".join(data.get("certificate",[])) or "없음"

    kobert_sentence = f"이름은 {name}이고 나이는 {age}세이며, 현재 직업은 {job}이다. 보유 기술은 {career}를 가지고 있으며 자격증은 {certificate}이다."
    return korbet_sentence

kobert_sentence = json_to_naturalsentence(data)
print(kobert_sentence)