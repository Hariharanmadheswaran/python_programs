
class taxi():

    def __init__(self,num_taxi,num_of_stops):
        self.num_taxi=[*range(1,num_taxi+1)]
        self.num_of_stops=num_of_stops
        self.position=[[] for i in range(self.num_of_stops)]
        self.position[0]=[*range(1,num_taxi+1)]
        self.earning=[0]*num_taxi
        self.free_taxi=[0]*num_taxi
        self.free_time=[0]*num_taxi


    def charges(self,kms):
        if kms<6:
            return 100
        return (kms-5)*10 + 100

    def check_free_taxi(self,start,end):
        if len(self.position[start])==1:

            if self.free_taxi[self.position[start][0]-1]==0:
                return self.position[start][0]
            else:
                return None

        elif len(self.position[start])>1:
            min=1000
            book_taxi=None
            for i in self.position[start]:
                # print(i)
                if self.free_taxi[i-1]==1:
                    continue
                if self.earning[i-1]<min:
                    min=self.earning[i-1]
                    book_taxi=i
            return book_taxi
        return None

    def booking(self,start,end,time_now):

        self.make_free(time_now)

        taxi=self.check_free_taxi(start-1,end-1)

        their_ini=start-1
        if taxi is None:
            taxi,their_ini= self.check_nearby(start-1,end-1)
        print("YOUR TAXI CAR NUMBER IS ",taxi)
        self.free_taxi[taxi-1]=1

        self.position[their_ini]=[i for i in self.position[their_ini] if i!=taxi ]
        self.position[end-1].append(taxi)
        self.free_time[taxi-1]=abs(end-start)+time_now
        self.earning[taxi-1]+=self.charges(abs(end-start)*15)

        self.display_taxis(time_now)

    def make_free(self,time):
        for i in range(len(self.free_time)):
            if time>=self.free_time[i]:
                self.free_taxi[i]=0


    def check_nearby(self,start,end):
        middle=start
        left=middle-1
        right=middle+1
        while left>=0 and right<=self.num_of_stops-1:

            if self.check_free_taxi(left,end) is None:
                left-=1
            else:
                return self.check_free_taxi(left,end),left

            if self.check_free_taxi(right,end) is None:
                right+=1
            else:
                return self.check_free_taxi(right,end).right
        while left>=0 :
            if self.check_free_taxi(left,end) is None:
                left-=1
            else:
                return self.check_free_taxi(left,end),left
        while right >= self.num_of_stops-1:
            if self.check_free_taxi(right, end) is None:
                right += 1
            else:
                return self.check_free_taxi(right,end),right

    def display_taxis(self,time_now):
        get_position=[0]*len(self.num_taxi)
        for i in range(len(self.position)):

            if self.position[i]==[]:
                continue
            else:
                for j in self.position[i]:
                    get_position[j-1]=i+1

        print("--"*20)
        print("TAXI_NO    THEIR EARNINGS    THEIR LOCATION    AT TIME     FREE TIME     IS BUSY?")
        for i in range(len(self.num_taxi)):
            # print(i + 1," "*8,self.free_taxi[i]," "*8,self.earning[i]," "*12,get_position[i]," "*12,time_now)
            print(f"{i + 1} {self.earning[i]:{15}},{get_position[i]:{20}},{time_now:{13}}hrs {self.free_time[i]:{13}}  {self.free_taxi[i]:{10}}")
        print("--" * 20)

if __name__=="__main__":
    number_of_taxi=5
    number_of_stops=10
    obj=taxi(number_of_taxi,number_of_stops)
    while True:

        print("press 'q' to exit.... or 's' to continue")
        inp=input()
        if inp=="q":
            break
        start_point=int(input("enter your start point --1 to 10"))
        end_point=int(input("enter your end point --1 to 10"))
        time=int(input("enter the current time"))
        obj.booking(start_point, end_point, time)
# obj=taxi(5,6)
# obj.booking(1,10,9)
# obj.booking(1,10,10)
# obj.booking(1,5,12)
# obj.booking(1,5,12)
# obj.booking(3,5,15)
# obj.booking(6,1,18)




