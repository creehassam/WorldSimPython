import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap 
import numpy as np

def f_graph(graph: str, target: str, object: object, tiles: list, kingdoms: list, citys: list, history: list):

    if graph.lower() == "pob":

        if target.lower() == "kingdoms":
            #plot pob --> kingdoms
            for k in kingdoms:
                plt.plot(history["kingdoms"][k.name][0])
            plt.title("Pob --> kingdoms")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True

        elif target.lower() == "citys":
            #plot pob --> citys
            for c in citys:
                plt.plot(history["citys"][c.name][0])
            plt.title("Pob --> citys")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True

        elif target.lower() == "kingdom":
            #plot specific kingdom pob
            plt.plot(history["kingdoms"][object][0])
            plt.title(f"Pob --> {object}")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True

        elif target.lower() == "city":
            #plot specific city pob
            plt.plot(history["citys"][object][0])
            plt.title(f"Pob --> {object}")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True

        elif target.lower() == "kingdom_citys":
            #plot kingdom citys pob
            for c in object.kingdomCitys:
                plt.plot(history["citys"][c.name][0])
            plt.title(f"Pob --> citys of {object.name}")
            plt.xlabel("Time")
            plt.ylabel("Pob")
            plt.show()
            return True
    
    elif graph.lower() == "money":

        if target.lower() == "kingdoms":
            #plot money --> kingdoms
            for k in kingdoms:
                plt.plot(history["kingdoms"][k.name][1])
            plt.title("Money --> kingdoms")
            plt.xlabel("Time")
            plt.ylabel("Money")
            plt.show()
            return True

        elif target.lower() == "citys":
            #plot money --> citys
            for c in citys:
                plt.plot(history["citys"][c.name][1])
            plt.title("Money --> citys")
            plt.xlabel("Time")
            plt.ylabel("Money")
            plt.show()
            return True

        elif target.lower() == "kingdom":
            #plot specific kingdom money
            plt.plot(history["kingdoms"][object][1])
            plt.title(f"Money --> {object}")
            plt.xlabel("Time")
            plt.ylabel("Money")
            plt.show()
            return True

        elif target.lower() == "city":
            #plot specific city money
            plt.plot(history["citys"][object][1])
            plt.title(f"Money --> {object}")
            plt.xlabel("Time")
            plt.ylabel("Money")
            plt.show()
            return True

        elif target.lower() == "kingdom_citys":
            #plot kingdom citys money
            for c in object.kingdomCitys:
                plt.plot(history["citys"][c.name][1])
            plt.title(f"Money --> citys of {object.name}")
            plt.xlabel("Time")
            plt.ylabel("Money")
            plt.show()
            return True

    elif graph.lower() == "tile":
        #plot plants and animals from tile
            plt.plot(history["tiles"][target][object][0])
            plt.plot(history["tiles"][target][object][1])
            plt.title(f"Tile {target},{object}")
            plt.xlabel("Time")
            plt.ylabel("Kt")
            plt.show()
            return True
    
    return False

def f_map(tiles: list, citys: list):

    map = []
    for x in range(len(tiles)):
        a = []
        for y in range(len(tiles[0])):
            a.append(tiles[y][x].type)
        map.append(a)
    
    map = np.array(map)
    plt.figure(figsize=(7,7))
    colors = ListedColormap(["cornflowerblue", "yellowgreen", "lawngreen", "grey"])
    print(map)
    plt.imshow(map, cmap=colors)

    coords = []
    letters = []
    for c in citys:
        x = c.x
        y = c.y
        l = c.kingdom.name[:3]
        coords.append((x, y))
        letters.append(l.title())
    
    for (x, y), letter in zip(coords, letters):
        plt.text(x, y, letter, ha='center', va='center', color='snow', fontsize=10, fontweight='bold')

    plt.show()