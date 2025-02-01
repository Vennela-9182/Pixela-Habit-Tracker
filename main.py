from http.client import responses
from time import strptime

import requests
from _datetime import datetime
pixel_url="https://pixe.la/v1/users"
USERNAME="vennela"
TOKEN="hjikytweghjtyul"
newToken="tyrewnuibdghrtuio"
parameters={
    "token":"hjikytweghjtyul",
    "username":"vennela",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#response=requests.post(url=pixel_url,json=parameters)
ID="graph1"
graph_url=f"{pixel_url}/{USERNAME}/graphs"
headers={
"X-USER-TOKEN":"tyrewnuibdghrtuio"
}
graph_params={

    "id":ID,
    "name":"Cycle graph",
    "unit":"km",
    "type":"int",
    "color":"sora"
}
#response1=requests.post(url=graph_url,json=graph_params,headers=headers)
#print(response1.text)



adding_values_graph_url=f"{pixel_url}/{USERNAME}/graphs/{ID}"
today=datetime.now()
#print(today.strftime('%Y%m%d'))

quantity=5
adding_values_graph={
    "date":today.strftime('%Y%m%d').strip(),
    "quantity":"5"
}
#response2=requests.post(url=adding_values_graph_url,json=adding_values_graph,headers=headers)
#print(response2.text)

update_url=f"{pixel_url}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
update_params={
    "quantity":"7"
}
#response3=requests.put(update_url,json=update_params,headers=headers)
#print(response3.text)

delete_url=f"{pixel_url}/{USERNAME}"
response4=requests.delete(delete_url,headers=headers)
print(response4.text)