
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.plotly as py
import plotly.graph_objs as go


learning_rates = [ 0.0001,0.00025,0.0005,.00075,.001,.0025,0.005,.01,.025,.05,0.1,0.25,0.5] + [1,2.5,5,7.5,10,15,17.5,20,22.5,25,30,32.5,35,40,45,50]
lr_dict = {x: i for i,x in enumerate(learning_rates)}
# SGD
lr_sgd      = [1,5,10,15,17.5,20,22.5,25,30]
tr_time_sgd = [30,30,30,25,24,21,20,27,30]
lr_sgd_dict = [lr_dict[x] for x in lr_sgd]
# ADAM
lr_adam = [0.00025,0.0005,.00075,.001,.0025,0.005,0.1]
lr_adam_dict = [lr_dict[x] for x in lr_adam]
tr_time_adam = [30,25,27,30,30,30,30]
# adagrad
lr_adagrad = [0.025,0.05,0.1,0.25,0.5,1,2.5,5,10,15]
lr_adagrad_dict = [lr_dict[x] for x in lr_adagrad]
tr_time_adagrad = [25,30,10,6,6,11,25,30,30,30,30]
# momentum
lr_mom = [.025,2.5,5,7.5,10,15]
lr_mom_dict = [lr_dict[x] for x in lr_mom]
tr_time_mom = [30,25, 25, 22, 14,27]
# NAG
lr_nag = [1,2.5,5,7.5,10,15]
lr_nag_dict = [lr_dict[x] for x in lr_nag]
tr_time_nag = [17,25, 22, 20, 12,21]

trace1 = go.Scatter(
    x=lr_sgd_dict,
    y=tr_time_sgd,
    mode='lines+markers',
    name="sgd",
    hoverinfo='name',
    line=dict(
        shape='linear',color='rgb(20,125,190)'
    )
)
trace2 = go.Scatter(
    x= lr_adam_dict,
    y=tr_time_adam,
    mode='lines+markers',
    name="adam",
    hoverinfo='text+name',
    line=dict(
        shape='linear',color='rgb(245,145,30)'

    )
)
trace3 = go.Scatter(
    x= lr_adagrad_dict,
    y=tr_time_adagrad,
    mode='lines+markers',
    name="adagrad",
    hoverinfo='text+name',
    line=dict(
        shape='linear',color='rgb(25,160,75)'
    )
)
trace4 = go.Scatter(
    x= lr_mom_suffle_dict,
    y=tr_time_mom,
    mode='lines+markers',
    name="momentum",
    hoverinfo='text+name',
    line=dict(
        shape='linear',color='rgb(200,30,135)'
    )
)
trace5 = go.Scatter(
    x= lr_nag_dict,
    y=tr_time_nag,
    mode='lines+markers',
    name="nag",
    hoverinfo='text+name',
    line=dict(
        shape='linear',color='rgb(0,0,0)'
    )
)


data = [trace1,trace2,trace3,trace4,trace5]
layout = dict(title = 'Time to train vs. learning rate, by optimizer',
                 width = 800,
    height = 500,
    xaxis = dict(
        tickvals = list(lr_dict.values()),
        ticktext = list(lr_dict.keys()),
      title = "Learning rate"
    ),
    yaxis=dict(
        type='linear',
        title = 'Training time in number of Epochs',
        autorange=True
    )
              )

print(layout["xaxis"]["tickvals"])
fig = dict(data=data, layout=layout)
init_notebook_mode(connected=True)
iplot(fig, filename='word-embedding-plot.html')



from plotly.offline import init_notebook_mode, iplot, plot
import plotly.plotly as py
import plotly.graph_objs as go

#learning_rates = [0.00025,0.0005,.00075,.001,0.1,0.25,0.5] + [2.5,5,7.5,10,15,20,22.5]
#lr_dict = {x: i for i,x in enumerate(learning_rates)}
# sgd_shuffle
lr_sgd_shuffle    = [15,17.5,20,22.5,25,30,32.5,35,40,45,50]
tr_time_sgd_shuffle = [23,20,17,16,15,14,12,12,11,10,9]
lr_sgd_shuffle_dict = [lr_dict[x] for x in lr_sgd_shuffle]
# adam_shuffle
lr_adam_shuffle = [.0001,0.00025,0.0005,.00075,.001,0.0025,0.005]
lr_adam_shuffle_dict = [lr_dict[x] for x in lr_adam_shuffle]
tr_time_adam_shuffle = [25,12,7,5,4,3,30]
# adagrad_shuffle
lr_adagrad_shuffle = [0.0005,0.01,0.025,0.05,0.1,0.25,0.5,1,2.5]
lr_adagrad_shuffle_dict = [lr_dict[x] for x in lr_adagrad_shuffle]
tr_time_adagrad_shuffle = [30,30,15,6,3,3,4,8,25]
# mom_suffleentum
lr_mom_suffle = [7.5,15,17.5,20,22.5,25]
lr_mom_suffle_dict = [lr_dict[x] for x in lr_mom_suffle]
tr_time_mom_suffle = [15,13,13,13,12,12]
# nag_shuffle
lr_nag_shuffle = [0.5,1,2.5,5,10,15]
lr_nag_shuffle_dict = [lr_dict[x] for x in lr_nag_shuffle]
tr_time_nag_shuffle = [10,17,16,14,10,12,15,13,]



trace1a = go.Scatter(
    x=lr_sgd_shuffle_dict,
    y=tr_time_sgd_shuffle,
    mode='lines+markers',
    name="sgd_shuffle",
    hoverinfo='name',
    line=dict(
        shape='linear',dash='dot',color='rgb(20,125,190)'
    )
)
trace2a = go.Scatter(
    x= lr_adam_shuffle_dict,
    y=tr_time_adam_shuffle,
    mode='lines+markers',
    name="adam_shuffle",
    hoverinfo='text+name',
    line=dict(
        shape='linear',dash='dot',color='rgb(245,145,30)'

    )
)
trace3a = go.Scatter(
    x= lr_adagrad_shuffle_dict,
    y=tr_time_adagrad_shuffle,
    mode='lines+markers',
    name="adagrad_shuffle",
    hoverinfo='text+name',
    line=dict(
        shape='linear',dash='dot',color='rgb(25,160,75)'
    )
)
trace4a = go.Scatter(
    x= lr_mom_suffle_dict,
    y=tr_time_mom_suffle,
    mode='lines+markers',
    name="momentum_suffle",
    hoverinfo='text+name',
    line=dict(
        shape='linear',dash='dot',color='rgb(200,30,135)'
    )
)
trace5a = go.Scatter(
    x= lr_nag_shuffle_dict,
    y=tr_time_nag_shuffle,
    mode='lines+markers',
    name="nag_shuffle",
    hoverinfo='text+name',
    line=dict(
        shape='linear',dash='dot',color='rgb(0,0,0)'
    )
)
data_a = [trace1a,trace2a,trace3a,trace4a,trace5a]
data = data + data_a
layout = dict(title = 'Time to train vs. learning rate, by optimizer',
                 width = 800,
    height = 500,
    xaxis = dict(
        tickvals = list(lr_dict.values()),
        ticktext = list(lr_dict.keys()),
      title = "Learning rate"
    ),
    yaxis=dict(
        type='linear',
        title = 'Training time in number of Epochs',
        autorange=True
    )
              )

fig = dict(data=data, layout=layout)
fig1 = dict(data=data_a, layout=layout)
init_notebook_mode(connected=True)
#iplot(fig, filename='word-embedding-plot')
iplot(fig1, filename='word-embedding-plot')


