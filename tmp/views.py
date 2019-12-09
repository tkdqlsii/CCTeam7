from django.shortcuts import render, get_object_or_404
from crow.util import chart
import pandas as pd
import matplotlib.pyplot as plt
import platform
import matplotlib
from matplotlib import font_manager,rc, style
from sqlalchemy import create_engine

# Create your views here.
def index(request):
    engine = create_engine('mysql+pymysql://root:root@localhost/testdb')
    conn = engine.connect()

    Mdata = pd.read_sql_table('melon', conn)
    Gdata = pd.read_sql_table('genie', conn)
    Bdata = pd.read_sql_table('bugs', conn)

    mtmp = Mdata.values.T.tolist()
    gtmp = Gdata.values.T.tolist()
    btmp = Bdata.values.T.tolist()

    data = Mdata.to_html()
    return render(request, 'site/index.html',{"data": data})

def melonp(request):
    return render(request, 'site/melonp.html')
