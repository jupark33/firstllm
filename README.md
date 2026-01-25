* Ollama 설치
* https://ollama.com/download/windows
```console
ollama pull nomic-embed-text
pip install faiss-cpu
```

* 실행결과 CPU i5-8400, MEM 16G
```console
260125 12:08 
faiss VERSION : 1.13.0
1 문서 객체 리스트 반환 (경과 시간: 0.0030초)
2 문서 분할 (경과 시간: 0.0070초)
분할된 문서 갯수 : 535
3 Ollama Embeddings 초기화 (경과 시간: 0.0190초)
4 벡터 변환 및 벡터스토어 생성 (경과 시간: 87.4074초)
5 문서 검색 (경과 시간: 0.0866초)
현재 시간 : 2026-01-25 17:40:13
```