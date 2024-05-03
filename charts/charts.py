import matplotlib.pyplot as plt
def generate_pie_chart():
    labels = ['A', 'B', 'C'] # los lebel son como los grupos que voy a medir
    values = [200, 34, 120]  # son los valores que va a tomar 

    fig, ax = plt.subplots() # ax seria las figuras que estan en el subplots
    ax.pie(values, labels=labels) # aqui le pido que sea una grafica pie 
    plt.savefig('pie.png') # no para el programa guarda la grafica
    plt.close()