import subprocess
import tempfile

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)

sol = "solutions_do_not_open/"

def test_01():
    _exec_notebook(sol+"Lab_01_DA Jupyter_solution.ipynb")

def test_02():
    _exec_notebook(sol+"Lab_02_DA Pandas_solution.ipynb")

def test_03():
    _exec_notebook(sol+"Lab_03_DA Matplotlib_solution.ipynb")

def test_04():
    _exec_notebook(sol+"Lab_04_ML Scikit Learn Regression_solution.ipynb")

def test_05():
    _exec_notebook(sol+"Lab_05_ML_Scikit_Learn_Classification_solution.ipynb")

def test_06():
    _exec_notebook(sol+"Lab_06_ML Scikit Learn Classification Long_solution.ipynb")

def test_07():
    _exec_notebook(sol+"Lab_07_ML Scikit Learn Clustering_solution.ipynb")

def test_08():
    _exec_notebook(sol+"Lab_08_ML Improving performance_solution.ipynb")

def test_09():
    _exec_notebook(sol+"Lab_09_DL_Keras_Classification_solution.ipynb")

def test_10():
    _exec_notebook(sol+"Lab_10_DL Keras Intro Shallow Models_solution.ipynb")

def test_11():
    _exec_notebook(sol+"Lab_11_DL Keras Intro Fully Connected Models_solution.ipynb")

def test_12():
    _exec_notebook(sol+"Lab_12_DL Visualizing Hidden Layers_solution.ipynb")

def test_13():
    _exec_notebook(sol+"Lab_13_DL Learning MNIST and Fashion_solution.ipynb")

def test_14():
    _exec_notebook(sol+"Lab_14_DL Fashion Mnist with CNNs_solution.ipynb")

def test_15():
    _exec_notebook(sol+"Lab_15_DL Keras Callbacks and Functional API_solution.ipynb")

# def test_16():
#     _exec_notebook(sol+"Lab_16_DL Keras Wandb_solution.ipynb")

def test_17():
    _exec_notebook(sol+"Lab_17_DL Pretrained models_solution.ipynb")

def test_18():
    _exec_notebook(sol+"Lab_18_DL Data Augmentation_solution.ipynb")

def test_19():
    _exec_notebook(sol+"Lab_19_DL Transfer Learning Short_solution.ipynb")

def test_20():
    _exec_notebook(sol+"Lab_20_DL Image similarity_solution.ipynb")

def test_21():
    _exec_notebook(sol+"Lab_21_DL Time Series Forecasting Short_solution.ipynb")

def test_22():
    _exec_notebook(sol+"Lab_22_DL Sentiment classification_solution.ipynb")

def test_23():
    _exec_notebook(sol+"Lab_23_DL Sequence Generation_solution.ipynb")

def test_24():
    _exec_notebook(sol+"Lab_24_APP_Text_Classification_solution.ipynb")

def test_25():
    _exec_notebook(sol+"Lab_25_DL Pretrained Embeddings for text_solution.ipynb")

def test_29():
    _exec_notebook(sol+"Lab_29_TF2_Data_solution.ipynb")

def test_30():
    _exec_notebook(sol+"Lab_30_Hyperparameter_tuning_solution.ipynb")

def test_31():
    _exec_notebook(sol+"Lab_31_DL Model Serving_solution.ipynb")
