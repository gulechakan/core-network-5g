#!/usr/bin/python

tourDescription = """
### Bring up an end-to-end 5G network with OpenAirInterface5G

This profile was created by Dustin Maas.

It deploys a single compute node with a disk image that includes docker,
docker-compose, tshark, and docker images for all of the OAI 5G core network 
functions. It also includes source code and a prebuilt version of the OAI RAN 
(gNB, nrUE, RF simulator).

To use this profile, you should have reserved a `d430` server at Emulab in 
advance.

"""

tourInstructions = """

Note: After you instantiate an experiment, you have to wait until the POWDER
portal shows your experiment status in green as "Your experiment is ready"
before proceeding.


"""


import geni.portal as portal
import geni.rspec.pg as rspec
import geni.urn as URN
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN
import geni.rspec.emulab as emulab

pc = portal.Context()
request = pc.makeRequestRSpec()

# Optional physical type for all nodes.
pc.defineParameter("phystype",  "Optional hardware type",
                   portal.ParameterType.STRING, "d430",
                   longDescription="Specify hardware type (d430 or d820)")

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()
pc.verifyParameters()

node = request.RawPC("node")
node.hardware_type = params.phystype
node.disk_image = "urn:publicid:IDN+emulab.net+image+mww2023:oai-cn5g-rfsim"
node.startVNC()

tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

portal.context.printRequestRSpec()




# #!/usr/bin/python
 
 # tourDescription = """
 # ### Bring up an end-to-end 5G network with OpenAirInterface5G
 
 # This profile was created by Dustin Maas.
 
 # It deploys a single compute node with a disk image that includes docker,
 # docker-compose, tshark, and docker images for all of the OAI 5G core network 
 # functions. It also includes source code and a prebuilt version of the OAI RAN 
 # (gNB, nrUE, RF simulator).
 
 # To use this profile, you should have reserved a `d430` server at Emulab in 
 # advance.
 
 # """
 
 # tourInstructions = """
 
 # Note: After you instantiate an experiment, you have to wait until the POWDER
 # portal shows your experiment status in green as "Your experiment is ready"
 # before proceeding.
 
 
 # """
 
 
 # import geni.portal as portal
 # import geni.rspec.pg as rspec
 # import geni.urn as URN
 # import geni.rspec.igext as IG
 # import geni.rspec.emulab.pnext as PN
 # import geni.rspec.emulab as emulab
 
 # pc = portal.Context()
 # request = pc.makeRequestRSpec()
 
 # # Optional physical type for all nodes.
 # pc.defineParameter("phystype",  "Optional hardware type",
 #                    portal.ParameterType.STRING, "d430",
 #                    longDescription="Specify hardware type (d430 or d820)")
 
 # # Retrieve the values the user specifies during instantiation.
 # params = pc.bindParameters()
 # pc.verifyParameters()
 
 # core = request.RawPC( "core" )
 # core.hardware_type = params.phystype
 # core.disk_image = "urn:publicid:IDN+emulab.net+image+mww2023:oai-cn5g-rfsim"
 # core.startVNC()
 
 # iface_core = core.addInterface('interface-core', rspec.IPv4Address('10.10.1.1','255.255.255.0'))
 
 # ran = request.RawPC( "ran" )
 # ran.hardware_type = params.phystype
 # ran.disk_image = "urn:publicid:IDN+emulab.net+image+mww2023:oai-cn5g-rfsim"
 # ran.startVNC()
 # iface_ran = ran.addInterface('interface-ran', rspec.IPv4Address('10.10.1.2','255.255.255.0'))
 
 # link = request.Link('link')
 # link.addInterface(iface_core)
 # link.addInterface(iface_ran)
 
 
 # tour = IG.Tour()
 # tour.Description(IG.Tour.MARKDOWN, tourDescription)
 # tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
 # request.addTour(tour)
 
 # portal.context.printRequestRSpec()