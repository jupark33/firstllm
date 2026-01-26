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