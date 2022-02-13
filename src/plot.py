from matplotlib import pyplot as plt

# finds subplot dimetions based of number of data sets
def subplot_dims(set_len):
    num_rows = 1
    num_cols = 1
    while set_len > (num_rows*num_cols):
        if num_rows < num_cols:
            num_rows += 1
        else:
            num_cols += 1
    
    return num_rows, num_cols


# plots data sets onto one figure
def plot_data_sets(data):
    fig = plt.figure()

    rows, cols = subplot_dims(len(data))

    for count, data_set in enumerate(data):
        ax = fig.add_subplot(rows, cols, count+1)
        ax.plot(data_set[:,0], data_set[:,1])
        ax.set_title(f'Set: {count+1}')
        ax.grid(True)

    plt.tight_layout()
    plt.show()


# Helped me test my subplot_dims algorithm
def test_plot(num=6):
    import numpy as np
    x = [1, 2, 3, 4, 5]
    y = [1, 5, 3, 2, 4]

    data = []
    for _ in range(num):
        data.append(np.array([x, y]).transpose())

    plot_data_sets(data)
