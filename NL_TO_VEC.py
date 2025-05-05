import json
from kobert_transformers import get_tokenizer
from transformers import BertModel
import torch

#JSON → 자연어 문장 생성
def json_to_naturalsentence(data):
    name = data.get("name", "미상")
    age = data.get("age", "미상")
    job = data.get("job", "없음")
    career=", ".join(data.get("career",[])) or "없음"
    certificate=", ".join(data.get("certificate",[])) or "없음"

    #JSON 정보 기반으로 다음과 같은 프롬프트 생성
    sentence = (
        f"{name}님은 {age}세의 {job}입니다. "
        f"보유한 기술은 {career}이며, "
        f"취득한 자격증으로는 {certificate}이 있습니다."
    )
    return sentence

#KoBERT 문장 임베딩 함수
def get_kobert_embedding(text, tokenizer, model, device):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    #KoBERT는 1회 요청에 512토큰까지만 가능, 지금 저장하는 프롬프트가 몇 토큰인지 체크해주는 코드드
    token_count = inputs["input_ids"].shape[1]
    print(f"해당 프롬프트의 토큰 수: {token_count}")    

    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
    return cls_embedding

#메인 실행 파트
if __name__ == "__main__":
    #JSON 형식의 데이터
    data = {
        "name": "sycho73",
        "age": 26,
        "job": "학생",
        "career": ["java", "javascript"],
        "certificate": ["정보처리기사", "SQLD"]
    }

    # 문장 생성
    kobert_sentence = json_to_naturalsentence(data)
    print("생성된 문장:")
    print(kobert_sentence)

    # KoBERT 로딩
    tokenizer = get_tokenizer()  #KOBERT 전용 토크나이저
    model = BertModel.from_pretrained("skt/kobert-base-v1")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # 임베딩 생성
    embedding = get_kobert_embedding(kobert_sentence, tokenizer, model, device)
    print("KoBERT 임베딩 벡터 크기:", embedding.shape)
    print("KoBERT 임베딩 벡터 값:", embedding)
