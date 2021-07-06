import valve.source
import valve.source.a2s
import valve.source.master_server
print ("Start")
#with valve.source.master_server.MasterServerQuerier() as msq:
    #print("passed with 1")
    #try:
        #print("into try 1")
        #for address in msq.find(region="na",                           
                                  #map="ctf_2fort"):#find returns (host,port) tuple from master server
           # print (address)
          #  print("in for loop")
  # except valve.source.NoResponseError:
        #print("Master server request timed out!")

address = ('85.190.152.82' , 27015) #port 27015 is right do not use port 7777
try: #(85.190.152.82,7777)
    with valve.source.a2s.ServerQuerier(address) as server:
         info = server.info()
         players = server.players()

    

except valve.source.NoResponseError:
         print("Server {}:{} timed out!".format(*address))
         #continue


displayListName = []

for player in players["players"]:
        if player["name"]:
            displayListName.append(player)
            duraSec = int(player["duration"])
            duraMin = duraSec/60
            duraHour = duraMin
            print ("{name} has been online for ".format(**player)  + str(duraHour) + " hours.")
            #for player in sorted(players["players"],
             #                    key=lambda p: p["score"], reverse=True):
                #print("{score} {name}".format(**player))
player_count = len(displayListName)

print (str(player_count) + "/70 players are online" ) 
print("{server_name}".format(**info))
   # except valve.source.NoResponseError:
       # print("Master server request timed out!")
		
