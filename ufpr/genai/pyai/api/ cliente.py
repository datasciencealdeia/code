import requests
import threading
import time

inicio = time.time()

URL = "http://127.0.0.1:8000/teste_async"

def fazer_requisicao(i):
  response = requests.get(URL, params={"id": i})
  print(response.text)

threads = []

for i in range(1, 10000):
  t = threading.Thread(target=fazer_requisicao, args=(i,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

fim = time.time()

inicioSync = time.time()

URL = "http://127.0.0.1:8000/teste_sync"

threads = []

for i in range(1, 10000):
  t = threading.Thread(target=fazer_requisicao, args=(i,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

fimSync = time.time()

print(f'Assíncrono: ',fim - inicio)
print(f'Síncrono: ',fimSync - inicioSync)

