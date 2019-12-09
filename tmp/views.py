from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    # engine = create_engine('mysql+pymysql://root:root@localhost/testdb')
    # conn = engine.connect()

    # Mdata = pd.read_sql_table('melon', conn)
    # Gdata = pd.read_sql_table('genie', conn)
    # Bdata = pd.read_sql_table('bugs', conn)

    # mtmp = Mdata.values.T.tolist()
    # gtmp = Gdata.values.T.tolist()
    # btmp = Bdata.values.T.tolist()

    # data = Mdata.to_html()
    return render(request, 'site/index.html')

def melonp(request):
    return render(request, 'site/melonp.html')

def geniep(request):
    return render(request, 'site/geniep.html')

def bugsp(request):
    return render(request, 'site/bugsp.html')
