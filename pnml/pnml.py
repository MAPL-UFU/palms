import os, sys

from .PetriNet import PetriNet
from .Place import Place
from .Transition import Transition
from .Arc import Arc
import xml.etree.ElementTree as elemTree # XML parser

def parse_pnml_file(file):
    """ This method parse all Petri nets of the given file.

    This method expects a path to a VipTool pnml file which
    represent a Petri net (.pnml), parse all Petri nets
    from the file and returns the Petri nets as list of PetriNet
    objects.

    XML format:
    <pnml>
      <net id="...">
        (<page>)
        <name>
          <text>name of Petri net</text>
        </name>
        <transition id="...">
          <name>
            <text>label of transition</text>
            <graphics>
              <offset x="0" y="0"/>
            </graphics>
          </name>
          <graphics>
            <position x="73" y="149"/>
          </graphics>
        </transition>
        ...
        <place id="...">
          <name>
            <text>label of transition</text>
            <graphics>
              <offset x="0" y="0"/>
            </graphics>
          </name>
          <graphics>
            <position x="73" y="149"/>
          </graphics>
          <initialMarking>
            <text>1</text>
          </initialMarking>
        </place>
        ...
        <arc id="..." source="id of source event" target="id of target event">
          <inscription>
            <text>1</text>
          </inscription>
        </arc>
        ...
        (</page>)
      </net>
      ...
    </pnml>
    """

    tree = elemTree.parse(file) # parse XML with ElementTree
    root = tree.getroot()

    nets = [] # list for parsed PetriNet objects

    #xmlns = '{http://www.pnml.org/version-2009/grammar/pnml}' not working
    xmlns = ''

    for net_node in root.iter(xmlns+'net'):
        # create PetriNet object
        net = PetriNet()
        net.id = net_node.get('id')
        netnmnode = net_node.find('./'+xmlns+'name/'+xmlns+'text')
        if netnmnode is not None:
             net.name = netnmnode.text
        else:
             net.name = net.id


        # and parse transitions
        for transition_node in net_node.iter(xmlns+'transition'):
            transition = Transition()
            transition.id = transition_node.get('id')
            transition.label = transition.id if transition_node.find('./name/text')== None else transition_node.find('./name/text').text
            position_node = transition_node.find('./graphics/position')
            transition.position = [int(float(position_node.get('x'))), int(float(position_node.get('y')))]
            off_node = transition_node.find('./'+xmlns+'name/'+xmlns+'graphics/'+xmlns+'offset')
            if off_node == None :
                transition.offset = [0,0]
            else :
                transition.offset = [int(off_node.get('x')), int(off_node.get('y'))]
            net.transitions[transition.id] = transition


        # and parse places
        for place_node in net_node.iter(xmlns+'place'):
            place = Place()
            place.id = place_node.get('id')
            place.label = place.id if place_node.find('./'+xmlns+'name/'+xmlns+'text')== None else place_node.find('./'+xmlns+'name/'+xmlns+'text').text
            position_node = place_node.find('./'+xmlns+'graphics/'+xmlns+'position')
            place.position = [int(float(position_node.get('x'))), int(float(position_node.get('y')))]

            off_node = place_node.find('./'+xmlns+'name/'+xmlns+'graphics/'+xmlns+'offset')
            if off_node == None :
                place.offset = [0,0]
            else :
                place.offset = [int(off_node.get('x')), int(off_node.get('y'))]

            place.marking = 0 if place_node.find('./initialMarking/text')== None else int(place_node.find('./initialMarking/text').text)
            net.places[place.id] = place

        # and arcs
        for arc_node in net_node.iter(xmlns+'arc'):
            arc = Arc()

            arc.id = arc_node.get('id')
            arc.source = arc_node.get('source')
            arc.target = arc_node.get('target')
            arc.type = arc_node.get('type')
            if arc.type is None:
                etp = arc_node.find('./'+xmlns+'type')
                if etp is not None:
                    arc.type = etp.get('value')
                if arc.type is None:
                    arc.type = 'normal'
            inscr_txt = arc_node.find('./'+xmlns+'inscription/'+xmlns+'text')
            if inscr_txt is not None:
                arc.inscription = inscr_txt.text
            else:
                arc.inscription = "1"


            net.arcs.append(arc)

            nets.append(net)
            arc.net = net

    return nets

def write_pnml_file(n, filename, relative_offset=True):
    pnml = elemTree.Element('pnml')
    net = elemTree.SubElement(pnml, 'net', id=n.id)
    net_name = elemTree.SubElement(net, 'name')
    net_name_text = elemTree.SubElement(net_name, 'text')
    net_name_text.text = n.name

    page = elemTree.SubElement(net, 'page', id='1')

    for _id, t in n.transitions.items():
        transition = elemTree.SubElement(page, 'transition', id=t.id)
        transition_name = elemTree.SubElement(transition, 'name')
        transition_name_text = elemTree.SubElement(transition_name, 'text')
        transition_name_text.text = t.label
        transition_name_graphics = elemTree.SubElement(transition_name, 'graphics')
        transition_name_graphics_offset = elemTree.SubElement(transition_name_graphics, 'offset')
        transition_name_graphics_offset.attrib['x'] = str(t.offset[0])
        transition_name_graphics_offset.attrib['y'] = str(t.offset[1])
        transition_graphics = elemTree.SubElement(transition, 'graphics')
        transition_graphics_position = elemTree.SubElement(transition_graphics, 'position')
        transition_graphics_position.attrib['x'] = str(t.position[0] if t.position is not None else 0)
        transition_graphics_position.attrib['y'] = str(t.position[1] if t.position is not None else 0)

    for _id, p in n.places.items():
        place = elemTree.SubElement(page, 'place', id=p.id)
        place_name = elemTree.SubElement(place, 'name')
        place_name_text = elemTree.SubElement(place_name, 'text')
        place_name_text.text = p.label
        place_name_graphics = elemTree.SubElement(place_name, 'graphics')
        place_name_graphics_offset = elemTree.SubElement(place_name_graphics, 'offset')
        place_name_graphics_offset.attrib['x'] = str(p.offset[0] if p.offset is not None else 0)
        place_name_graphics_offset.attrib['y'] = str(p.offset[1] if p.offset is not None else 0)
        place_name_graphics_offset.attrib['x'] = str(p.offset[0] if p.offset is not None else 0)
        place_name_graphics_offset.attrib['y'] = str(p.offset[1] if p.offset is not None else 0)
        place_graphics = elemTree.SubElement(place, 'graphics')
        place_graphics_position = elemTree.SubElement(place_graphics, 'position')
        place_graphics_position.attrib['x'] = str(p.position[0] if p.position is not None else 0)
        place_graphics_position.attrib['y'] = str(p.position[1] if p.position is not None else 0)
        place_initialMarking = elemTree.SubElement(place, 'initialMarking')
        place_initialMarking_text = elemTree.SubElement(place_initialMarking, 'text')
        place_initialMarking_text.text = str(p.marking)

    for e in n.arcs:
        arc = elemTree.SubElement(page, 'arc', id=e.id, source=e.source, target=e.target, type=e.type)
        arc_inscription = elemTree.SubElement(arc, 'inscription')
        arc_inscription_text = elemTree.SubElement(arc_inscription, 'text')
        arc_inscription_text.text = str(e.inscription)

    tree = elemTree.ElementTree(element=pnml)
    tree.write(filename, encoding="utf-8", xml_declaration=True, method="xml")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nets = parse_pnml_file(sys.argv[1])
        
        for net in nets:
            print(net)


