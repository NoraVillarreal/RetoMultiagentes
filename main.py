from A01570748_M1.traffic_model import TrafficModel
import matplotlib.pyplot as plt
import time


def basic_example_space():

    start_time = time.time()
    model = TrafficModel(6, 10, 10, 1)
    count = 0
    while count <= 100:
        time.sleep(0.25)
        model.step()
        model.printarray()
        count = count+1
        #print(model.ps)
        

    print("--- %s segundos ---" % (time.time() - start_time))

    
    
    
