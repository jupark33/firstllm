import os
import time
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
import faiss
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_classic.chains import RetrievalQA

import utils

print(f'faiss VERSION : {faiss.__version__}, 현재 시간 : {utils.timestamp()}')

INDEX_PATH_BOOKS30 = "faiss_index_books30"

###########################
# 시작 시간 기록
start_time = time.time()

# 📚 100권 소설책 로드 (예: books 폴더 안에 book1.txt ~ book100.txt)
documents = []
books_dir = "books30"   # 소설책 텍스트 파일들이 들어있는 폴더
book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

print(f"총 {len(book_files)}권의 책을 로드합니다.")

for file in book_files:
    loader = TextLoader(os.path.join(books_dir, file), encoding="utf-8")
    documents.extend(loader.load())

elapsed = time.time() - start_time
print(f"1 문서 객체 리스트 반환 (경과 시간: {elapsed:.4f}초)")

###########################
# 1 문서 분할
start_time = time.time()
text_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)
elapsed = time.time() - start_time
print(f"2 문서 분할 (경과 시간: {elapsed:.4f}초)")
print(f'분할된 문서 갯수 : {len(docs)}')

###########################
# 3. HuggingFace Embeddings 초기화
start_time = time.time()
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cpu"}    # GPU 사용 시 "cuda"
)
elapsed = time.time() - start_time
print(f"3 HuggingFace Embeddings 초기화 (경과 시간: {elapsed:.4f}초)")

###########################
# 4. 벡터 변환 및 벡터스토어 생성
if os.path.exists(INDEX_PATH_BOOKS30):
    start_time = time.time()
    vectorstore = FAISS.load_local(INDEX_PATH_BOOKS30, embeddings, allow_dangerous_deserialization=True)
    elapsed = time.time() - start_time
    print(f"4 저장된 FAISS 인덱스 불러오기 완료 (경과 시간: {elapsed:.4f}초)")
else:
    start_time = time.time()
    vectorstore = FAISS.from_documents(docs, embeddings)
    elapsed = time.time() - start_time
    print(f"FAISS 인덱스 새로 생성 완료 (경과 시간: {elapsed:.4f}초)")
    vectorstore.save_local(INDEX_PATH_BOOKS30)
    print(f"4 인덱스를 '{INDEX_PATH_BOOKS30}' 폴더에 저장했습니다.")
print(f'현재 시간 : {utils.timestamp()}')

###########################
# 5. ChatOllama + RetrievalQA 연결
llm = ChatOllama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff"
)

###########################
# 6. 질문 실행
# start_time = time.time()
# query = "주인공의 직업은 무엇인가? Please answer in Korean"
# answer = qa_chain.invoke(query)
# elapsed = time.time() - start_time
#
# print(f'질문 : {query}')
# print(f'답변 : {answer}')
# print(f"6 ChatOllama QA 실행 (경과 시간: {elapsed:.4f}초)")
# print(f'현재 시간 : {utils.timestamp()}')


###########################
# 7. CLI 대화 루프
def chat_cli():
    print("RAG 챗봇 시작! 질문을 입력하세요. (종료하려면 'exit' 입력)")
    while True:
        question = input("질문 > ").strip()
        if question.lower() in ["exit", "quit", "종료"]:
            print("챗봇을 종료합니다.")
            break
        start_t = time.time()
        answer_q = qa_chain.invoke(question + " Please answer in Korean")
        elapsed_t = time.time() - start_t
        print(f"ChatOllama QA 실행 (경과 시간: {elapsed_t:.4f}초)")
        print("답변 >", answer_q)


chat_cli()
