* Ollama 설치
* https://ollama.com/download/windows
```console
ollama pull nomic-embed-text
pip install faiss-cpu
```

* 벡터저장을 로컬에 하여, 재활용
* 기존 : 벡터 변환 및 벡터스토어 생성 (경과 시간: 87.4074초)
* 개선 : 저장된 FAISS 인덱스 불러오기 완료 (경과 시간: 0.0523초)
  * 원본 텍스트 파일 : 540KB 
  * 저장된 FAISS 인덱스 크기 : 2.1MB
* 실행결과 CPU i5-8400, MEM 16G
```console
260125 12:08 
faiss VERSION : 1.13.0
1 문서 객체 리스트 반환 (경과 시간: 0.0030초)
2 문서 분할 (경과 시간: 0.0070초)
분할된 문서 갯수 : 535
3 Ollama Embeddings 초기화 (경과 시간: 0.0190초)
4 벡터 변환 및 벡터스토어 생성 (경과 시간: 87.4074초)
4.1 저장된 FAISS 인덱스 불러오기 완료 (경과 시간: 0.0523초)
5 문서 검색 (경과 시간: 0.0866초)
현재 시간 : 2026-01-25 17:40:13
```

* 추가 hugging face hub
```console
huggingface-cli download BM-K/KoSimCSE-roberta-multitask --local-dir ./models/KoSimCSE\ 
pip install -U langchain langchain-core langchain-community langchain-huggingface
pip install -U sentence-transformers

```
* 실행결과
```console
FAISS 인덱스 새로 생성 완료 (경과 시간: 208.5387초)
인덱스를 'faiss_index_secret' 폴더에 저장했습니다.
현재 시간 : 2026-01-26 17:53:27
```

* mistral 모델 추가 
```console
ollama pull mistral
```

* 실행결과
```console
faiss VERSION : 1.13.2
1 문서 객체 리스트 반환 (경과 시간: 0.0810초)
2 문서 분할 (경과 시간: 0.0050초)
분할된 문서 갯수 : 339
3 Ollama Embeddings 초기화 (경과 시간: 10.1361초)
저장된 FAISS 인덱스 불러오기 완료 (경과 시간: 0.1246초)
현재 시간 : 2026-01-26 18:12:39
질문 : 헤이스케의 직업은 무엇인가?  Please answer in Korean
답변 : {'query': '헤이스케의 직업은 무엇인가?  Please answer in Korean', 'result': ' 헤이스케의 직업은 자동차 부품 제조업체의 생산공장에서 일하고 있습니다.'}
6 ChatOllama QA 실행 (경과 시간: 48.8072초)
현재 시간 : 2026-01-26 18:13:28
```
* 채팅 기능 추가
```console
RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)
질문 > 1장 요약 해줘요.
ChatOllama QA 실행 (경과 시간: 64.3313초)
답변 > {'query': '1장 요약 해줘요.', 'result': ' 이 설정에서는 한 차원의 차이가 있는 두 사람인 헤이스케와 나오코가 있습니다. 무거운 심정으로 자신과 전화를 걸어온 세이코(나오코의 친구)에게 헤이스케는 교통 지도를 보고 세이코의 집을 찾아갔습니다. 그런 후일담은 나와지지 않았으므로 1장의 주제는 헤이스케와 나오코가 어떻게 만난 것인가와 두 사람간의 관계에 대한 시작입니다.'}
질문 > 
```

* 책 2권 RAG
```console
E:\project\intellij\python\llm\firstllm\venv\Scripts\python.exe E:\project\intellij\python\llm\firstllm\main.py 
faiss VERSION : 1.13.2, 현재 시간 : 2026-01-30 15:45:36
총 2권의 책을 로드합니다.
1 문서 객체 리스트 반환 (경과 시간: 0.0030초)
2 문서 분할 (경과 시간: 0.0108초)
분할된 문서 갯수 : 662
3 HuggingFace Embeddings 초기화 (경과 시간: 10.3228초)
FAISS 인덱스 새로 생성 완료 (경과 시간: 338.9731초)
4 인덱스를 'faiss_index_books2' 폴더에 저장했습니다.
현재 시간 : 2026-01-30 15:51:26
RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)
질문 > 책 들의 제목은? 
ChatOllama QA 실행 (경과 시간: 70.5769초)
답변 > {'query': '책 들의 제목은?', 'result': ' The context provided doesn\'t directly answer the question about the titles of the books on the desk. However, we can infer that they are related to economics based on the following sentences:\n\n1. "... 서적들이 잡다하게 쌓여 있었다." (There were stacks of various books.)\n2. "저일스는 그중에서 몇 권인가를 집어들고 제목을 읽어보았다." (She picked up a few books and read their titles.)\n3. "\'경제, 이론과 실천\', \'상급자를 위한 경제학\'" (Among the books, there were titles like "Economics, Theory and Practice" and "Advanced Economics")\n\nThese titles suggest that the books are related to economics.'}
질문 > 레이의 직업은 무엇인가?
ChatOllama QA 실행 (경과 시간: 42.7255초)
답변 > {'query': '레이의 직업은 무엇인가?', 'result': ' 문헌에서 보아하면, 레이는 에스코트 업태를 하고 있었습니다. 따라서 그녀의 직업은 "에스코트"라고 할 수 있습니다.'}
질문 > 
```