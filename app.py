from flask import Flask, request, jsonify, render_template_string, render_template

app = Flask(__name__)

import http.client
import json
import os



#for i in range(100):
#  print(dataapi["results"][i]['poster'])
#        dataapi["results"][i]["poster"]

@app.route("/")
def home():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'latest.json')

    with open(f"{file_path}",'r') as f:
        dataapi = json.load(f)
        f.close()
    

    target = {}
    for i in range(len(dataapi['results'])):
        netrating = dataapi['results'][i]['rating']
        if netrating != "":
            target[i] = float(netrating)
        else:
            target[i] = 11
        sorted_target = dict(sorted(target.items(), key=lambda item: item[1], reverse=True))


    msg = ""
    msg = msg + "<div class= 'image-container'>"
    #msg = msg+"hello everyone!"
    #print(int(dataapi["Object"]["total"]/100))
    
    for i in list(sorted_target.keys()):
        #print("{}".format(dataapi["results"][i]["poster"]))
        net_id = dataapi['results'][i]['netflix_id']
        web_addr = "https://www.netflix.com/watch/"
        web_addr += str(net_id)
        #print(web_addr)
        #input()
        msg = msg + "<div class= 'scaling'><br>"
        msg = msg + "<a href ="
        msg = msg + "{}".format(web_addr)
        msg = msg + " >"
        msg = msg + " <img  src= "
        msg += "{}".format(dataapi['results'][i]["img"])
        msg=msg+" > </a>"
        msg=msg+"<div class='info-overlay'>"
        msg+= "IMDB Rating: "
        if target[i] == 11:
            msg += " await "
        else:
            msg += "{}".format(dataapi["results"][i]["rating"])
        msg +="<br>"
        msg += "{}".format(dataapi['results'][i]['synopsis'])
        msg += "</div>"
        msg = msg +"</div>" 
    
    msg = msg + "</div>" 





    return render_template("index.html",msg=msg)

@app.route('/submit_data', methods=['GET','POST'])
def submit_d():
    data = request.form
#    name = data.get('name')
#    email = data.get('email')
    imdb = data.get('imdb')
    show = data.get('TypeofShow')
    genre = data.get('Genre')
    #print("Rating is: ",imdb)
    #print("imdb and genre are: ",imdb,genre)
    
    """
    print("Just after the gets")
    
    conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "59ce401ee0msh90157ee3be78c4bp184c49jsne85badb13d29",
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com"
    }

    print("Just before api call...")
    
    conn.request("GET", f"/search/titles?country_list=46&offset=0&order_by=date&start_rating=1", headers=headers)
    res = conn.getresponse()
    datapi = res.read()
    datapi = json.loads(datapi)
    with open('output.json', 'a') as f:
        json.dump(datapi, f)
        
    #with open('output.json','r') as f:
    #   dataapi = json.load(f)
    #   f.close()
    
    max = int(datapi["Object"]["total"]/100)

    print("Max is: ",max)
    
    for i in range(1,2,1):
        conn.request("GET", f"/search/titles?country_list=46&offset={i}&order_by=date&start_rating=1", headers=headers)
        res = conn.getresponse()
        datapi = res.read()
        datapi = json.loads(datapi)
        with open('output.json', 'a') as f:
            json.dump(datapi, f)

    f.close()    
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'flixdata.json')

    #print(os.listdir(current_directory))
    #print("File Path is: ",file_path)
    
    #print("cause interrupt")
    #input()

    with open(f"{file_path}",'r') as f:
        dataapi = json.load(f)
        f.close()
    
    # Test 070225

    #with open("genre_lookup.json","r") as h:
    #    gen = json.load(h)
    #    h.close()

    #genkeys = list(gen.keys())

    #print(genkeys)

    #if genre in genkeys:
    #    print("Yes genre in here!")
    
    
    file_path = os.path.join(current_directory, 'nettogen.json')
    with open(f"{file_path}","r") as g:
        netgen = json.load(g)
        g.close()
    
    max = len(dataapi['results'])

    #print("MAX is: ",max)

    target = {}
    for i in range(max):
        netid = dataapi['results'][i]['netflix_id']
        showtype = dataapi['results'][i]['title_type']
        netrating = dataapi['results'][i]['rating']
        #print(netgen[f"{netid}"])
        if ((showtype == show) & (float(netrating) >= float(imdb)) & (genre in netgen[f"{netid}"])):
            target[i] = float(netrating)

        
        sorted_target = dict(sorted(target.items(), key=lambda item: item[1], reverse=True))

        """
        print(show, showtype, genre)
        print(netrating,imdb)
        print(target)
        """






        


              




    
    # Process received data
    #if not name or not email:
    #    return jsonify({"message": "Invalid input"}), 400
    
    #print("Rating is: ",imdb)
    #print("Showtype is: ",show)
    #print("Genre is: ",genre)
    
    #print("Check type of dataapi and value of 3895: ")
    #print(type(dataapi))

    #print(dataapi['results'][3889]['title'])

    #print("Hang here!")
    #input()
    # Respond back
    # ----
    #
    #for i in range(10):
    #    print(dataapi["results"][i]["poster"])
    

    msg = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <head>
    <style>
      body {background-color: lightcyan;}
      p {color: black;}
      h1 {color: maroon;}
      .image-container {display: flex; 
       flex-wrap: wrap;}
      .image-container img {
         width: 200px; 
         height: auto; 
         margin: 40px;  }

      .info-overlay {
         position: relative;
         bottom: 0;
         left: 0;
         right: 0;
         background: rgba(0,0,0,0.7);
         color: #ff0;
         padding: 10px;
         text-align: center;
         width: 250px;
         word-wrap: break-word;  
         opacity: 0;
         transform: translateY(100%);
         transition: opacity 0.3s ease, transform 0.3s ease;}

        .scaling:hover .info-overlay {
          opacity: 1;
          transform: translateY(0);}


      .scaling:hover img {
         transform: scale(1.4);
         transition: transform 0.3s ease}

    </style>
    </head>
    <body> 
    <br>
    """
    #print("START....")
    
    
    msg = msg + "<div class= 'image-container'>"
    #msg = msg+"hello everyone!"
    #print(int(dataapi["Object"]["total"]/100))
    
    for i in list(sorted_target.keys()):
        #print("{}".format(dataapi["results"][i]["poster"]))
        net_id = dataapi['results'][i]['netflix_id']
        web_addr = "https://www.netflix.com/watch/"
        web_addr += str(net_id)
        #print(web_addr)
        #input()
        msg = msg + "<div class= 'scaling'><br>"
        msg = msg + "<a href ="
        msg = msg + "{}".format(web_addr)
        msg = msg + " >"
        msg = msg + " <img  src= "
        msg += "{}".format(dataapi['results'][i]["img"])
        msg=msg+" > </a>"
        msg=msg+"<div class='info-overlay'>"
        msg+= "IMDB Rating: "
        msg += "{}".format(dataapi["results"][i]["rating"])
        msg +="<br>"
        msg += "{}".format(dataapi['results'][i]['synopsis'])
        msg += "</div>"
        msg = msg +"</div>" 
    
    msg = msg + "</div> </body> </HTML>" 
    #print("HERE IS msg: ")
    #msg = "This is the Response!"
    #print(msg)
     #return jsonify({"message": f"Hello {name}, your email {email} was received successfully!"})
    return render_template_string(msg);
    #return (msg)

if __name__ == '__main__':
    app.run(debug=True)
