import matplotlib.pyplot as plt

def f_graph(graph: str, target: str, object: object, tiles: list, kingdoms: list, citys: list):

    if graph.lower() == "pob":
        print("pob")
        if target.lower() == "kingdoms":
            for k in kingdoms:
                plt.plot(k.Hpob)
            plt.title("Pob --> kingdoms")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True

        elif target.lower() == "citys":
            #plot citys pob
            plt.show()

        elif target.lower() == "kingdom":
            #plot specific kingdom pob
            plt.show()

        elif target.lower() == "city":
            #plot specific city pob
            plt.show()

        elif target.lower() == "kingdom_citys":
            #plot kingdom citys pob
            plt.show()
    
    return False