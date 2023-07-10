import numpy as np 
import math
import matplotlib.pyplot as plt
import seaborn as sns

PALETTE = ['#9BCDD2','#FF8551', '#C3EDC0', '#FCD5CE', '#F8EDEB', '#FEC89A']
sns.set_palette(PALETTE)
sns.set_style('white')

def get_categorical_features(df):
    return df.select_dtypes(exclude=np.number).columns

def get_numerical_features(df):
    return df.select_dtypes(include=np.number).columns 

def histplot_num_feature_by_target(df, target="Churn", label_yes="Yes", label_no="No",  features=None, cols=3, density=True, pallete=PALETTE):
    if features is None:
        features = get_numerical_features(df)

    # Create a figure
    rows = math.ceil(len(features) / cols)
    fig, ax = plt.subplots(rows, cols, figsize=(2+4*cols, 5*rows))
    
    for row in range(rows):
        for col in range(cols):
            i = row * cols + col
            if i < len(features):
                var = features[i]
                new_ax = ax[row, col] if rows > 1 else ax[col]
                # Plot histograms for churn and non-churn customers
                df[df[target] == label_no][var].plot(kind="hist", bins=35, ax=new_ax,  density=density, color=pallete[0], alpha=0.5).set_title(var)
                df[df[target] == label_yes][var].plot(kind="hist", bins=35, ax=new_ax, density=density,  color=pallete[1], alpha=0.7)
                
                new_ax.set_ylabel('')
            else:
                plt.delaxes(ax[row, col])
        
    plt.legend([label_no, label_yes], loc="upper right", title=target, bbox_to_anchor=(0.6, 0.5, 0.5, 0.5), fancybox=True)
        
def barplot_cat_feature_by_target(df, target="Churn", label_yes="Yes", label_no="No",  features=None, cols=4, palette=PALETTE):
    if features is None:
        features = get_categorical_features(df)

    rows =  math.ceil(len(features)/ cols)
    fig, ax = plt.subplots(rows, cols, figsize=(2+4*cols, 5*rows))

    for row in range(rows):
        for col in range(cols):
            i = row * cols + col
            if i < len(features):
                var = features[i]
                new_ax = ax[row, col] if rows > 1 else ax[col]
    
                df[df[target] == label_no][var].value_counts().plot(kind="bar", width=.5, ax=ax[row, col], color=palette[0], alpha=0.5).set_title(var)
                df[df[target] == label_yes][var].value_counts().plot(kind="bar", width=.3, ax=ax[row, col], color=palette[1], alpha=0.5)
            
            else:
                plt.delaxes(ax[row, col])
                        
            if col == 0:
                ax[row, col].legend(["No Churn", "Churn"], loc="upper right", bbox_to_anchor=(0, 1.35), shadow=True)
            
            ax[row, col].set_xlabel("")  # Remove x-label

    fig.subplots_adjust(hspace=0.7)
