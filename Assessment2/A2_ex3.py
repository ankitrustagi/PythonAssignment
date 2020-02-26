from heapq import heappush, heappop

def minimumWaitingTime(customers, orderDetails):
    priorityqueue = []
    time_waiting = 0
    current_time = 0
    while orderDetails or priorityqueue:
        while orderDetails and orderDetails[-1][0] <= current_time:
            heappush(priorityqueue, orderDetails.pop()[::-1])
        if priorityqueue:
            current_task = heappop(priorityqueue)
            current_time += current_task[0]
            time_waiting += current_time - current_task[1]
        else:
            heappush(priorityqueue, orderDetails.pop()[::-1])
            current_time = priorityqueue[0][1]
    return time_waiting // customers

if __name__ == "__main__":
    orderDetails = []
    customers = int(raw_input("Enter how many customer's are in restaurant \n"))
    for _ in range(customers):
        arrival, cook_time = map(int, raw_input('Enter Arrival and Cooktime with space \n').split())
        orderDetails.append((arrival, cook_time))
    orderDetails.sort(reverse=True)
    optimumTime = minimumWaitingTime(customers, orderDetails)
    print("Tieu achieve the minimum average waiting time of {}".format(optimumTime))
