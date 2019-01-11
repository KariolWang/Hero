
import random
from Hero_Era_Pro import PrintMsgs as PM, GetConn as Conn


def auto_create_group(conn, g_num, avg_num, r_num):
    """
    自动生成指定数量的势力，并随机分配一定范围内的英雄数到势力中，并修改相应的英雄状态和属性
    :param conn: 数据库操作对象
    :param g_num: 指定生成势力数
    :param avg_num: 指定分配到势力的英雄数
    :param r_num: 指定分配到势力的英雄数波动范围
    :return: None
    """
    # 获取英雄信息
    heroes = Conn.get_heroes(conn)
    # 主公备选英雄ID列表
    wait_list = list(heroes.keys())
    # 主公信息
    lord_dict = dict()
    # 新建势力信息
    build_group = dict()
    # 势力所属英雄信息
    g_hero = dict()
    # 循环创建g_num个势力
    for i in range(g_num):
        # 分配到各个势力的英雄数范围
        h_num = avg_num + random.randint(0, r_num)
        # 从主公候选英雄列表中随机获取一个英雄ID
        h_id = random.choice(wait_list)
        # 从候选名单中移除已经选中的英雄ID
        wait_list.remove(h_id)
        # 新建势力信息
        build_group['g_lord'] = h_id
        build_group['g_name'] = '{}军'.format(heroes.get(h_id).get('h_name'))
        # 调用方法创建势力（向数据库写入势力信息）
        Conn.insert_data(conn, 'hero_group', build_group)
        # 主公英雄属性变化，五维全部+5，修改h_group为势力ID，修改状态为主公
        lord_dict['h_group'] = i+1
        lord_dict['h_lead'] = heroes.get(h_id).get('h_lead') + 5
        lord_dict['h_force'] = heroes.get(h_id).get('h_force') + 5
        lord_dict['h_brain'] = heroes.get(h_id).get('h_brain') + 5
        lord_dict['h_politics'] = heroes.get(h_id).get('h_politics') + 5
        lord_dict['h_charm'] = heroes.get(h_id).get('h_charm') + 5
        lord_dict['h_status'] = 3
        # 数据库更新条件语句
        condition = 'h_id={}'.format(h_id)
        # 调用方法将英雄变更为主公（修改数据库内指定英雄的属性）
        Conn.update_data(conn, 'heroes', lord_dict, condition)
        # 循环分配特定个数的势力所属英雄
        for j in range(h_num):
            # 英雄属性变化
            g_hero['h_group'] = i+1
            g_hero['h_status'] = 2
            # 从英雄列表中随机选择一个英雄加入势力
            h_id = random.choice(wait_list)
            # 从英雄列表中移除已加入势力的英雄ID
            wait_list.remove(h_id)
            # 数据库更新条件语句
            condition = 'h_id={}'.format(h_id)
            # 调用方法将英雄变更为势力所属（修改数据库内指定英雄的属性）
            Conn.update_data(conn, 'heroes', g_hero, condition)
    print('当前游戏难度将新增敌对势力共{}个！'.format(g_num))
    

def new_group(conn, hero, c_num):
    """
    玩家新建势力
    :param conn: 数据库连接对象
    :param hero: 玩家新建英雄信息
    :param c_num: 当前游戏难度下新建势力可招揽的最大英雄数
    :return: None
    """
    # 新建势力信息
    build_group = dict()
    # 新主公信息
    lord_hero = dict()
    # 势力所属英雄信息
    g_hero = dict()
    # 势力信息
    build_group['g_id'] = 10
    build_group['g_lord'] = hero.get('h_id')
    build_group['g_name'] = '{}军'.format(hero.get('h_name'))
    # 调用方法创建新势力（向数据库中写入势力数据）
    Conn.insert_data(conn, 'hero_group', build_group)
    # 主公信息
    lord_hero['h_group'] = 10
    lord_hero['h_lead'] = hero.get('h_lead') + 5
    lord_hero['h_force'] = hero.get('h_force') + 5
    lord_hero['h_brain'] = hero.get('h_brain') + 5
    lord_hero['h_politics'] = hero.get('h_politics') + 5
    lord_hero['h_charm'] = hero.get('h_charm') + 5
    lord_hero['h_status'] = 3
    # 数据库更新条件语句
    condition = 'h_id={}'.format(hero.get('h_id'))
    # 调用方法更新主公属性（修改数据库中指定英雄的属性）
    Conn.update_data(conn, 'heroes', lord_hero, condition)
    # 获取英雄信息
    heroes = Conn.get_heroes(conn)
    # 候选英雄ID列表
    h_candidate = list()
    # 循环匹配在野英雄，并将英雄ID存放到候选英雄ID列表
    for k, v in heroes.items():
        if v.get('h_status') == 1:
            h_candidate.append(k)
    # 接收玩家选择的英雄ID，且只接收最大限定人数，并分割为列表存储
    PM.print_choice_hero(h_candidate, c_num, heroes)
    choices = input().strip().split(' ')[:c_num]
    # 循环更新所选英雄属性
    for choice in choices:
        g_hero['h_group'] = 10
        g_hero['h_status'] = 2
        condition = 'h_id={}'.format(choice)
        Conn.update_data(conn, 'heroes', g_hero, condition)
    print('新建势力{}成功！'.format(build_group.get('g_name')))
