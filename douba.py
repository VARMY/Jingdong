from selenium import webdriver
import requests
import time
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# driver = webdriver.Chrome()


# world = input('请输入商品名称：')
#搜素商品
def first_get():

    driver.get('https://gou.jd.com/')
    driver.find_element_by_id('inputkey').send_keys(world)
    driver.find_element_by_class_name('btn').click()
    driver.implicitly_wait(30)
    page_num = driver.find_element_by_css_selector('#page span b').text
    return page_num


#获取商品的URL
def goods(page_num):
    list = []
    for num in range(1,int(page_num)-2):
        url = 'http://gou.jd.com/search?keyword='+world+'&page='+str(num)+'&sort=&expKey=&jdww=&wtype=&stock=&abt=searchbox&from=cps&cu=true&utm_source=gou.jd.com&utm_medium=uniongou&utm_campaign=t_220520384_&utm_term=7d1be08d690841a19d83f8c588090c44&abt=3'
        # print('开始获取第'+str(num)+'页的商品URL')
        driver.get(url)
        url_list =driver.find_elements_by_css_selector('.pic a')
        for i in url_list:
           list.append(i.get_attribute('href'))
        driver.implicitly_wait(30)
    return list



#获取商品的信息
def goods_data(url_list):
    # print(len(url_list))
    list_id = []
    for url in url_list[:3]:
         driver.get(url)
         # goods_name = driver.find_element_by_class_name('sku-name').text
         goods_id = driver.find_element_by_css_selector('.left-btns a').get_attribute('data-id')
         # goods_price = driver.find_element_by_css_selector('.p-price .price').text
         list_id.append(goods_id)
    return list_id

def maxPage(list_id):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1459&productId='+list_id+'&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
    response = requests.get(url)
    html = response.text
    print(html)


def comment(goods_id):
    comment_list = []
    for pag_num in range(0,3):
        url = 'http://club.jd.com/comment/productPageComments.action?productId='+goods_id+'&score=0&sortType=5&page='+str(pag_num)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
        comment_list.append(requests.get(url,headers=headers).json().get('maxPage'))
    print(comment_list)
    # try:
    #     for contents in  comment_list:
    #         for i in contents:
    #             if i['content'] != None:
    #                 comment = i['']['content']
    #                 print(comment)
    # except Exception:
    #         print('获取评价错误！')
        # comment_user = driver.find_elements_by_css_selector('.user-info')
        # praises = [i.text for i in driver.find_elements_by_class_name('J-nice')]
        # comment_time = [i.text for i in driver.find_elements_by_class_name('comment-time')]
        # comment_article = [i.text for i in driver.find_elements_by_css_selector('.comment-con')]
        # for user, praise, time, article in zip(comment_user,praises,comment_time,comment_article):
        #     data = {
        #         'comment_user':user.text,
        #         ''
        #     }
        #     print(data)
        # print(comment_user)
        # driver.implicitly_wait(30)
        # yield comment_user




def main():
    # page_num = first_get()
    # url_list = goods(page_num)
    # list_id = goods_data(url_list)
    # comment(l)
    maxPage('3901175')


if __name__ == '__main__':
    main()
