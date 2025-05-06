#자연어 프롬프트 토큰 수 확인용 파일(512토큰 넘는지 확인해야함)

from kobert_transformers import get_tokenizer

def count_tokens(prompt):
    # KoBERT 토크나이저 로드
    tokenizer = get_tokenizer()
    
    # 프롬프트 토큰화
    tokens = tokenizer.tokenize(prompt)
    
    # 토큰 수 계산
    token_count = len(tokens)
    
    return token_count

if __name__ == "__main__":
    prompt = input("자연어 프롬프트를 입력하세요: ")
    token_count = count_tokens(prompt)
    print(f"프롬프트의 토큰 수: {token_count}")
