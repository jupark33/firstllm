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

| 책 권수 | 원본사이즈  | FAISS 인덱스 생성 시간 | 벡터 데이터 사이즈 | 답변 시간 |
|------|--------|--------------|------------|-------|
| 1    | 350KB  |  87초        | 1.71MB     | 48초   |
| 2    | 709KB  |  338초       | 3.36MB     | 42초   |
| 3    | 1.33MB |  748초       | 6.62MB     | 65초   |
| 10   | 3.72MB |  2382초(39분) | 18.9MB     | 71초   |
| 30   | 8.59MB |  5370초(89분 30초) | 43.2MB     | 76초   |



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

* 책 3권 RAG
```console
E:\project\intellij\python\llm\firstllm\venv\Scripts\python.exe E:\project\intellij\python\llm\firstllm\main.py 
faiss VERSION : 1.13.2, 현재 시간 : 2026-01-30 16:38:46
총 3권의 책을 로드합니다.
1 문서 객체 리스트 반환 (경과 시간: 0.0587초)
2 문서 분할 (경과 시간: 0.1150초)
분할된 문서 갯수 : 1284
3 HuggingFace Embeddings 초기화 (경과 시간: 10.5540초)
FAISS 인덱스 새로 생성 완료 (경과 시간: 748.1036초)
4 인덱스를 'faiss_index_books3' 폴더에 저장했습니다.
현재 시간 : 2026-01-30 16:51:25
RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)
질문 > 아이비가 사는 곳과 직업은? 
ChatOllama QA 실행 (경과 시간: 65.2530초)
답변 > {'query': '아이비가 사는 곳과 직업은? Please answer in Korean', 'result': ' 아이비는 유산으로 받아들인 대저택에서 살고 있으며, 런싱 회사에서 근무하고 있다. 그러나 직업은 비서로 발탁된 후 한달 반 만에 해고되었고, 이전에는 타이프실에서 2년 근무했다.'}
질문 > 
```

* 책 10권 RAG, 39분 
```console
E:\project\intellij\python\llm\firstllm\venv\Scripts\python.exe E:\project\intellij\python\llm\firstllm\main.py 
faiss VERSION : 1.13.2, 현재 시간 : 2026-01-30 16:59:07
총 10권의 책을 로드합니다.
1 문서 객체 리스트 반환 (경과 시간: 0.2624초)
2 문서 분할 (경과 시간: 0.4397초)
분할된 문서 갯수 : 3730
3 HuggingFace Embeddings 초기화 (경과 시간: 7.5745초)
FAISS 인덱스 새로 생성 완료 (경과 시간: 2382.2170초) 39분 
4 인덱스를 'faiss_index_books10' 폴더에 저장했습니다.
현재 시간 : 2026-01-30 17:38:58
RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)
질문 > 레슬리는 성격은 어떤가? 레슬리의 직업과 사는 곳은 어디 인가? 
ChatOllama QA 실행 (경과 시간: 71.2559초)
답변 > {'query': '레슬리는 성격은 어떤가? 레슬리의 직업과 사는 곳은 어디 인가? Please answer in Korean', 'result': ' 레슬리는 부모님이 파이어 섬에서 별장을 갖고 있었기 때문에 자신은 도시와 시골의 튀기 같은 존재였습니다. 아버지의 누이인 에반스부인이었고, 어린 시절부터 뉴욕에서 자신을 자랐거나 그러한 곳에서 살았는지는 알려지지 않았습니다.'}
질문 >  
```
* 책 30권 RAG, 89분 30초
```console
faiss VERSION : 1.13.2, 현재 시간 : 2026-01-31 10:15:05
총 30권의 책을 로드합니다.
1 문서 객체 리스트 반환 (경과 시간: 0.0509초)
2 문서 분할 (경과 시간: 1.0936초)
분할된 문서 갯수 : 8468
3 HuggingFace Embeddings 초기화 (경과 시간: 11.5497초)
FAISS 인덱스 새로 생성 완료 (경과 시간: 5370.2279초)
4 인덱스를 'faiss_index_books30' 폴더에 저장했습니다.
현재 시간 : 2026-01-31 11:44:48
RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)
질문 > 재크의 성격과, 성장 과정, 직업과 사는 곳은 어디인가?
ChatOllama QA 실행 (경과 시간: 76.9219초)
답변 > {'query': '재크의 성격과, 성장 과정, 직업과 사는 곳은 어디인가? Please answer in Korean', 'result': ' 이 문헌에서는 바네사는 재크를 좋아하고 있지만 자신의 마음을 표현할 수 없으며, 재크는 36세, 부두에서 일한 후 런던과 파리에서 그림공부를 하였고 현재 코네티컷주에서 작업을 해오며, 아틀리에(소호)에서 사는 것으로 나타난다. 또한 재크의 성격은 어느 정도 악인적이고 그는 현재 업타운에 거주하고 있으며, 그를 갈아탄 곳은 없다고 말한다.'}
질문 > 
```