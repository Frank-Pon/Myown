import requests
from bs4 import BeautifulSoup
import pandas as pd
#import matplotlib.pyplot as plt
all_data = []
url = ['https://member.jav101.com/joinus'
       ]
for i in url:
    response = requests.get(i)
    soup = BeautifulSoup(response.text,'xml')

    title = soup.title.text if soup.title else '無title'
    meta_desc = soup.find("meta",attrs = {'name','description'})
    meta_desc = meta_desc["content"] if meta_desc else '無meta description'

    h1_tags = [h1.text.strip() for h1 in soup.find_all('h1')]
    h2_tags = [h2.text.strip() for h2 in soup.find_all('h2')]
    # a_tags = [a.text.strip() for a in soup.find_all('a')]

    print(f'Title：{title}')
    print(f'Meta Description：{meta_desc}')
    print(f'H1 Tag：{h1_tags}')
    print(f'H2 Tag：{h2_tags}')
    print('=========================')
    #print(f'a Tag：{a_tags}')

    #-----網    路    爬    蟲--------

    all_data.append({
        "Title":[title],
        "Meta Desription":[meta_desc],
        "H1_Tag":[",".join(h1_tags)],
        "H2_tag":[",".join(h2_tags)]
        })

df = pd.DataFrame(all_data)
df.to_excel("SEO_report.xlsx",index=False)
print("SEO資料已成功儲存成Excel")

#------爬  蟲  內  容  存  成  E x c e l------

# labels = ['H1','H2']
# counts = [len(h1_tags),len(h2_tags)]

# plt.bar(labels,counts,color=['blue','green'])
# plt.title('H1 & H2 Title Count')
# plt.ylabel('Quality')
# plt.show()
