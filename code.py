#WAP-create a dictonary out of  the following list
colours=["yellow","blue","black","orange","white"]
colour_dist=dict();
position=1

for item in colours:
    colour_dist[position]=item;
    print(colour_dist)
    position+=1
print(colour_dist)