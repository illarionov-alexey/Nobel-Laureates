import pandas as pd
import numpy as np
import os
import requests
import sys
import re
import matplotlib.pyplot as plt


def json_download():
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'Nobel_laureates.json' not in os.listdir('../Data'):
        sys.stderr.write("[INFO] Dataset is loading.\n")
        url = "https://www.dropbox.com/s/m6ld4vaq2sz3ovd/nobel_laureates.json?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/Nobel_laureates.json', 'wb').write(r.content)
        sys.stderr.write("[INFO] Loaded.\n")


def first_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:
    df = df.dropna(subset=['gender']).reset_index(drop=True)
    if output:
        print(df[['country', 'name']].head(20).to_dict())
    return df


def second_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:
    for i in range(0, df.shape[0]):
        if df.at[i, 'born_in'] == '':
            if str(df.at[i, 'place_of_birth']).find(',') != -1:
                df.at[i, 'born_in'] = df.at[i, 'place_of_birth'].split(',')[-1].strip()
            else:
                df.at[i, 'born_in'] = None

    df.dropna(subset=['born_in'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['born_in'].replace({'US': 'USA', 'United States': 'USA', 'U.S.': 'USA', 'United Kingdom': 'UK'}, inplace=True)
    if output:
        print(df['born_in'].tolist())
    return df


def third_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:
    df['year_born'] = df['date_of_birth'].apply(lambda val: int(re.search(r'\d{4}', val).group()))
    df['age_of_winning'] = df['year'] - df['year_born']
    if output:
        print(df['year_born'].tolist())
        print(df['age_of_winning'].tolist())
    return df


def forth_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:
    s = df[["born_in", 'country']].groupby("born_in").count()['country']
    data = {'Other countries': s[s < 25].sum()}
    data.update(s[s >= 25].sort_values(ascending=False).to_dict())
    # print(data)
    if output:
        vals = list(data.values())
        exp = [0 if v > 97 else 0.08 for v in vals]
        colors = ['blue', 'orange', 'red', 'yellow', 'green', 'pink', 'brown', 'cyan', 'purple']
        plt.figure(figsize=(12, 12))
        plt.pie(vals, labels=data.keys(), colors=colors, explode=exp,
                autopct=lambda pct: f"{pct:.2f}%\n({pct * sum(vals) / 100:.0f})")
        plt.show()
        # plt.imsave("img.png")
    return df

def fiveth_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:

    male_series = df[df.category != ''][df.gender == 'male'].groupby(['category']).size()
    labls = male_series.index.tolist()
    males = male_series.tolist()
    females = df[df.gender == 'female'].groupby(['category']).size().tolist()

    if output:
        plt.figure(figsize=(10, 10))
        x_axis = np.arange(len(labls))
        print(x_axis)
        plt.bar(x_axis-0.2, males,  width=0.4, label='Males', color='blue')
        plt.bar(x_axis+0.2, females, width=0.4, label='Females', color='crimson')
        plt.xticks(x_axis,labls)

        plt.xlabel('Category', fontsize=14)
        plt.ylabel('Nobel Laureates Count', fontsize=14)
        plt.title('The total count of male and female Nobel Prize winners by categories', fontsize=20)
        plt.legend()
        plt.show()
    return df

def sixth_stage(df: pd.DataFrame, output: bool = True) -> pd.DataFrame:
    categories = df['category'][df.category != ''].unique().tolist()
    categories.sort()
    data = []
    for c in categories:
        data.append(df[ df.category == c ]['age_of_winning'].tolist())
    categories.append('All categories')
    data.append(df[df.category != '']['age_of_winning'].tolist())

    if output:
        meanprops = {'color': 'b', 'linestyle': '-', 'linewidth': 1.0,
                     'marker': '^', 'markerfacecolor': 'g', 'markeredgecolor': 'k'}
        plt.figure(figsize=(10, 10))
        plt.boxplot(data, labels=categories,showmeans=True)
        plt.ylabel('Age of Obtaining the Nobel Price',fontsize=14)
        plt.xlabel('Category',fontsize=14)
        plt.title('Distribution of Ages by Category', fontsize=20)
        plt.show()


if __name__ == '__main__':
    json_download()
    # write your code here
    df = pd.read_json('../Data/Nobel_laureates.json')
    df = first_stage(df, False)
    df = second_stage(df, False)
    df = third_stage(df, False)
    df = forth_stage(df, False)
    df = fiveth_stage(df, False)
    df = sixth_stage(df, True)
