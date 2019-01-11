# -*- coding:utf-8 -*-

import random
import configparser
from Hero_Era_Pro import GetConn as Conn


def auto_create_hero(conn, num):
    """
    自动创建人物，包含人物姓名、人物性别和人物属性
    @ cp 读取配置文件内容
    @ last_names 接收配置文件中姓氏集
    @ first_names_female 接收配置文件中女性名集
    @ first_names_male 接收配置文件中男性名集
    @ hero_data 存储新建人物信息的字典，内容包含姓名，性别，统率，武力，智力，政治，魅力
    @ hero_types 存储着人物身份的list
    @ gen 随机生成性别参数
    @ types 随机生成身份参数
    @ last_name 随机从last_names姓氏集中选择一个作为新建人物姓氏
    @ first_name 依据gen参数的不同分别从first_names_female女性名集或first_names_male男性名集中随机选择一个作为新建人物名
    @ h_name 将随机选取的姓氏和名拼接为新建人物姓名
    @ h_gender 依据gen参数确定新建人物性别
    @ h_identity 随机生成新建人物身份
    @ h_lead 随机生成新建人物统率
    @ h_force 随机生成新建人物武力
    @ h_brain 随机生成新建人物智力
    @ h_politics 随机生成新建人物政治
    @ h_charm 随机生成新建人物魅力
    程序执行，调用MySQLConn来执行数据入库的操作
    @ n_gender 接收自动生成的num个英雄的姓名和性别list
    @ student 接收完整的学生信息字典
    :param conn: 数据库连接对象
    :param num: 需要生成的英雄信息条数
    :return: None
    """
    # 读取配置文件
    cp = configparser.ConfigParser()
    cp.read('./conf.cfg', encoding='utf-8')
    # 从配置文件中获取指定内容并进行格式化处理切分
    last_names = cp.get('NAME', 'LN').strip().replace('\n', ' ').split(' ')
    first_names_female = cp.get('NAME', 'FN1').strip().replace('\n', ' ').split(' ')
    first_names_male = cp.get('NAME', 'FN2').strip().replace('\n', ' ').split(' ')
    hero_data = dict()
    hero_type = ['统帅', '武将', '军师', '宰辅']
    for n in range(num):
        gen = random.randint(1, 2)
        types = random.randint(1, 4)
        last_name = random.choice(last_names)
        # a if k == v else b，这是三元运算写法，解读为当k=v为True时，返回a，为False时，返回b
        first_name = random.choice(first_names_female if gen == 1 else first_names_male)
        # '%s' % k，这是字符串占位符，使用%s占位，实际内容为k，中间使用%做格式化声明 
        h_name = '{0}{1}'.format(last_name, first_name)
        h_gender = '{}'.format('女' if gen == 1 else '男')
        h_age = random.randint(15, 60)
        h_identity = hero_type[types-1]
        hero_5 = type_hero(types)
        hero_data['h_name'] = h_name
        hero_data['h_gender'] = h_gender
        hero_data['h_age'] = h_age
        hero_data['h_identity'] = h_identity
        hero_data['h_lead'] = hero_5[0]
        hero_data['h_force'] = hero_5[1]
        hero_data['h_brain'] = hero_5[2]
        hero_data['h_politics'] = hero_5[3]
        hero_data['h_charm'] = hero_5[4]
        Conn.insert_data(conn, 'heroes', hero_data)
    print("当前游戏难度将诞生各类英雄共{}人！".format(num))
    

def new_hero(conn):
    """
    玩家新建英雄，需输入基本信息，自动生成身份及五维
    :param conn: 数据库连接对象
    :return: hero_data
    """
    # 存储新建英雄数据信息
    hero_data = dict()
    # 分别接收从控制台输入的姓名性别及年龄
    h_name = input('请输入英雄姓名，不得超过4个字：\n').strip()[:4]
    h_gender = input('请输入英雄性别：\n').strip()
    h_age = int(input('请输入英雄年龄（不得小于15岁且不得大于70岁）：\n').strip())
    # 重新生成属性的控制开关
    check = True
    # 身份备选列表
    hero_type = ['统帅', '武将', '军师', '宰辅']
    # 循环生成英雄属性，直到玩家确定英雄属性
    while check:
        # 随机获取一个身份
        types = random.randint(1, 4)
        h_identity = hero_type[types-1]
        # 调用type_hero()方法随机生成五维
        hero_5 = type_hero(types)
        print('新建英雄{0}\n性别：{1}\n年龄：{2}\n身份：{3}\n统率：{4}\n武力：{5}\n智力：{6}\n政治：{7}\n魅力：{8}'.format(
            h_name, h_gender, h_age, h_identity, hero_5[0], hero_5[1], hero_5[2], hero_5[3], hero_5[4]))
        if int(input('是否确定？\n1 确定创建  2 重新生成\n')) == 1:
            hero_data['h_id'] = 500
            hero_data['h_name'] = h_name
            hero_data['h_gender'] = h_gender
            hero_data['h_age'] = h_age
            hero_data['h_identity'] = h_identity
            hero_data['h_lead'] = hero_5[0]
            hero_data['h_force'] = hero_5[1]
            hero_data['h_brain'] = hero_5[2]
            hero_data['h_politics'] = hero_5[3]
            hero_data['h_charm'] = hero_5[4]
            Conn.insert_data(conn, 'heroes', hero_data)
            print('新建英雄{}成功！'.format(h_name))
            # 接收开关控制
            check = False
    return hero_data


def type_hero(types):
    """
    根据传入的types随机生成并返回一个五维数据
    :param types: 身份参考值
    :return: hero_5
    """
    # 英雄五维列表
    hero_5 = list()
    # 根据身份参考值分别生成对应范围的五维
    if types == 1:  # 统帅，高统
        h_lead = random.randint(80, 99)
        h_force = random.randint(50, 95)
        h_brain = random.randint(50, 95)
        h_politics = random.randint(50, 95)
        h_charm = random.randint(50, 99)
    elif types == 2:  # 武将，高武
        h_lead = random.randint(50, 95)
        h_force = random.randint(80, 99)
        h_brain = random.randint(50, 95)
        h_politics = random.randint(50, 95)
        h_charm = random.randint(50, 99)
    elif types == 3:  # 军师，高智
        h_lead = random.randint(50, 95)
        h_force = random.randint(50, 95)
        h_brain = random.randint(80, 99)
        h_politics = random.randint(50, 95)
        h_charm = random.randint(50, 99)
    else:  # 宰辅，高政
        h_lead = random.randint(50, 95)
        h_force = random.randint(50, 95)
        h_brain = random.randint(50, 95)
        h_politics = random.randint(80, 99)
        h_charm = random.randint(50, 99)
    hero_5.append(h_lead)
    hero_5.append(h_force)
    hero_5.append(h_brain)
    hero_5.append(h_politics)
    hero_5.append(h_charm)
    return hero_5
