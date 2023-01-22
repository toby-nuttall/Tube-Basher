#this section takes user input:
station1 = str(input("start:"))
station2 = str(input("end:"))

all_stations = ["s1","s2","s3","s4","p1","p2","p3","p4"]

#this is a command that checks the user inputs exist
x1 = 0
x2 = 0
for i in range(0,len(all_stations)):
    if station1 == all_stations[i]:
        x1 = 1
    elif station2 == all_stations[i]:
        x2 = 1
if x1 == 0 or x2 == 0:
    print("one or both of your stations do not exist (try no caps)")
    exit()

class underground():

    def __init__(self):
        self.lines = []
        self.type1_lines = []
        self.type2_lines = []
    
    def add_line(self,Line):
        self.lines.append(Line)
    
    def search_all(self):
        for i in range(0,len(self.lines)):
            self.lines[i].search()
    
    def add_type1_line(self,Line):
        self.type1_lines.append(Line)
        
    def add_type2_line(self,Line):
        self.type2_lines.append(Line)
    
    def go_compare(self):
        self.search_all()
        for i in range(0,len(self.type2_lines)):
            for j in range(0,len(self.type1_lines)):
                self.type2_lines[i].compare(self.type1_lines[j])


class line():
    
    def __init__(self,stations,name,railway):
        self.railway = railway
        self.stations = stations
        self.name = name
        self.railway.add_line(self)
        
        #the tube can go in either direction so add the reverse of each line
    def reverse_line(self):
        stations_reversed = self.stations.reverse()
        reverse_line = line(stations_reversed,self.name,self.railway)
        
    

    #defining a search command that checks if either of the input stations are in a line 
    #and prints the line if both are present in that line
    def search(self):
        self.reverse_line()
        counter1 = 0
        counter2 = 0
        start = 0
        stop = 0
        
        for i in range(0,len(self.stations)):
            if (self.stations[i]) == station1:
                counter1 = 1
                start = i
                cut1_stations = self.stations[i:]

            elif (self.stations[i]) == station2:
                counter2 = 1
                stop = i + 1
                cut2_stations = self.stations[:i+1]

        if counter1 == 1 and counter2 == 1:
            cut3_stations = self.stations[start:stop]
            print(f"{self.name}: {cut3_stations}")
        
        elif counter1 == 1 and counter2 == 0:
            type1 = line(cut1_stations,self.name,self.railway)
            self.railway.add_type1_line(type1)
            
        elif counter1 == 0 and counter2 == 1:
            type2 = line(cut2_stations,self.name,self.railway)
            self.railway.add_type2_line(type2)

    def compare(self,other):
        for i in range(0,len(self.stations)):
            for j in range(0,len(other.stations)):
                if self.stations[i] == other.stations[j]:
                    stationlist2 = self.stations[i:]
                    stationlist1 = other.stations[:j+1]
                    print(f"{other.name}: {stationlist1} then {self.name}: {stationlist2}")
                    break


#building the london underground
Underground = underground()

picadilli = line(["p1","p2","p3","p4","s1","s2"],"picadilli",Underground)
circle_line = line(["s1","s2","s3","s4"],"circle line",Underground)

#calling the funtions
Underground.go_compare()


