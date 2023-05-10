import plotly.graph_objects as go
from random_walk import RandomWalk
import numpy as np

#Make making new walks, as long as the program is active
while True:

    #Make random walk
    rw = RandomWalk(5_000)
    rw.fill_walk()

    #Plot the points in the walk
    fig = go.Figure(data=go.Scatter(x=rw.x_values,
                                    y=rw.y_values,
                                    mode='markers',
                                    marker=dict(
                                    size=12,
                                    color=np.random.randn(5000), 
                                    colorscale='Viridis',
                                    showscale=False
                                         )
                                     )
                   )
    fig.show()


