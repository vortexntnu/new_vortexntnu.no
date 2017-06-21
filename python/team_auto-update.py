import codecs


def getFileName(name):
        name = name.replace(" ", "")
        name = name.replace("'", "")
        name = name.lower()
        name = "img/team/team"+year+"/"+name+".png"
        return name
    

year = "2016"
teams = ["Management", "Marketing", "Mechanical", "Electronics", "Control and Communication", "Manipulator"]
# teams = ["The Board","Marketing","Control","Electronics","Mechanical"];
teamTxt = [None for x in range(len(teams))]

teamTxt[0] = "The management is responsible for coordinating the project and securing a sustainable development of the organization. Their involvement ensures close cooperation between the respective group leaders, and the team’s overall progression, budget and wellbeing."
teamTxt[1] = "The marketing group is responsible for establishing sponsorship agreements as well as follow-ups. The efforts involve exposure of our activities and partners on campus, to the industry and during the competition. This includes marketing and public relations, management of our website and social media profiles."
teamTxt[2] = "The mechanical group is responsible for designing and manufacturing a unified waterproof ROV frame construction. This includes 3D modelling in CAD, making payloads, production of buoyancy elements and competition props."
teamTxt[3] = "The electronics group is responsible for the mapping and packaging of the entire electronic system. The work includes development of mission-specific sensors, circuit boards, and the control unit."
teamTxt[4] = "The control and communication group is responsible for maneuverability and stability of the ROV allowing the pilot to perform the tasks consistently and reliably. The work spans from system architecture design, writing embedded software to control the thrusters, programming the dynamic positioning system, and ensuring seamless communication between topside and the ROV is established."
teamTxt[5] = "The manipulator group is responsible for the design and production of a capable manipulator arm that can pick up and handle objects. The arm is an essential and critical part of the ROV allowing it to complete tasks assigned in the MATE competition."

# teamTxt[0] = "The Board is responsible for coordinating the project and securing a sustainable development of the organization. Their involvement ensures close cooperation between the respective group leaders, and the team’s overall progression, budget and wellbeing."
# teamTxt[1] = "The Marketing group is responsible for the overall branding and profiling of the organization. This includes organizing the website, social media, stands, events, sponsors, media outreach, as well as outlining the market display and product presentation for the actual contest."
# teamTxt[2] = "The Control System group is responsible for developing software that makes it possible for the pilot to control the ROV in an easy, predictable, and reliable way. The responsibilities of the team include essentially all software between the inputs of the pilot, the data gathered by the sensors, and the outputs to the thrusters and manipulator arm."
# teamTxt[3] = "The Electronics group is responsible for the mapping and packaging of the entire electronic system from scratch. The work range from designing custom PCBs to assembling the finished hardware system. This includes optimizing the solutions, as well as troubleshooting it all when it does not work."
# teamTxt[4] = "The Mechanical group is responsible for developing a waterproof ROV frame construction. This includes 3D modeling, CFD, coordination of manufacturing, designing thrusters, customizing buoyancy elements, as well as integrating the thrusters and cameras to the overall design. The work also includes development of a capable manipulator arm, which is a critical part og the ROV - allowing us to complete the challenging tasks assigned in the competition."

f = codecs.open("../data/team" + year + ".json", "r", "utf-8")
data = f.read()
json = eval(data)
f.close()


def getTeam(json, tabs):
    html = ""
    
    for i in range(len(json)):
        html += tabs*"\t"+"<div class='group'>\n"
        html += tabs*"\t"+"\t<div class='top'>\n"
        html += tabs*"\t"+"\t\t<div class='member'>\n"
        html += tabs*"\t"+"\t\t\t<img src='"+getFileName(json[i][0]["navn"])+"'>\n"
        html += tabs*"\t"+"\t\t\t<h3>"+json[i][0]["navn"]+"</h3>\n"
        html += tabs*"\t"+"\t\t\t<p>"+json[i][0]["rolle"]+"<br>Hometown : "+json[i][0]["hjemby"]+"</p>\n"
        html += tabs*"\t"+"\t\t</div>\n"
        html += tabs*"\t"+"\t\t<div class='info'>\n"
        html += tabs*"\t"+"\t\t\t<h2>"+teams[i]+"</h2>\n"
        html += tabs*"\t"+"\t\t\t<p>"+teamTxt[i]+"</p>\n"
        html += tabs*"\t"+"\t\t</div>\n"
        html += tabs*"\t"+"\t</div>\n"
        html += tabs*"\t"+"\t<div class='bot'>\n"

        for m in range(1, len(json[i])):
            html += tabs*"\t"+"\t\t<div class='member'>\n"
            html += tabs*"\t"+"\t\t\t<img src='"+getFileName(json[i][m]["navn"])+"'>\n"
            html += tabs*"\t"+"\t\t\t<h3>"+json[i][m]["navn"]+"</h3>\n"
            html += tabs*"\t"+"\t\t\t<p>"+json[i][m]["rolle"]+"<br>Hometown : "+json[i][m]["hjemby"]+"</p>\n"
            html += tabs*"\t"+"\t\t</div>\n"

        html += tabs*"\t"+"\t</div>\n"
        html += tabs*"\t"+"</div>\n"
    return html
        

html = getTeam(json, 3)
print(html)


def insertInTag(file, tag, idOrClass):
    f = codecs.open(file, "r", "utf-8")
    # print(html)
    target = f.read()
    # print(target)
    f.close()
    
    before = target[:(target.index("<"+tag+bool(idOrClass)*(' '+idOrClass)+">")+(len(tag)+len(idOrClass)+3))]+"\n"
    after = target[target.index("</"+tag+">"+bool(idOrClass)*("<!--"+idOrClass+"-->")):]
    newHTML = before + html + after
    
    # print(newHTML)
    f = codecs.open(file, "w", "utf-8")
    print(newHTML)
    f.close()

# insertInTag("../team.html","div",'class="align"')
