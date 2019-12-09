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

                m = [str(mtmp[3][i]) + "위"]
                g = [str(gtmp[3][j]) + "위"]
                b = [str(btmp[3][k]) + "위"]
                #y = [mtmp[3][i], gtmp[3][j], btmp[3][k]]

                plt.bar(m, mtmp[3][i], color = 'yellowgreen', width=0.2, label='melon')
                plt.bar(g, gtmp[3][j], color = 'lightskyblue', width=0.3, label='genie')
                plt.bar(b, btmp[3][k], color = 'orange', width=0.5, label = 'bugs')
                plt.xlabel('제목 : ' + mtmp[0][i], size=14)
                plt.ylabel('score')
                plt.title('차트별 순위')
                plt.legend()
                plt.savefig("C:/Users/chlqu/MySite/crow/static/assets/images/chart.png", dpi=550)
                #plt.show()
                break
            else:
                k+=1
        break
    else:
        j+=1

conn.close()
