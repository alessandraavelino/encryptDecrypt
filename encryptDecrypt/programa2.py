import pickle
import hashlib
import rsa





# III - O programa 2 deverá ler o conteúdo de um arquivo de texto e gerar um código hash SHA-256 sobre o conteúdo lido;

arquivo = open('msg.txt')
msg = arquivo.read()
h = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print(h)

#IV - O programa 2 deverá criptografar o código hash gerado com a chave pública gerada pelo programa 1;
key = pickle.load(open('pubKey.pkl', 'rb'))
encMessage = rsa.encrypt(h.encode(), key)
print("hash criptografado: ", encMessage)

# **  Estava salvando esse hash em formato .txt , por isso estava ocasionando problemas de que não é possível converter strings para bytes, algo assim... **
pickle.dump(encMessage, open('hashCripto.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)



#V - O usuário do sistema (ou o programa 2) deverá criar um pacote (.rar, .tar, etc...) contendo o arquivo de texto e o código hash criptografado;



