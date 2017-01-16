import codecs

def getFileName(navn):
        navn = navn.replace(" ","");
        navn = navn.replace("'","");
        navn = navn.lower();
        navn = "img/team/"+navn+".png";
        return navn
    
teams = ["The Board","Marketing","Control","Electronics","Mechanical"];
teamTxt = [None for x in range(5)]
teamTxt[0] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus leo eget ex vestibulum finibus. Mauris congue lacus quis sodales maximus. Sed efficitur sed enim id elementum. Praesent id feugiat ante. Phasellus quis tortor ac eros tincidunt volutpat nec nec felis. Vestibulum luctus est ut erat rhoncus, ac suscipit erat iaculis."
teamTxt[1] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus leo eget ex vestibulum finibus. Mauris congue lacus quis sodales maximus. Sed efficitur sed enim id elementum. Praesent id feugiat ante. Phasellus quis tortor ac eros tincidunt volutpat nec nec felis. Vestibulum luctus est ut erat rhoncus, ac suscipit erat iaculis."
teamTxt[2] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus leo eget ex vestibulum finibus. Mauris congue lacus quis sodales maximus. Sed efficitur sed enim id elementum. Praesent id feugiat ante. Phasellus quis tortor ac eros tincidunt volutpat nec nec felis. Vestibulum luctus est ut erat rhoncus, ac suscipit erat iaculis."
teamTxt[3] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus leo eget ex vestibulum finibus. Mauris congue lacus quis sodales maximus. Sed efficitur sed enim id elementum. Praesent id feugiat ante. Phasellus quis tortor ac eros tincidunt volutpat nec nec felis. Vestibulum luctus est ut erat rhoncus, ac suscipit erat iaculis."
teamTxt[4] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus leo eget ex vestibulum finibus. Mauris congue lacus quis sodales maximus. Sed efficitur sed enim id elementum. Praesent id feugiat ante. Phasellus quis tortor ac eros tincidunt volutpat nec nec felis. Vestibulum luctus est ut erat rhoncus, ac suscipit erat iaculis."

f = codecs.open("../data/team.json","r","utf-8")
data = f.read()
json = eval(data)
f.close()


def getTeam(json,tabs):
    print(len(json))
    html = "";
    
    for i in range(len(json)):
        html += tabs*"\t"+"<div class='team'>\n"
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

        print("i",i)
        for m in range(1,len(json[i])):
            print("m",m)
            html += tabs*"\t"+"\t\t<div class='member'>\n"
            html += tabs*"\t"+"\t\t\t<img src='"+getFileName(json[i][m]["navn"])+"'>\n"
            html += tabs*"\t"+"\t\t\t<h3>"+json[i][m]["navn"]+"</h3>\n"
            html += tabs*"\t"+"\t\t\t<p>"+json[i][m]["rolle"]+"<br>Hometown : "+json[i][m]["hjemby"]+"</p>\n"
            html += tabs*"\t"+"\t\t</div>\n"

        html += tabs*"\t"+"\t</div>\n"
        html += tabs*"\t"+"</div>\n"
    return html
        

html = getTeam(json,1)
        

def insertInTag(file,tag,idOrClass):
    f = codecs.open(file,"r","utf-8")
    #print(html)
    target = f.read()
    #print(target)
    f.close()
    
    before = target[:(target.index("<"+tag+ bool(idOrClass)*(' '+idOrClass) +">")+(len(tag)+len(idOrClass)+3))] + "\n"
    after = target[target.index("</"+tag+">"+bool(idOrClass)*("<!--"+idOrClass+"-->")):]
    newHTML = before + html + after
    
    #print(newHTML)
    f = codecs.open(file,"w","utf-8")
    f.write(newHTML)
    f.close()

insertInTag("../team.html","div",'class="align"')
