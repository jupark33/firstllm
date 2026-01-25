import os
import time
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
import faiss
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.chains import RetrievalQA

import utils

print(f'faiss VERSION : {faiss.__version__}')

INDEX_PATH = "faiss_index_secret"

###########################
# 시작 시간 기록
start_time = time.time()
# 텍스트 파일 로드
loader = TextLoader("secret_utf8.txt", encoding="utf-8")
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
# 최초 실행 여부 판단
if os.path.exists(INDEX_PATH):
    # 저장된 인덱스가 있으면 불러오기
    start_time = time.time()
    vectorstore = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    elapsed = time.time() - start_time
    print(f"저장된 FAISS 인덱스 불러오기 완료 (경과 시간: {elapsed:.4f}초)")
else:
    # 없으면 새로 생성 후 저장
    start_time = time.time()
    vectorstore = FAISS.from_documents(docs, embeddings)
    elapsed = time.time() - start_time
    print(f"FAISS 인덱스 새로 생성 완료 (경과 시간: {elapsed:.4f}초)")
    vectorstore.save_local(INDEX_PATH)
    print(f"인덱스를 '{INDEX_PATH}' 폴더에 저장했습니다.")
print(f'현재 시간 : {utils.timestamp()}')

###########################
# 5. ChatOllama + RetrievalQA 연결
llm = ChatOllama(model="llama2:7b")  # 원하는 Ollama 모델 이름 지정 (예: "llama2", "mistral", "gemma" 등)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff"
)

###########################
# 6. 질문 실행
start_time = time.time()
query = "헤이스케의 직업은?  Please answer in Korean"
answer = qa_chain.invoke(query)
elapsed = time.time() - start_time

print(f'질문 : {query}')
print(f'답변 : {answer}')
print(f"6 ChatOllama QA 실행 (경과 시간: {elapsed:.4f}초)")
print(f'현재 시간 : {utils.timestamp()}')