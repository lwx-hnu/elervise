#version 1.02
#author W-L
#time 2020-12-18
#更新日志：V1.02____该版本优化了字符串的清洗功能，现在导出article时可以导出完整的不带杂音的文章了
import requests
import re
import json
import time
if __name__ == "__main__":
    list_token=[]
    list_title=[]
    cookie ='__cfduid=d3bf05b9bfe7103f5e8fdf33e838a83ee1607916372; EUID=f80557a0-1a48-4676-a233-0d543c50f9a7; id_ab=B:100:8:f471f661-0103-4007-bc68-14fc02285b57; mboxes=%7B%7D; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; fingerPrintToken=63871c623999df2bd167b51679758381; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18615%7CMCMID%7C15587988382064304172649633027284887076%7CMCAAMLH-1608873930%7C11%7CMCAAMB-1608873930%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1608276330s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1439495112%7CvVersion%7C5.0.0; sd_session_id=3fed365a6ee193432c69acf0827a102e16b9gxrqa; acw=3fed365a6ee193432c69acf0827a102e16b9gxrqa%7C%24%7C2A0277851E87C25C57DC75194FABC56C4606779644DE2EC82CCB5E9E44EBF1F89E4B17C052E53E1A03F53D0B2B0979157BB3BB76A441EF463FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=A98C733B6C2C7D4704509EE198BF43DEE67722AB977A58722B84D6FB838F12D2A46D7BA052243F5495B8199195EAEF1A538E9745997A3D28; has_multiple_organizations=false; MIAMISESSION=51ae2cd3-08af-48d2-be4b-5e42467a1a2a:3785721947; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwODI2OTE0NzQ2N30=; Hm_lvt_6c9e6e168b46aaa118c7ed52e9a02f43=1608266642,1608266644,1608269828,1608271343; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F18%2F06%3A13%3A38%3A326%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; s_pers=%20v8%3D1608280462607%7C1702888462607%3B%20v8_s%3DLess%2520than%25201%2520day%7C1608282262607%3B; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dplastic%2520pollution%2520in%2520five%2520urban%2520estuaries%2520of%2520kwazulu-natal%2520south%2520africa%3B%20e13%3Dqs%253Dplastic%2520pollution%2520in%2520five%2520urban%2520estuaries%2520of%2520kwazulu-natal%2520south%2520africa%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253DPlastic%2520pollution%2520in%2520five%2520urban%2520estuaries%2520of%2520KwaZulu-Natal%252C%2520South%2520Africa%3B%20s_ppvl%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C3%252C3%252C826%252C1707%252C826%252C1536%252C864%252C1.13%252CP%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_sq%3Delsevier-sd-prod%25252Celsevier-global-prod%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dsd%2525253Aproduct%2525253Ajournal%2525253Aarticle%252526link%25253DDownload%25252520Marine%25252520Pollution%25252520Bulletin%25252520Volume%25252520101%2525252C%25252520Issue%252525201%2525252C%2525252015%25252520December%252525202015%2525252C%25252520Pages%25252520473-480%25252520Baseline%25252520paper%25252520Plastic%25252520pollution%25252520in%25252520five%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dsd%2525253Aproduct%2525253Ajournal%2525253Aarticle%252526pidt%25253D1%252526oid%25253DfunctionHc%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DDIV%3B%20s_ppv%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C71%252C71%252C13291%252C1707%252C826%252C1536%252C864%252C1.13%252CP%3B; mbox=session%233f8c85f98ad24d04a5b8d35cf210133d%231608283465%7CPC%23f039e4d245604102907cc9d0a0c7f8ec.34_0%231671526405; Hm_lpvt_6c9e6e168b46aaa118c7ed52e9a02f43=1608281612'
    #fingerPrintToken=63871c623999df2bd167b51679758381; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18611%7CMCMID%7C15587988382064304172649633027284887076%7CMCAAMLH-1608549835%7C11%7CMCAAMB-1608549835%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1607952235s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1439495112%7CvVersion%7C5.0.0; sd_session_id=f00cf8fc9f8ac74e9f9a4e14d6a45e4cb4cfgxrqa; acw=f00cf8fc9f8ac74e9f9a4e14d6a45e4cb4cfgxrqa%7C%24%7CA0339B0C8D66E55CDC1A312DACC478DAB6E9E2611DFD1017C1353E7A6D9740B305ADA8ED04DEE5A45AE40E91CA7E2791925D36F4275D46DE3FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=952982594668D88579FF47BE38C0ABBCBB73BE8E9BD782C4D3647645F6D8FB3DBC7D357875DD0985D479CF8B659F9ABFCA7D8A38C0FBF64C; has_multiple_organizations=false; MIAMISESSION=fc9ac4c8-af43-41af-8330-983aa7a3d6c8:3785398115; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwNzk0NTMxNTE3MH0=; Hm_lvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607927767,1607945039,1607948786,1607948842; Hm_lpvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607948930; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F14%2F12%3A31%3A04%3A167%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1607950867802%3B%20v68%3D1607949064968%7C1607950867827%3B%20v8%3D1607949067870%7C1702557067870%3B%20v8_s%3DLess%2520than%25201%2520day%7C1607950867870%3B; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dmicroplastics%3B%20e13%3Dqs%253Dmicroplastics%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253Dmicroplastics%3B%20s_ppvl%3Dsd%25253Asearch%25253Aresults%25253Acustomer%25253Aanon%252C19%252C17%252C857.8181762695312%252C1396%252C676%252C1536%252C864%252C1.38%252CP%3B%20e41%3D1%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C5%252C5%252C676%252C507%252C676%252C1536%252C864%252C1.38%252CL%3B; mbox=session%233451e6bffb374082b325328628d070e1%231607950930%7CPC%23f039e4d245604102907cc9d0a0c7f8ec.34_0%231671193870'
    headers_get={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'cookie':cookie
    }
    url_search='https://www.sciencedirect.com/search'
    header_search={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }
    parms={
        'qs': 'Plastic pollution in five urban estuaries of KwaZulu-Natal, South Africa',
        'show':'25'
    }
    url='https://www.sciencedirect.com/science/article/pii/'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'cookie':cookie
    }
    url_get = 'https://www.sciencedirect.com/sdfe/arp/pii/'
    num = 0
    text_list=[]
    text_result=[]
    text_result_1=[]
    text_result_finally=[]
    ###########################################以上为主参数##############################################################
    response_search=requests.get(url=url_search,params=parms,headers=header_search).text
    t_response_search = re.findall(r'<a href=(.*?)>', response_search, re.S)
    print('爬取url头结束')
    t_result = re.findall(r'0-(.*?)-main', str(t_response_search), re.S)
    print("清洗url结束")
    #######################################################爬取Url头#####################################################
    print('正在存储url地址，请勿中断')
    with open('./save_url.txt','w',encoding='utf-8') as f:
        f.write(str(t_result))
        print('url地址储存完毕，储存地址为./save_url.txt')
    for line in t_result:
        print("开始请求第",num,"token")
        response = requests.get(url=url + line, headers=headers).text
        t = re.findall(r'"entitledToken":"(.*?)"', str(response), re.S)
        print("开始请求第",num,"文章")
    #写个正则识别entitledToken
        params={
            'entitledToken': t
        }
        response_article=requests.get(url=url_get+line+'/body?',params=params,headers=headers_get)
        print(response_article)
        response_article1=response_article.json()
        data_list = response_article1["content"]
        for dic in data_list:
            text_list.append(dic["$$"])
        for dic in text_list[0]:
            text_result.append(dic["$$"])
        for dic in text_result[0]:
            text_result_1.append(dic["$$"])
        for i in range(len(text_result_1)):
            for dic in text_result_1[i]:
                try:
                    text_result_finally.append(dic['_'])
                except KeyError:
                    continue
        num = num + 1
        with open('./elsevier_article.txt', 'a', encoding='utf-8') as fp:
            string1=str(text_result_finally)
            fp.write(string1)
    print("爬取25篇文章结束，休息几秒以免被墙")
    print("Sleeping", end="")
    for i in range(20):
        print(".", end='', flush=True)
        time.sleep(0.5)
