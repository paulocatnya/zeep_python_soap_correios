# import Client do zeep, apos instalar:pip install zeep

# muito util
# python -mzeep 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
# client.wsdl.dump() retorna metodos tipos e etc
# retorna todos os metodos de um wsdl

""" PARA AUTENTICAR NO ZEEP:::
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(username, password)
session = Session()
session.auth = auth
tranport = Transport(session=session)
client = Client(<wsdl_link>, transport=transport)
"""

from zeep import Client



def ConsultaCEP(cep):
    try:
        url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
        client = Client(url)       
        dicCep = client.service.consultaCEP(cep)
        return dicCep

    except Exception as error:
        print('Rolou esse erro na consulta: ', error)


def BuscaDataAtual():
    try:
        url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
        client = Client(url)    
        vlDataAtual = client.service.buscaDataAtual()
        return vlDataAtual

    except Exception as error:
        print('Rolou esse erro na consulta: ', error)


consultaCEP = ConsultaCEP('31846100')
vlDataAtual = BuscaDataAtual()

if consultaCEP:
    print('\nconsultaCEP::')
    print(consultaCEP)

    
if vlDataAtual:
    print('\n#################\n\nvlDataAtual::')
    print(vlDataAtual)
