"""This module contains the exact code to reproduce the 3 graphs in notebooks/main.ipynb."""


from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
from src.create_event_data import CreateEventData


class CreateGraphs:
    event_data_path = Path('..') / 'event_data'

    def __init__(self):
        self.create_event_instance = CreateEventData(csv_path_list=self.event_data_path)
        self.event_df = self.create_event_instance.data_pipeline()

    def create_graph_query_1(self):
        session_id_values = Counter(self.event_df['sessionId']).values()
        item_in_session_values = Counter(self.event_df['itemInSession']).values()

        fig, ax = plt.subplots(figsize=(16, 8), ncols=2)

        ax[0] = sns.histplot(session_id_values, legend=False, stat='probability', ax=ax[0])
        ax[0].set_xlabel('Number of instances per unique value')
        ax[0].set_xticks(np.arange(0, 120, 10))
        ax[0].set_yticks(np.arange(0, 0.4, 0.05))
        ax[0].set_yticklabels([f"{round(x * 100, 2)}%" for x in np.arange(0, 0.4, 0.05)])
        ax[0].set_title("Most unique values within 'sessionId' contain 5 instances or less")

        ax[1] = sns.histplot(item_in_session_values, legend=False, stat='probability', ax=ax[1])
        ax[1].set_xlabel('Number of instances per unique value')
        ax[1].set_xticks(np.arange(0, 550, 50))
        ax[1].set_yticks(np.arange(0, 0.6, 0.05))
        ax[1].set_yticklabels([f"{round(x * 100, 2)}%" for x in np.arange(0, 0.6, 0.05)])
        ax[1].set_title("'itemInSession' contains quite a few large outliers")

        fig.suptitle(
            "Partition key for query 1:\n 'sessionId' is better due to less"
            "variance / large outliers in the distribution of unique values",
            fontsize=16)

    def create_graph_query_2(self):
        session_id_values = Counter(self.event_df['sessionId']).values()
        user_id_values = Counter(self.event_df['userId']).values()

        fig, ax = plt.subplots(figsize=(16, 8), ncols=2)

        ax[0] = sns.histplot(session_id_values, legend=False, stat='probability', ax=ax[0])
        ax[0].set_xlabel('Number of instances per unique value')
        ax[0].set_xticks(np.arange(0, 120, 10))
        ax[0].set_yticks(np.arange(0, 0.4, 0.05))
        ax[0].set_yticklabels([f"{round(x * 100, 2)}%" for x in np.arange(0, 0.4, 0.05)])
        ax[0].set_title("Most unique values within 'sessionId' contain 5 instances or less")

        ax[1] = sns.histplot(user_id_values, legend=False, stat='probability', ax=ax[1])
        ax[1].set_xlabel('Number of instances per unique value')
        ax[1].set_xticks(np.arange(0, 750, 50))
        ax[1].set_yticks(np.arange(0, 0.6, 0.05))
        ax[1].set_yticklabels([f"{round(x * 100, 2)}%" for x in np.arange(0, 0.6, 0.05)])
        ax[1].set_title("'userId' contains quite a few large outliers")

        fig.suptitle(
            "Partition key for query 2:\n 'sessionId' is better due to less"
            "variance / large outliers in the distribution of unique values",
            fontsize=16)

    def create_graph_query_3(self):
        song_values = Counter(self.event_df['song']).values()

        fig, ax = plt.subplots(figsize=(16, 8))

        ax = sns.histplot(song_values, legend=False, stat='probability', bins=40)
        ax.set_xlabel('Number of instances per unique value')
        ax.set_xticks(np.arange(0, 40, 5))
        ax.set_yticks(np.arange(0, 1.05, 0.05))
        ax.set_yticklabels([f"{round(x * 100, 2)}%" for x in np.arange(0, 1.05, 0.05)])
        ax.set_title("Almost all unique values within 'song' contain 5 instances or less")

        fig.suptitle("Partition key for query 3:\n 'song' is an excellent partition key",
                     fontsize=16)
