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

    Mdata = pd.read_sql_table('total', conn)

    mtmp = Mdata.values.T.tolist()
    """
    for i in range(len(mtmp[0])):
        j = 0

        if mtmp[0][i] == gtmp[0][j]:
            for k in range(len(btmp[0])):
                if mtmp[0][i] == btmp[0][k]:
                    t.append([mtmp[i], mtmp[i+1], mtmp[i+2], mtmp[i+3]])

                    #plt.show()
                    break
                else:
                    k+=1
            break
        else:
            j+=1


    tt = t[0][0]
    ta = t[0][1]
    tc = t[0][2]
    ts = t[0][3]"""
    data = Mdata.to_html()

    return render(request, 'site/index.html',{"data": data})

def melonp(request):
    return render(request, 'site/melonp.html')

def geniep(request):
    return render(request, 'site/geniep.html')

def bugsp(request):
    return render(request, 'site/bugsp.html')
