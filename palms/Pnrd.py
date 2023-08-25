from .pnml import parse_pnml_file, write_pnml_file
import numpy as np
from datetime import datetime, date
import pytz
from palms.FileCreator import FileCreator
import json


class Pnrd:
    def __init__(self):
        # generate a unique id
        self.file = ""
        self._incidence_matrix_t = []
        self.marking_vector = []
        self.initial_token_vector = []
        self.initial_fire_vector = []
        self.incidence_matrix = []
        self.incidence_vector = []
        self.str_incidence_vector = ""
        self.str_initial_token_vector = ""
        self.str_initial_fire_vector = ""
        self.len_places = 0
        self.len_transitions = 0
        self.nets = dict()
        self.fire_vector = list()
        self.transition_names = list()
        self.numpy_inci_matrix_t = list()
        self.numpy_fire_vector = list()
        self.numpy_marking_vector = list()

    def set_pnml(self, file):
        self.file = file
        try:
            self.nets = parse_pnml_file(self.file)
            return "File Uploaded Successfully", True
        except Exception:
            return "Error Loading File", False

    def _set_incidence_vector(self):
        self.incidence_vector = []
        for row in self.incidence_matrix_t:
            for i in row:
                self.incidence_vector.append(i)

        self.str_incidence_vector = " ".join(map(str, self.incidence_vector))

    def set_initial_token_vector(self):
        length = len(self.marking_vector)
        self.initial_token_vector = [1] + [0] * (length - 1)
        self.str_initial_token_vector = " ".join(map(str, self.initial_token_vector))

    def set_initial_fire_vector(self):
        self.initial_fire_vector = [1] + [0] * (self.len_transitions - 1)
        self.str_initial_fire_vector = " ".join(map(str, self.initial_fire_vector))

    def create_net(self):
        try:
            for net in self.nets:
                self.len_transitions = net.len_transitions
                self.len_places = net.len_places
                self.marking_vector, self.incidence_matrix_t = net.incidence_matrix()
                self.incidence_matrix = [
                    [
                        self.incidence_matrix_t[j][i]
                        for j in range(len(self.incidence_matrix_t))
                    ]
                    for i in range(len(self.incidence_matrix_t[0]))
                ]
                self.numpy_marking_vector = np.array(self.marking_vector)
                self.numpy_inci_matrix_t = np.matrix(self.incidence_matrix_t)

                self.numpy_marking_vector.shape = (self.len_places, 1)
            self._set_incidence_vector()
            self.set_initial_token_vector()
            self.set_initial_fire_vector()
            return "Net successfully created", True
        except Exception as error:
            print(error)
            return "Error Creating Net", False

    def update_pnml(self, fire_vector=list(), token=list(), _type="fire"):
        if _type == "fire":
            if len(fire_vector) == self.len_transitions:
                for net in self.nets:
                    self.fire_vector = fire_vector
                    self.numpy_fire_vector = np.array(self.fire_vector)
                    self.numpy_fire_vector.shape = (self.len_transitions, 1)

                    self.numpy_marking_vector = (
                        self.numpy_marking_vector
                        + self.numpy_inci_matrix_t * self.numpy_fire_vector
                    )
                    self.marking_vector = (
                        self.numpy_marking_vector.transpose().tolist()[0]
                    )

                    net.mount_marking(self.marking_vector)
                    try:
                        write_pnml_file(net, self.file)
                        return "File uploaded successfully", True
                    except Exception:
                        return "Error Sending File", False
            else:
                msg = (
                    f"The Fire Vector has a different size than {self.len_transitions}"
                )
                return msg, False
        elif _type == "token":
            if len(token) == self.len_places:
                for net in self.nets:
                    self.numpy_marking_vector = np.array(token)
                    self.numpy_marking_vector.shape = (self.len_places, 1)
                    self.marking_vector = (
                        self.numpy_marking_vector.transpose().tolist()[0]
                    )
                    self.marking_vector = token

                    net.mount_marking(self.marking_vector)
                    try:
                        write_pnml_file(net, self.file)
                        return "File uploaded successfully", True
                    except Exception:
                        return "Error Sending File", False
            else:
                msg = f"Vector Token with a different size of {self.len_places}"
                return msg, False

    def pnrd_setup(self, filename):
        _, ok = self.set_pnml(filename)
        if ok:
            _, created = self.create_net()
            if created:
                return "Net created successfully", True
            return "Error creating net", False
        return "Error loading file", False

    def create_palms_file(self, palms_data):
        palms_file = FileCreator("palmsSetup", self.file, "setup", "palms")
        palms_file.set_text(json.dumps(palms_data, indent=4, sort_keys=True))

    def create_pnrd_init_file(self, wifi, mqtt):
        self.set_initial_token_vector()

        content = f"""{self.len_places}
{self.len_transitions}
{len(self.incidence_vector)}
{len(self.initial_token_vector)}
{self.str_incidence_vector}
{self.str_initial_token_vector}
{wifi["ssid"]}
{wifi["password"]}
{mqtt["broker"]}
{mqtt["port"]}
{mqtt["username"]}
{mqtt["password"]}
"""

        pnrd_init = FileCreator("palmsSetup", self.file, "pnrd_initData", "txt")
        pnrd_init.set_text(content)

    def create_ipnrd_init_file(self, wifi, mqtt):
        self.set_initial_fire_vector()
        content = f"""{self.len_places}
{self.len_transitions}
{len(self.initial_fire_vector)}
{self.str_initial_fire_vector}
{wifi["ssid"]}
{wifi["password"]}
{mqtt["broker"]}
{mqtt["port"]}
{mqtt["username"]}
{mqtt["password"]}
"""

        ipnrd_init = FileCreator("palmsSetup", self.file, "ipnrd_initData", "txt")
        ipnrd_init.set_text(content)

    def create_pnrd_reader_file(self, readers, wifi, mqtt):
        reader_count = 0
        for e in readers:
            if e["readerName"] == "":
                e["readerName"] = "palms"

            pnrd_readers_file = FileCreator(
                "palmsSetup/{0}".format(e["readerName"]),
                self.file,
                "pnrd_reader",
                "txt",
            )
            content = f"""{self.len_places}
{self.len_transitions}
{reader_count}
{e["readerName"]}
{wifi["ssid"]}
{wifi["password"]}
{mqtt["broker"]}
{mqtt["port"]}
{mqtt["username"]}
{mqtt["password"]}
{e["IP"]}
"""
            pnrd_readers_file.set_text(content)
            reader_count += 1

    def create_ipnrd_reader_file(self, readers, wifi, mqtt):
        for e in readers:
            if e["readerName"] == "":
                e["readerName"] = "palms"
            content = f"""{self.len_places}
{self.len_transitions}
{len(self.incidence_vector)}
{len(self.initial_token_vector)}
{self.str_incidence_vector}
{self.str_initial_token_vector}
{e["readerName"]}
{wifi["ssid"]}
{wifi["password"]}
{mqtt["broker"]}
{mqtt["port"]}
{mqtt["username"]}
{mqtt["password"]}
{e["IP"]}
"""
            ipnrd_readers_file = FileCreator(
                "palmsSetup/{0}".format(e["readerName"]),
                self.file,
                "ipnrd_reader",
                "txt",
            )
            ipnrd_readers_file.set_text(content)

    def decode_pnrd_reader_msg(self, msg):
        try:
            today = date.today()
            now_BR = datetime.now(pytz.timezone("America/Sao_Paulo"))
            date_now = today.strftime("%d-%m-%Y")
            time = now_BR.strftime("%H-%M-%S")
            tag = dict()
            if msg != "":
                _temp = msg.split("-")
                if len(_temp) == 7:
                    for e in _temp:
                        if e.startswith("I"):  # TAG ID
                            tag["id"] = e[1:]
                        elif e.startswith("A"):  # Antena
                            tag["ant"] = e[1:]
                        elif e.startswith("R"):  # Reader
                            tag["readerId"] = e[1:]
                        elif e.startswith("P"):
                            tag["pnrd"] = e[1:]
                        elif e.startswith("T"):
                            if tag["pnrd"] and tag["pnrd"] == "INIT_TAG":
                                tag["token"] = list()
                            else:
                                string_token = e[2:-1]
                                tag["token"] = string_token.split(",")
                                tag["token"] = list(map(int, tag["token"]))
                        elif e.startswith("F"):
                            tag["fire"] = int(e[1:])
                    tag["time"] = time
                    tag["date"] = date_now
                if tag == {}:
                    pass
                else:
                    return tag

        except Exception:
            return "ERROR ON READ"

    def __str__(self):
        str_i_matrix_t = (
            "Incidence Matrix Transpose: \n" + str(self.numpy_inci_matrix_t) + "\n"
        )
        str_marking_vector = "Marking Vetor: \n" + str(self.numpy_marking_vector) + "\n"
        return str_i_matrix_t + str_marking_vector
