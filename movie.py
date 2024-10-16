import csv
data = []

with open(r"C:\Users\vrusn\Downloads\movieRatings - Sheet1.csv", 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    while(True):
        answer = input("Add New Rating: rate\nView All Ratings: view all\nEnd Program: end\nType Here: ")
        print("-------------------")
        if(answer == "rate"):
            newRating = []
            title = input("Enter title: ")
            veronicaRating = input("Veronica's Rating: ")
            seanRating = input("Sean's Rating: ")
            newRating.append(title)
            newRating.append(veronicaRating)
            newRating.append(seanRating)
            data.append(newRating)
            writer.writerows(data)
            data = []
        elif(answer == "view all"):
            csvfile.seek(0)
            print(csvfile.read() + "\n")
        elif(answer == "end"):
            break



