import requests
import re
import json
import time
if __name__ == "__main__":
    list_token=[]
    list_title=[]
    cookie ='EUID=5ea52cd4-cf49-45bf-8060-2348e9a5efd1; utt=25051c183f9a371d7110744a3c8eb793e856907; id_ab=B:100:8:18813486-3343-4449-bbcd-f883519e7890; __cfduid=d6b28bea3ab6af7aa4e378d09fdc5be531606878959; mboxes=%7B%7D; sd_session_id=4a9342521ad88644ea2a7fa0521823a8c787gxrqa; acw=4a9342521ad88644ea2a7fa0521823a8c787gxrqa%7C%24%7CCED7C26C3AD01A1C12FB45429B1523E3326BDAAF718D93626FA098E4C9BE25CA377F22038F8D573736F6C19CA3FBD0A5F5D25A4D9D3E38693FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=84A8DCEC00875166EF2CC6AC1BCD93273376BB174D1E499580D149CB58E1AF535BBED4EA3DB496CF97ED5C4DF70D587E78828F171D9A86FD; has_multiple_organizations=false; __cf_bm=4467d21a08d3a26e28f0aa89bd81247e33544b7b-1608100484-1800-AaUydGQ1iMalwzSg3VscQikTLNqKTwjl106d2inyRp81YX0Uo5ldtnWKY7KQK0OUhCy6Y76iiNmoA2zlnknKH04=; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; fingerPrintToken=6f1fbfc09ce891b27134c4e48b0ca310; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18613%7CMCMID%7C22529632567077746793877409762714738845%7CMCAAMLH-1608705290%7C11%7CMCAAMB-1608705290%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1608107690s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.0.0%7CMCCIDH%7C-1439495112%7CMCSYNCSOP%7C411-18620; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F16%2F06%3A37%3A25%3A340%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; mbox=session%238a458bd5b60b479d9b76b1a71cfdc89a%231608102506%7CPC%2306e9d9d8219246e58d00fa1cedf67860.37_0%231671345446; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1608102512101%3B%20v68%3D1608100709222%7C1608102512139%3B%20v8%3D1608100712216%7C1702708712216%3B%20v8_s%3DMore%2520than%25207%2520days%7C1608102512216%3B; MIAMISESSION=765ce76c-0704-4020-9445-82fbe26ae280:3785553523; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwODEwMDcyMzU3N30=; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dmicroplastic%3B%20e13%3Dqs%253Dmicroplastic%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253Dmicroplastic%3B%20s_sq%3D%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_ppvl%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C2%252C2%252C410.9701461791992%252C1433%252C305%252C1536%252C864%252C1.34%252CP%3B%20s_ppv%3Dsd%25253Asearch%25253Aresults%25253Acustomer-standard%252C7%252C7%252C305%252C1433%252C305%252C1536%252C864%252C1.34%252CP%3B'
        #b57; mboxes=%7B%7D; fingerPrintToken=63871c623999df2bd167b51679758381; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18611%7CMCMID%7C15587988382064304172649633027284887076%7CMCAAMLH-1608549835%7C11%7CMCAAMB-1608549835%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1607952235s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1439495112%7CvVersion%7C5.0.0; sd_session_id=f00cf8fc9f8ac74e9f9a4e14d6a45e4cb4cfgxrqa; acw=f00cf8fc9f8ac74e9f9a4e14d6a45e4cb4cfgxrqa%7C%24%7CA0339B0C8D66E55CDC1A312DACC478DAB6E9E2611DFD1017C1353E7A6D9740B305ADA8ED04DEE5A45AE40E91CA7E2791925D36F4275D46DE3FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=952982594668D88579FF47BE38C0ABBCBB73BE8E9BD782C4D3647645F6D8FB3DBC7D357875DD0985D479CF8B659F9ABFCA7D8A38C0FBF64C; has_multiple_organizations=false; MIAMISESSION=fc9ac4c8-af43-41af-8330-983aa7a3d6c8:3785398115; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwNzk0NTMxNTE3MH0=; Hm_lvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607927767,1607945039,1607948786,1607948842; Hm_lpvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607948930; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F14%2F12%3A31%3A04%3A167%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1607950867802%3B%20v68%3D1607949064968%7C1607950867827%3B%20v8%3D1607949067870%7C1702557067870%3B%20v8_s%3DLess%2520than%25201%2520day%7C1607950867870%3B; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dmicroplastics%3B%20e13%3Dqs%253Dmicroplastics%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253Dmicroplastics%3B%20s_ppvl%3Dsd%25253Asearch%25253Aresults%25253Acustomer%25253Aanon%252C19%252C17%252C857.8181762695312%252C1396%252C676%252C1536%252C864%252C1.38%252CP%3B%20e41%3D1%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C5%252C5%252C676%252C507%252C676%252C1536%252C864%252C1.38%252CL%3B; mbox=session%233451e6bffb374082b325328628d070e1%231607950930%7CPC%23f039e4d245604102907cc9d0a0c7f8ec.34_0%231671193870'
    headers_get={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'cookie':cookie
    }
    url_search='https://www.sciencedirect.com/search'
    header_search={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }
    parms={
        'qs': 'microplastic',
        'offset': '25'
    }
    url='https://www.sciencedirect.com/science/article/pii/'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'cookie':cookie
    }
    url_get = 'https://www.sciencedirect.com/sdfe/arp/pii/'
    num = 0
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
        num = num + 1
        with open('./elsevier_article.txt', 'a', encoding='utf-8') as fp:
            json.dump(response_article1,fp,ensure_ascii=False)
    print("爬取25篇文章结束，休息几秒以免被墙")
    print("Sleeping", end="")
    for i in range(20):
        print(".", end='', flush=True)
        time.sleep(0.5)
