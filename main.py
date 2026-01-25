import time
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import faiss

import utils

print(f'faiss VERSION : {faiss.__version__}')

###########################
# 시작 시간 기록
start_time = time.time()
# 텍스트 파일 로드
loader = TextLoader("sam01.txt", encoding="utf-8")
# 문서 객체 리스트 반환
documents = loader.load()
# 경과 시간 계산
elapsed = time.time() - start_time
print(f"1 문서 객체 리스트 반환 (경과 시간: {elapsed:.4f}초)")

###########################
# 1 문서 분할, 시작 시간 기록
start_time = time.time()
# 텍스트 분할기 정의
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=50
)
# 문서 분할
docs = text_splitter.split_documents(documents)
# 경과 시간 계산
elapsed = time.time() - start_time
print(f"2 문서 분할 (경과 시간: {elapsed:.4f}초)")

## 540KB 텍스트 파일, CPU i5-8400, MEM 16GB
# 문서 객체 리스트 반환 (경과 시간: 0.0040초)
# 문서 분할 (경과 시간: 0.0080초)
##

###########################
#
print(f'분할된 문서 갯수 : {len(docs)}')  # 분할된 문서 개수
# print(f'분할된 문서 첫번째 chunk : {docs[0].page_content}')  # 첫 번째 chunk 내용

###########################
# 3. Ollama Embeddings 초기화
# 시작 시간 기록
start_time = time.time()
embeddings = OllamaEmbeddings(model="nomic-embed-text")  # 원하는 모델 이름 지정
# 경과 시간 계산
elapsed = time.time() - start_time
print(f"3 Ollama Embeddings 초기화 (경과 시간: {elapsed:.4f}초)")

###########################
# 4. 벡터 변환 및 벡터스토어 생성
# 시작 시간 기록
start_time = time.time()
vectorstore = FAISS.from_documents(docs, embeddings)
# 경과 시간 계산
elapsed = time.time() - start_time
print(f"4 벡터 변환 및 벡터스토어 생성 (경과 시간: {elapsed:.4f}초)")
print(f'현재 시간 : {utils.timestamp()}')

######################
# 5. 문서 검색
start_time = time.time()
query = "유비가 사는 곳은?"
documents = vectorstore.similarity_search(query)
for document in documents:
    print(f'질문 : {query}')
    print(f'결과')
    print(document.page_content)
# 경과 시간 계산
elapsed = time.time() - start_time
print(f"5 문서 검색 (경과 시간: {elapsed:.4f}초)")
print(f'현재 시간 : {utils.timestamp()}')

'''
'''