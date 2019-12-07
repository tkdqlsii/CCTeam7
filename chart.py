#print(Mdata.to_html()) 이거 나중에 쓸라고 냅둠
import pandas as pd
import matplotlib.pyplot as plt
import platform
import matplotlib
from matplotlib import font_manager,rc, style
from sqlalchemy import create_engine

if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else: rc('font', family='AppleGothic')

matplotlib.rcParams['axes.unicode_minus'] = False

engine = create_engine('mysql+pymysql://root:root@localhost/testdb')
conn = engine.connect()

Mdata = pd.read_sql_table('melon', conn)
Gdata = pd.read_sql_table('genie', conn)
Bdata = pd.read_sql_table('bugs', conn)

mtmp = Mdata.values.T.tolist()
gtmp = Gdata.values.T.tolist()
btmp = Bdata.values.T.tolist()

for i in range(len(mtmp[0])):
    j = 0

    if mtmp[0][i] == gtmp[0][j]:
        for k in range(len(btmp[0])):
            if mtmp[0][i] == btmp[0][k]:
                names = ['melon', 'genie', 'bugs']
                score = [mtmp[3][i], gtmp[3][j], btmp[3][k]]
                colors = ['yellowgreen', 'lightskyblue','gold']
                explodes = (0, 0, 0)
                plt.pie(score, explode = explodes, labels = names, colors = colors, autopct='%1.1f%%', shadow = None, startangle=90, textprops={'fontsize': 14})
                plt.axis('equal')
                plt.title('점유율')
                plt.show()
                break;
            else:
                k+=1
        break;
    else:
        j+=1
conn.close()
