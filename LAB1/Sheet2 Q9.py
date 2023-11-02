departure_time = input("Enter the departure time: ")
arrival_time = input("Enter the arrival time: ")

departure_hour, departure_minute = departure_time.split(":")

arrival_hour, arrival_minute = arrival_time.split(":")
tminutes = (int(arrival_hour) - int(departure_hour)) * 60 + (int(arrival_minute) - int(departure_minute))

triphours = tminutes // 60
tripminutes = tminutes % 60
print("The trip time is {} hours and {} minutes.".format(triphours, tripminutes))