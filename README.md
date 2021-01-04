## Speed is of the essence 

<img src="https://images.pexels.com/photos/290470/pexels-photo-290470.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=800">

Source: https://www.pexels.com

After carefully analyzing the behaviour of our users the analytics team proposed a few very successful user stories
which significantly contributed to the growth of Sparkify. To avoid being perished by their own success, the analytics
team needs a serious performance upgrade when it comes to querying the database. Since speed is the most important
factor for the analytics teams, we have decided to create a Cassandra database, specifically optimized for certain
queries.

### The queries and primary keys

- query 1 ```sql```
- query 2
- query 3

You can find a visual component in the main notebook. 

### Instructions

Before you can run the notebook, there are a few things you need to do:
- create and activate a virtual environment
- run the tests

Furthermore, note that the logic needed to execute the notebook is stored in the /src folder. The Python version used
for this project is 3.8.5. 

#### create and activate a virtual environment 

You can either use Anaconda or venv to create the virtual environment. Regardless of your choice, you have to open
a (Anaconda) prompt, clone the project, and navigate to the project folder. Next, enter the following:

##### Anaconda
```bash
conda env create -f environment.yml
conda activate postgres
```

##### venv
```bash
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt 
```

#### Tests

```bash
pytest -v
```

### Start

The complete project revolves around one jupyter notebook, stored in notebooks/main.ipynb. This notebook includes every
step in the process, additional explanation and comments when necessary, and visual support for the primary keys.

### Contact

In case of suggestions or remarks please contact the Data Engineering department