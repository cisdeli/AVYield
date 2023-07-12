from data.pre_processing import datasets
import plotly.express as px
import pandas as pd
import numpy as np


def print_data(selected_crop):
    print("Selected crop: ", selected_crop)
    print(datasets[selected_crop].head())


def get_dataset(selected_crop):
    return datasets[selected_crop]


def set_mean_yield_bar_graph(df, crop, title):
    if crop == 'Corn' or crop == 'Wheat':
        mean_yield_year = df.groupby('YEAR').agg(
            {'YIELD': lambda x: round(x.mean(), 2),
             'MOIST': lambda x: round(x.mean(), 2)}
        ).reset_index()
        color_col = 'MOIST'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year', 'MOIST': 'Moist'}
        color_cont_scale = px.colors.sequential.Aggrnyl
    elif crop == 'Sunflower':
        mean_yield_year = df.groupby('YEAR').agg(
            {'YIELD': lambda x: round(x.mean(), 2),
             'DAYS': lambda x: round(x.mean(), 2)}
        ).reset_index()
        color_col = 'DAYS'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year', 'DAYS': 'Days'}
        color_cont_scale = px.colors.sequential.Viridis
    else:
        mean_yield_year = df.groupby('YEAR')['YIELD'].mean().reset_index()
        mean_yield_year['YIELD'] = round(mean_yield_year['YIELD'], 2)
        color_col = 'YIELD'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year'}
        color_cont_scale = px.colors.sequential.Bluered

    return px.bar(
        mean_yield_year,
        x='YEAR',
        y='YIELD',
        color=color_col,
        title=title,
        labels=labels_dict,
        color_continuous_scale=list(reversed(color_cont_scale))
    )


# Brand Yield per year
def brand_year(selected_crop, selected_brand):
    df = datasets[selected_crop]
    brand = df[df['BRAND'] == selected_brand]
    brand.loc[:, 'YEAR'] = brand['YEAR'].astype(str)
    return set_mean_yield_bar_graph(brand, selected_crop, 'Mean Brand Yield Per Year')


# Yield per brand
def yield_brand(selected_crop, selected_year):
    df = datasets[selected_crop]
    yield_brand = df[df['YEAR'] == selected_year]
    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    swarm = px.strip(yield_brand, x='BRAND', y='YIELD', title='Yield per Brand', color='WATER_REGIME',
                     color_discrete_map=color_map, hover_data=sorted(
                         list(yield_brand.columns)),
                     labels={'BRAND': 'Brand', 'YIELD': 'Yield', 'WATER_REGIME': 'Water Regime'})
    return swarm


# Mean Yield per year
def yield_year(selected_crop):
    return set_mean_yield_bar_graph(datasets[selected_crop], selected_crop, 'Mean Yield per Year')
