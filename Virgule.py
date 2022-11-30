import pandas as pd




def readFile():
    df = pd.read_excel(open('C:/pikoro/Orientation/data_Ent/Data.xlsx','rb'),sheet_name='Feuil1')
    return df

def addV():
    df = readFile()
    x = df.to_dict('records')
    print(type(x))
    for i in x :
     a = str(i['SDO'])
     if len(a) == 7 :
            m = a
            m = m[0:3]+'.' + m[3:(len(m)-1)]
            i['SDO'] = m
     elif len(a) == 6 :
            m = a
            m = m[0:2]+'.' + m[2:(len(m)-1)]
            i ['SDO'] = m
     else :
            continue

    df1 = pd.DataFrame.from_dict(x)
    with pd.ExcelWriter('C:/pikoro/Orientation/data_Ex/data.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Feuil1',index=False)