
from .pnml import parse_pnml_file,write_pnml_file
import numpy as np

class Pnrd:

    def __init__(self):
        #generate a unique id
        self.file = ''
        self._incidence_matrix_t = []
        self.len_places = 0
        self.len_transitions = 0
        self.nets = dict()
        self.fire_vector = list()

        self.numpy_inci_matrix_t = list()
        self.numpy_fire_vector = list()
        self.numpy_marking_vector = list()

    def set_pnml(self,file):

        self.file = file
        try:
            self.nets = parse_pnml_file(self.file)
            return "Arquivo Carregado com Sucesso",True
        except:
            return "Erro ao Carregar Arquivo",False

    def create_net(self):

        try:
            for net in self.nets:
                self.len_transitions = net.len_transitions
                self.len_places = net.len_places 
                self.marking_vector, self.incidence_matrix_t = net.incidence_matrix()
                self.numpy_marking_vector = np.array(self.marking_vector)
                self.numpy_inci_matrix_t = np.matrix(self.incidence_matrix_t)

                self.numpy_marking_vector.shape = (self.len_places,1)
            return "Net Criada com Sucesso", True
        except:
            return "Erro ao Criar Net", False


    def update_pnml(self,fire_vector=list(),token=list(),_type='fire'):

        if _type =='fire':
            if len(fire_vector) ==self.len_transitions:
                
                for net in self.nets:
                    self.fire_vector = fire_vector
                    self.numpy_fire_vector = np.array(self.fire_vector)
                    self.numpy_fire_vector.shape = (self.len_transitions,1)

                    self.numpy_marking_vector = self.numpy_marking_vector + self.numpy_inci_matrix_t *self.numpy_fire_vector
                    self.marking_vector = self.numpy_marking_vector.transpose().tolist()[0]

                    net.mount_marking(self.marking_vector)
                    try:
                        write_pnml_file(net,self.file)
                        return "Arquivo Enviado com Sucesso", True
                    except:
                        return "Erro ao Enviar o Arquivo", False
            else:
                msg = f"fire Vector possui um Tamanho Diferente de {self.len_transitions}"
                return msg,False
        elif _type =='token':
            if len(token) ==self.len_places:
                for net in self.nets:
                    self.numpy_marking_vector = np.array(token)
                    self.numpy_marking_vector.shape = (self.len_places,1)
                    self.marking_vector = self.numpy_marking_vector.transpose().tolist()[0]
                    self.marking_vector = token                    

                    net.mount_marking(self.marking_vector)
                    try:
                        write_pnml_file(net,self.file)
                        return "Arquivo Enviado com Sucesso", True
                    except:
                        return "Erro ao Enviar o Arquivo", False
            else:
                msg = f"Token Vector com um tamanho diferente de {self.len_places}"
                return msg,False


    def __str__(self):
        str_i_matrix_t = "Incidence Matrix Transpose: \n"+ str(self.numpy_inci_matrix_t)+ "\n"
        str_marking_vector = "Marking Vetor: \n"+ str(self.numpy_marking_vector)+ "\n"
        return str_i_matrix_t + str_marking_vector