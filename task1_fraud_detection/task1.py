import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return df.columns.tolist()

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df.type.unique().tolist()

def exercise_5(df):
    series = df.nameDest.value_counts()[:10]
    return series

def exercise_6(df):
    all_frauds = df[df['isFraud'] == 1]
    return all_frauds

def exercise_7(df):
    pass

def visual_1(df):
    def transaction_counts(df):
        # TODO
        return df.type.value_counts()
    def transaction_counts_split_by_fraud(df):
        # TODO
        all_frauds = exercise_6(df)
        return all_frauds.type.value_counts()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Counts')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Total number of transactions')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Counts by fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Total number of transactions')
    fig.suptitle('Total transactions vs Total fraud transactions')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'Transaction Graphs show which transaction type is the most common and then shows which types have the most fraud'

visual_1(df)

def visual_2(df):
    def query(df):
        # TODO
        df['Origin Delta'] = df['oldbalanceOrg'] -	df['newbalanceOrig']
        df['Destination Delta'] = df['oldbalanceDest'] -	df['newbalanceDest']
        return df[df['type']=='CASH_OUT']
    plot = query(df).plot.scatter(x='Origin Delta',y='Destination Delta')
    plot.set_title('Origin Delta vs. Destination Delta')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'This graph compares change in balance at origin with change in balance at destination'

visual_2(df)

def exercise_custom(df):
    # TODO
    return df
    
def visual_custom(df):
    plot = exercise_custom(df).plot.scatter(x='type',y='amount')
    plot.set_title('All transaction amounts per type')
    plot.set_xlim(left=-1, right=5)
    plot.set_ylim(bottom=0, top=1e7)
    return 'This graph transaction amounts per type'

visual_custom(df)
