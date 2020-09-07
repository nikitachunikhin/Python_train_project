def days_represented(trips):
    for i in range(0, len(trips)):
        for j in range(i+1, len(trips)):
            if i<len(trips) and j<len(trips):
                trip1=trips[i]
                trip2=trips[j]
                print(f"trip1={trip1}")
                print(f"trip2={trip2}")
                print('')
                if trip1[0]>trip2[0] and trip1[1]<trip2[1]:
                    trips.pop(i) #удаляем трип1 так как он полностью входит в трип2
                elif trip1[0]<trip2[0] and trip1[1]>trip2[1]:
                    trips.pop(j) #удаляем трип2 так как он полностью входит в трип1
                elif trip1[0]<trip2[0] and trip1[1]<trip2[1] and trip2[0]<trip1[1]:
                    trips.pop(i)
                    trips.pop(j)
                    trips.append([trip1[0], trip2[1]])
                elif trip1[0]>trip2[0] and trip1[1]>trip2[1] and trip2[1]>trip1[0]:
                    trips.pop(i)
                    trips.pop(j)
                    trips.append([trip2[0], trip1[1]])
    # return trips
    #TODO: Просумировать интервалы масива трипс

if __name__ == '__main__':
    trips = [[2,8], [220,229],[6,16],[50,67]]
    res = days_represented(trips)
    print(res)