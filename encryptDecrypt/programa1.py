import hashlib
import pickle
import zipfile
import binascii
import rsa





# I - O programa 1 deverá gerar um par de chaves, sendo uma pública e uma privada;
x = input("Deseja gerar chave? s/n ")

if x == "s":
# ** Estava mantendo apenas 514 bytes para as chaves, por isso estava dando erros de memória. **
    publicKey, privateKey = rsa.newkeys(1024)
    pickle.dump(publicKey, open('pubKey.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(privateKey, open('privKey.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    print("Chaves geradas.")
    

else:

# VI - O programa 1 deverá ler o conteúdo do arquivo de texto que está no pacote e gerar um código hash SHA-256 sobre o conteúdo lido;

    file = open("msg.txt", 'r')
    msg = file.read()
    print(msg)

    originalHash = hashlib.sha256(msg.encode('utf-8')).hexdigest()
    print(originalHash)

#  VII - O programa 1 deverá descriptografar o código hash do pacote com a chave privada;
    recoveryHash = pickle.load(open('hashCripto.pkl', 'rb'))
    print(recoveryHash)
    key = pickle.load(open('privKey.pkl', 'rb'))
    print(key)

    decMessage = rsa.decrypt(recoveryHash, key).decode()
    print(decMessage)

# VIII - O programa 1 deverá comparar os códigos hash obtidos dos passos VI e VII e exibir uma mensagem de “Arquivo autêntico”, para códigos iguais ou “Arquivo Não Autêntico” para códigos diferentes.
    if decMessage == originalHash:
        print("Arquivo autêntico")
    else:
        print("Arquivo Não Autêntico")
        








