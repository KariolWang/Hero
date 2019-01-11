import random
from Hero_Era_Pro import Manage_Group as MG, GetConn as Conn


def run(conn, time):
    ranker = Conn.get_ranker(conn)
    groups = Conn.get_groups(conn)
    heroes = Conn.get_heroes(conn)
    gems = Conn.get_gems(conn)
    for k, v in groups.items():
        if v.get('g_status') == 0:
            group = groups.get(k)
            g_id = group.get('g_id')
            group_hero = Conn.get_group_hero(conn, g_id)
            while True:
                # main_order = [0, 10] 命令选择参数
                # [0, 5) 内政 40%
                # [5, 7) 军政 30%
                # [7, 9) 英雄 20%
                # [9] 退朝 10%
                main_order = random.randint(0, 9)
                hero_id = list()
                check = 1
                # 内政
                if 0 <= main_order < 4:    # 0,1,2,3
                    manage_order = random.randint(1, 5)
                    if manage_order == 1:    # 经济
                        h_id = choice_hero(group_hero, heroes, 4)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        group = MG.get_economy(conn, group, heroes, hero_id, check)
                    elif manage_order == 2:  # 农业
                        h_id = choice_hero(group_hero, heroes, 4)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        group = MG.get_farming(conn, group, heroes, hero_id, check)
                    elif manage_order == 3:  # 军事
                        h_id = choice_hero(group_hero, heroes, 2)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        group = MG.get_military(conn, group, heroes, hero_id, check)
                    elif manage_order == 4:  # 科技
                        h_id = choice_hero(group_hero, heroes, 3)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        group = MG.get_science(conn, group, heroes, hero_id, check)
                    elif manage_order == 5:    # 民心
                        h_id = choice_hero(group_hero, heroes, 5)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        group = MG.get_morale(conn, group, heroes, hero_id, check)
                    if len(group_hero) == 0:
                        break
                # 军政
                elif 4 <= main_order < 7:    # 4, 5, 6
                    manage_order = random.randint(1, 4)
                    if manage_order == 1:    # 募兵
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                        max_ranker = round(group.get('g_populace') / 50)
                        new_ranker = random.randint(round(max_ranker / 10), max_ranker)
                        group = MG.get_ranker(conn, group, heroes, hero_id, max_ranker, new_ranker, check)
                    elif manage_order == 2:  # 训练
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    elif manage_order == 3:  # 巡逻
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    elif manage_order == 4:  # 征讨
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    if len(group_hero) == 0:
                        break
                # 英雄
                elif 7 <= main_order < 9:    # 7, 8
                    manage_order = random.randint(1, 1)
                    if manage_order == 1:  # 寻访
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    elif manage_order == 2:  # 辞退
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    elif manage_order == 3:  # 官职
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    elif manage_order == 4:  # 赏罚
                        h_id = choice_hero(group_hero, heroes, 1)
                        group_hero.remove(h_id)
                        hero_id.append(h_id)
                    if len(group_hero) == 0:
                        break
                # 退朝
                elif main_order == 9:
                    break
            group = MG.get_populace(conn, group)
            group = MG.eat_rations(conn, group, heroes, ranker)
            MG.check_group(conn, group, heroes, gems)
            if time % 3 == 0:
                group = MG.pay_provisions(conn, group, heroes, ranker)
                group = MG.get_gold(conn, group)
                MG.get_rations(conn, group)
            print('{}完成本月任务部署！'.format(group.get('g_name')))
        else:
            continue


def choice_hero(group_hero, heroes, k):
    """
    根据执行内容自动选择对应能力最高者来执行相应操作
    :param group_hero: 势力英雄id列表
    :param heroes: 所有英雄字典信息
    :param k: 对应能力参数    0为h_id  1为h_lead    2为h_force   3为h_brain   4为h_politics    5为h_charm
    :return: choice_id 返回选择的英雄id
    """
    hero = list()
    h_ids = list()
    lead = list()
    force = list()
    brain = list()
    politics = list()
    charm = list()
    for h_id in group_hero:
        h_ids.append(h_id)
        lead.append(heroes.get(h_id).get('h_lead'))
        force.append(heroes.get(h_id).get('h_force'))
        brain.append(heroes.get(h_id).get('h_brain'))
        politics.append(heroes.get(h_id).get('h_politics'))
        charm.append(heroes.get(h_id).get('h_charm'))
        hero = [h_ids, lead, force, brain, politics, charm]
    max_lead = max(hero[k])
    max_lead_index = hero[k].index(max_lead)
    choice_id = hero[0][max_lead_index]
    return choice_id
