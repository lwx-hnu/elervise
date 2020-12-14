import requests
import re

if __name__ == "__main__":
    list_token=[]
    headers_get={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'cookie':'__cfduid=d3bf05b9bfe7103f5e8fdf33e838a83ee1607916372; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; fingerPrintToken=63871c623999df2bd167b51679758381; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18611%7CMCMID%7C15587988382064304172649633027284887076%7CMCAAMLH-1608521649%7C11%7CMCAAMB-1608521649%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1607924049s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1439495112%7CvVersion%7C5.0.0; EUID=f80557a0-1a48-4676-a233-0d543c50f9a7; sd_session_id=2b32099d8a54f04b5b298450e96f8b2ea82agxrqa; acw=2b32099d8a54f04b5b298450e96f8b2ea82agxrqa%7C%24%7C9AD56A67FB18AF109EF05A794E934E1CF1CCCC78615BE5262365DD77FD1B3C62A21B6A52EAE64122E35589FBA092F206C1FB3048F7AFD5EF3FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=7FDADB3861A25AFE2C60FFC373DF6B2BD21758495713BB3FD7065D2128441CBA99F207CD2C40B334FDB75A0AB7F922E03D9FF82EC2CA1168; has_multiple_organizations=false; id_ab=B:100:8:f471f661-0103-4007-bc68-14fc02285b57; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F14%2F03%3A47%3A43%3A901%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; MIAMISESSION=e5c5fcae-92aa-4c45-b04f-50e3eb4a32b6:3785370528; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwNzkxNzcyODE5MX0=; mboxes=%7B%7D; usbls=1; Hm_lvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607917388,1607919719,1607920083,1607921759; Hm_lpvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607921759; mbox=session%2394a42734414d40d282ccdc9bd1b0cf1f%231607923625%7CPC%23f039e4d245604102907cc9d0a0c7f8ec.34_0%231671166565; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1607923565199%3B%20v68%3D1607921752051%7C1607923565221%3B%20v8%3D1607921765349%7C1702529765349%3B%20v8_s%3DFirst%2520Visit%7C1607923565349%3B; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dmicroplastic%3B%20e13%3Dqs%253Dmicroplastic%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253Dmicroplastic%3B%20e41%3D1%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_ppvl%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C10%252C2%252C2857.818115234375%252C574%252C676%252C1536%252C864%252C1.38%252CL%3B%20s_ppv%3Dsd%25253Asearch%25253Aresults%25253Acustomer%25253Aanon%252C13%252C13%252C676%252C574%252C676%252C1536%252C864%252C1.38%252CL%3B'
    }
    url_search='https://www.sciencedirect.com/search'
    header_search={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }
    parms={
        'qs': 'microplastics',
        'show':'25',
        'offset': '25',
        'navigation': 'true'
    }
    response_search=requests.get(url=url_search,params=parms,headers=header_search).text

    with open('./search_result.html','w',encoding='utf-8') as f_search:
        f_search.write(response_search)
    with open('./search_result.html','r',encoding='utf-8') as f_search:
        lines = f_search.read()
        t = re.findall(r'<a href=(.*?)>', lines, re.S)
        t_convert = ''.join(t)
        list = t_convert.split('.')
        with open('./search_result_clear.txt','w+',encoding='utf-8') as clear:
            for line in list:
                clear.write(line + '\r\n')  # 需进行类型转换
        ####写入清洗后的数据到search_result_clear.txt中
    with open('./search_result_clear.txt','r',encoding='utf-8') as clear1:
        lines = clear1.read()
        t = re.findall(r'0-(.*?)-main', lines, re.S)
        with open('./search_result_finally_clear.txt','w+',encoding='utf-8') as clear_finally:
            clear_finally.write(str(t) + '\r\n')  # 需进行类型转换
    with open('./search_result_finally_clear.txt','r',encoding='utf-8') as clear_finally:
        line1=clear_finally.read()
        list_clear = line1.split(',')
        list_clear=list_clear[:-1]
        list_clear[0]=list_clear[0].strip('[')
    #爬取首页，提取S********************，写个正则，提取S********************
    url='https://www.sciencedirect.com/science/article/pii/'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'Cookie': '__cfduid=d3bf05b9bfe7103f5e8fdf33e838a83ee1607916372; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; fingerPrintToken=63871c623999df2bd167b51679758381; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18611%7CMCMID%7C15587988382064304172649633027284887076%7CMCAAMLH-1608521649%7C11%7CMCAAMB-1608521649%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1607924049s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1439495112%7CvVersion%7C5.0.0; EUID=f80557a0-1a48-4676-a233-0d543c50f9a7; sd_session_id=2b32099d8a54f04b5b298450e96f8b2ea82agxrqa; acw=2b32099d8a54f04b5b298450e96f8b2ea82agxrqa%7C%24%7C9AD56A67FB18AF109EF05A794E934E1CF1CCCC78615BE5262365DD77FD1B3C62A21B6A52EAE64122E35589FBA092F206C1FB3048F7AFD5EF3FBA44D1BD4E4F2EAFE9C31A29ED2080B6DA1F7CB1786ABB; ANONRA_COOKIE=7FDADB3861A25AFE2C60FFC373DF6B2BD21758495713BB3FD7065D2128441CBA99F207CD2C40B334FDB75A0AB7F922E03D9FF82EC2CA1168; has_multiple_organizations=false; id_ab=B:100:8:f471f661-0103-4007-bc68-14fc02285b57; SD_ART_LINK_STATE=%3Ce%3E%3Cq%3Escience%3C%2Fq%3E%3Corg%3Erslt_list%3C%2Forg%3E%3Cz%3Erslt_list_item%3C%2Fz%3E%3CsrcFr%3Erslt_list_item%3C%2FsrcFr%3E%3Crdt%3E2020%2F12%2F14%2F03%3A47%3A43%3A901%3C%2Frdt%3E%3Cenc%3EN%3C%2Fenc%3E%3C%2Fe%3E; MIAMISESSION=e5c5fcae-92aa-4c45-b04f-50e3eb4a32b6:3785370528; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI2MDMzNCIsInRpbWVzdGFtcCI6MTYwNzkxNzcyODE5MX0=; mboxes=%7B%7D; usbls=1; mbox=session%2394a42734414d40d282ccdc9bd1b0cf1f%231607922640%7CPC%23f039e4d245604102907cc9d0a0c7f8ec.34_0%231671165580; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1607922584224%3B%20v68%3D1607920779849%7C1607922584245%3B%20v8%3D1607921710178%7C1702529710178%3B%20v8_s%3DFirst%2520Visit%7C1607923510178%3B; Hm_lvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607917388,1607919719,1607920083,1607921759; Hm_lpvt_6c9e6e168b46aaa118c7ed52e9a02f43=1607921759; s_sess=%20s_cpc%3D0%3B%20c21%3Dqs%253Dmicroplastic%3B%20e13%3Dqs%253Dmicroplastic%253A1%3B%20c13%3Drelevance-desc%3B%20e78%3Dqs%253Dmicroplastic%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_sq%3Delsevier-sd-prod%25252Celsevier-global-prod%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dsd%2525253Aproduct%2525253Ajournal%2525253Aarticle%252526link%25253DDownload%25252520Environmental%25252520Pollution%25252520Available%25252520online%252525205%25252520November%252525202020%2525252C%25252520115946%25252520In%25252520Press%2525252C%25252520Corrected%25252520ProofWhat%25252520are%25252520Corrected%25252520Proof%25252520arti%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dsd%2525253Aproduct%2525253Ajournal%2525253Aarticle%252526pidt%25253D1%252526oid%25253DfunctionHc%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DDIV%3B%20s_ppvl%3Dsd%25253Aproduct%25253Ajournal%25253Aarticle%252C10%252C2%252C2857.818115234375%252C574%252C676%252C1536%252C864%252C1.38%252CL%3B%20s_ppv%3Dsd%25253Asearch%25253Aresults%25253Acustomer%25253Aanon%252C13%252C13%252C676%252C574%252C676%252C1536%252C864%252C1.38%252CL%3B'
    }
    for line in list_clear:
        response = requests.get(url=url + line, headers=headers).text
        with open('./elsevier_token_inilzition.txt','a+',encoding='utf-8') as token:
            token.write(response)
        with open('./elsevier_token_inilzition.txt','r',encoding='utf-8') as token:
            lines = token.read()
            t = re.findall(r'entitledToken\":(.*?),', lines, re.S)
            with open('./entitledToken_finally_clear.txt', 'w+', encoding='utf-8') as token_clear:
                token_clear.write(str(t) + '\r\n')  # 需进行类型转换
    list_token=t
    #写个正则识别entitledToken
    for token_to_article,list_to_article in list_token,list_clear:
        prams={
            'entitledToken': token_to_article
        }
        url_get = 'https://www.sciencedirect.com/sdfe/arp/pii/S0269749120366355/body'
        response_get=requests.get(url=url_get+list_to_article+'/body',params=prams,headers=headers_get).text
        fp = open('./elsevier_key.html', 'w', encoding='utf-8')
        fp.write(response)
        fp.close()
        fp = open('./elsevier.html', 'w', encoding='utf-8')
        fp.write(response_get)
        fp.close()
        print(response_get)