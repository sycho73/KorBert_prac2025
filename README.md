# KorBert_prac2025
KoBERT를 이용하여 벡터 정보로 변환 연습<br><br>

1.실습 전 다운받아야할 것들<br>
transformers - 허깅 페이스 모델&토크나이저 로딩<br>
torch - PyTorch 기반 모델 실행 엔진<br>
sentencepiece - KoBERT 토크나이저 내부에서 사용하는 라이브러리<br>
kobert-transformers - KoBERT를 허깅 페이스 스타일로 사용할 수 있게 해줌<br>
pip install transformers torch sentencepiece kobert-transformers 명령어를 통해 다운<br><br>

2.각 파일 별 특성<br>
NLG_test.py : 자연어 생성 파일, 테스트를 위해 python NLG_test.py 실행<br>
해당 파일에서 문장 형식의 프롬프트로 자연어 생성을 한 이유는 KoBERT 모델이 자연스러운 한국어 문장 형식의 자연어를 인식하는 모델이기 때문<br>
NL_TO_VEC.py : JSON 데이터를 이용하여 생성한 프롬프트를 KoBERT를 이용하여 벡터 정보로 반환 후 관련 정보들을 반환환<br><br>

3.INPUT , OUTPUT<br>
INPUT : JSON 정보를 기반으로 자연어 생성한 프롬프트<br>
OUTPUT : INPUT 프롬프트의 토큰 수, KoBERT 벡터 크기, KoBERT 임베딩 벡터 값<br><br>

4.참고 사항<br>
-KoBERT는 한 번 정보를 반환할 때 최대 512토큰을 반환하며 그 이상의 토큰은 잘라서 반환하지 않느다. 그러기에 현재 프롬프트가 몇 토큰인지 확인하는 코드를 추가하였다<br>
-KoBERT 임베딩 벡터 값이 상당히 많이 나올텐데 실습용으로 앞의 N개의 데이터만 반환되게 하고 싶으면 print("KoBERT 임베딩 벡터 값:", embedding) -> print("KorBERT 임베딩 벡터 값:", embedding[:N]) 으로 수정하면된다<br>
-디폴트로 적어둔 JSON 데이터의 결과는 다음과 같으니 필요시 사용<br>
[DefaultData.txt](https://github.com/user-attachments/files/20042407/DefaultData.txt)<br>
-리포지토리에는 KorBERT❗라고 적혀있지만 이건 틀렸고 KoBERT✅가 맞다<br>


