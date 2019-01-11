import queue
import random
import threading
import time

from Hero_Era_Pro import GetConn as Conn


def get_economy(conn, group, heroes, hero_id, check):
    """
    势力经济开发操作
    :param conn: 数据库连接对象
    :param group: 势力信息
    :param heroes: 英雄信息
    :param hero_id: 势力英雄ID列表
    :param check: 确认执行
    :return: group
    """
    if check == 1:
        # 定义一个字典接收势力变更信息
        new_group = dict()
        # 获取势力黄金
        g_gold = group.get('g_gold')
        # 计算本次执行任务的经费
        used_gold = 50 * len(hero_id)
        # 判断势力黄金数是否足够执行任务经费如果不足，则直接返还原group
        if g_gold < used_gold:
            if group.get('g_status') == 1:
                print('黄金不足！')
            return group
        # 获取势力经济
        g_economy = group.get('g_economy')
        # 获取势力科技
        g_science = group.get('g_science')
        # 执行英雄名称
        name = ''
        # 接收执行英雄的政治
        h_politics = 0
        # 传入多个执行英雄ID，循环累加英雄政治，拼接英雄名
        for h_id in hero_id:
            h_politics += heroes.get(h_id).get('h_politics')
            name += '{},'.format(heroes.get(h_id).get('h_name'))
        # 势力黄金减少执行英雄数*50两
        g_gold -= used_gold
        # 经济变化量受英雄政治和势力科技影响
        new_economy = random.randint(round(h_politics * 0.05 * (1 + g_science / 1000)),
                                     round(h_politics * 0.08 * (1 + g_science / 1000)))
        g_economy += new_economy
        if g_economy >= 1000:
            g_economy = 1000
            if group.get('g_status') == 1:
                print('势力经济已达最大值！')
        # 分别更新势力信息
        new_group['g_gold'] = g_gold
        group['g_gold'] = g_gold
        new_group['g_economy'] = g_economy
        group['g_economy'] = g_economy
        # 玩家势力输出信息，否则不输出
        if group.get('g_status') == 1:
            print('本月{0}执行任务共提升经济{1}点'.format(name[:-1], new_economy))
        condition = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_farming(conn, group, heroes, hero_id, check):
    """
    势力农业开发操作
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param check: 
    :return: group
    """
    if check == 1:
        new_group = dict()
        g_gold = group.get('g_gold')
        # 计算本次执行任务的经费
        used_gold = 50 * len(hero_id)
        # 判断势力黄金数是否足够执行任务经费如果不足，则直接返还原group
        if g_gold < used_gold:
            if group.get('g_status') == 1:
                print('黄金不足！')
            return group
        g_farming = group.get('g_farming')
        g_science = group.get('g_science')
        name = ''
        h_politics = 0
        for h_id in hero_id:
            h_politics += heroes.get(h_id).get('h_politics')
            name += '{},'.format(heroes.get(h_id).get('h_name'))
        g_gold -= used_gold
        new_group['g_gold'] = g_gold
        group['g_gold'] = g_gold
        # 农业变化量受英雄政治和势力科技影响
        new_farming = random.randint(round(h_politics * 0.05 * (1 + g_science / 1000)),
                                     round(h_politics * 0.08 * (1 + g_science / 1000)))
        g_farming += new_farming
        if g_farming >= 1000:
            g_farming = 1000
            if group.get('g_status') == 1:
                print('势力农业已达最大值！')
        new_group['g_farming'] = g_farming
        group['g_farming'] = g_farming
        if group.get('g_status') == 1:
            print('本月{0}执行任务共提升农业{1}点'.format(name[:-1], new_farming))
        condition = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_military(conn, group, heroes, hero_id, check):
    """
    势力军事操作
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param check: 
    :return: group
    """
    if check == 1:
        new_group = dict()
        g_gold = group.get('g_gold')
        # 计算本次执行任务的经费
        used_gold = 50 * len(hero_id)
        # 判断势力黄金数是否足够执行任务经费如果不足，则直接返还原group
        if g_gold < used_gold:
            if group.get('g_status') == 1:
                print('黄金不足！')
            return group
        g_military = group.get('g_military')
        g_science = group.get('g_science')
        name = ''
        h_force = 0
        for h_id in hero_id:
            h_force += heroes.get(h_id).get('h_force')
            name += '{},'.format(heroes.get(h_id).get('h_name'))
        g_gold -= used_gold
        new_group['g_gold'] = g_gold
        group['g_gold'] = g_gold
        # 军事变化量受英雄武力和势力科技影响
        new_military = random.randint(round(h_force * 0.05 * (1 + g_science / 1000)),
                                      round(h_force * 0.08 * (1 + g_science / 1000)))
        g_military += new_military
        if g_military >= 1000:
            g_military = 1000
            if group.get('g_status') == 1:
                print('势力军事已达最大值！')
        new_group['g_military'] = g_military
        group['g_military'] = g_military
        if group.get('g_status') == 1:
            print('本月{0}执行任务共提升军事{1}点'.format(name[:-1], new_military))
        condition = 'g_id = %s' % group.get('g_id')
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_science(conn, group, heroes, hero_id, check):
    """
    势力科技操作
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param check: 
    :return: group
    """
    if check == 1:
        new_group = dict()
        g_gold = group.get('g_gold')
        # 计算本次执行任务的经费
        used_gold = 50 * len(hero_id)
        # 判断势力黄金数是否足够执行任务经费如果不足，则直接返还原group
        if g_gold < used_gold:
            if group.get('g_status') == 1:
                print('黄金不足！')
            return group
        g_science = group.get('g_science')
        name = ''
        h_brain = 0
        for h_id in hero_id:
            h_brain += heroes.get(h_id).get('h_brain')
            name += '%s,' % heroes.get(h_id).get('h_name')
        g_gold -= used_gold
        new_group['g_gold'] = g_gold
        group['g_gold'] = g_gold
        # 科技变化量受英雄智力和势力科技影响
        new_science = random.randint(round(h_brain * 0.05 * (1 + g_science / 1000)),
                                     round(h_brain * 0.08 * (1 + g_science / 1000)))
        g_science += new_science
        if g_science >= 1000:
            g_science = 1000
            if group.get('g_status') == 1:
                print('势力科技已达最大值！')
        new_group['g_science'] = g_science
        group['g_science'] = g_science
        if group.get('g_status') == 1:
            print('本月{0}执行任务共提升科技{1}点'.format(name[:-1], new_science))
        condition = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_morale(conn, group, heroes, hero_id, check):
    """
    势力民心操作
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param check: 
    :return: group
    """
    if check == 1:
        new_group = dict()
        g_gold = group.get('g_gold')
        # 计算本次执行任务的经费
        used_gold = 50 * len(hero_id)
        # 判断势力黄金数是否足够执行任务经费如果不足，则直接返还原group
        if g_gold < used_gold:
            if group.get('g_status') == 1:
                print('黄金不足！')
            return group
        g_morale = group.get('g_morale')
        name = ''
        h_charm = 0
        for h_id in hero_id:
            h_charm += heroes.get(h_id).get('h_charm')
            name += '{},'.format(heroes.get(h_id).get('h_name'))
        g_gold -= used_gold
        new_group['g_gold'] = g_gold
        group['g_gold'] = g_gold
        # 民心变化量受英雄魅力和势力民心影响
        new_morale = random.randint(round(h_charm * 0.08 * (1 + g_morale / 1000)),
                                    round(h_charm * 0.1 * (1 + g_morale / 1000)))
        g_morale += new_morale
        if g_morale >= 1000:
            g_morale = 1000
            if group.get('g_status') == 1:
                print('势力民心已达最大值！')
        new_group['g_morale'] = g_morale
        group['g_morale'] = g_morale
        if group.get('g_status') == 1:
            print('本月{0}执行任务共提升民心{1}点'.format(name[:-1], new_morale))
        condition = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_gold(conn, group):
    """
    势力黄金收入
    :param conn: 
    :param group: 
    :return: group
    """
    g_gold = group.get('g_gold')
    g_economy = group.get('g_economy')
    g_populace = group.get('g_populace')
    g_science = group.get('g_science')
    new_group = dict()
    # 黄金收入量受势力经济和势力人口以及势力科技影响
    new_gold = random.randint(round(g_economy * g_populace * (1 + g_science / 1000) / 1000),
                              round(g_economy * g_populace * (1 + g_science / 1000) / 800))
    g_gold += new_gold
    new_group['g_gold'] = g_gold
    group['g_gold'] = g_gold
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本季度{0}获得黄金{1}两'.format(group.get('g_name'), new_gold))
    return group


def get_rations(conn, group):
    """
    势力粮草收入
    :param conn: 
    :param group: 
    :return: group
    """
    g_rations = group.get('g_rations')
    g_farming = group.get('g_farming')
    g_populace = group.get('g_populace')
    g_science = group.get('g_science')
    new_group = dict()
    # 粮草收入量受势力农业和势力人口以及势力科技影响
    new_rations = random.randint(round(g_farming * g_populace * (1 + g_science / 1000) / 500),
                                 round(g_farming * g_populace * (1 + g_science / 1000) / 300))
    g_rations += new_rations
    new_group['g_rations'] = g_rations
    group['g_rations'] = g_rations
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本季度{0}收获粮草{1}石'.format(group.get('g_name'), new_rations))
    return group


def get_ranker(conn, group, heroes, hero_id, max_ranker, new_ranker, check):
    """
    势力募兵操作
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param max_ranker: 
    :param new_ranker: 
    :param check: 
    :return: group
    """
    if check == 1:
        g_populace = group.get('g_populace')
        g_ranker = group.get('g_ranker')
        g_rations = group.get('g_rations')
        g_gold = group.get('g_gold')
        g_morale = group.get('g_morale')
        new_group = dict()
        name = ''
        h_lead = 0
        if g_rations < 0:
            return group
        for h_id in hero_id:
            h_lead += heroes.get(h_id).get('h_lead')
            name += '{},'.format(heroes.get(h_id).get('h_name'))
        if new_ranker > max_ranker:
            new_ranker = max_ranker
        g_ranker += new_ranker
        if g_ranker > g_populace / 10:
            new_ranker = round(g_populace / 10) - (g_ranker - new_ranker)
            if group.get('g_status') == 1:
                print('因势力兵力不得超过总人口的十分之一，所以本次招募最大兵力为{}'.format(new_ranker))
            g_ranker = round(g_populace / 10)
        h_buff = round(h_lead * (1 + g_morale / 1000) / 20)
        # 募兵消耗粮草和黄金，并影响势力民心，消耗量受执行英雄统率影响
        new_rations = round(new_ranker / 50 - h_buff) if new_ranker / 50 - h_buff > 0 else 0
        new_gold = round(new_ranker / 200 - h_buff) if new_ranker / 200 - h_buff > 0 else 0
        new_morale = round(new_ranker / 1000) if new_ranker / 1000 > 0 else 0
        new_morale = 20 if new_morale > g_morale * 0.3 else new_morale
        g_populace -= new_ranker
        g_rations -= new_rations
        g_gold -= new_gold
        g_morale -= new_morale
        new_group['g_populace'] = g_populace
        new_group['g_rations'] = g_rations
        new_group['g_gold'] = g_gold
        new_group['g_morale'] = g_morale
        new_group['g_ranker'] = g_ranker
        group['g_populace'] = g_populace
        group['g_rations'] = g_rations
        group['g_gold'] = g_gold
        group['g_morale'] = g_morale
        group['g_ranker'] = g_ranker
        if group.get('g_status') == 1:
            print('本次{0}成功招募士兵共{1}人，消耗粮草{2}石，消耗黄金{3}两，降低民心{4}点，减少人口{5}人'.format(
                name[:-1], new_ranker, new_rations, new_gold, new_morale, new_ranker))
        condition = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def get_populace(conn, group):
    """
    势力人口操作
    :param conn: 
    :param group: 
    :return: group
    """
    g_populace = group.get('g_populace')
    g_morale = group.get('g_morale')
    new_group = dict()
    # 人口增加量受势力人口和势力民心影响
    new_populace = random.randint(round(g_populace * (1 + g_morale / 1000) / 300),
                                  round(g_populace * (1 + g_morale / 1000) / 100))
    # 人口增加会降低势力民心，降低量受新增人口和势力民心影响
    new_morale = round(new_populace / (1000 * (1 + g_morale / 1000)))
    new_morale = new_morale if new_morale >= 1 else 1
    g_populace += new_populace
    g_morale -= new_morale
    new_group['g_populace'] = g_populace
    new_group['g_morale'] = g_morale
    group['g_morale'] = g_morale
    group['g_populace'] = g_populace
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本月{0}新增人口{1}人，民心减少{2}点'.format(group.get('g_name'), new_populace, new_morale))
    return group


def eat_rations(conn, group, heroes, ranker):
    """
    势力粮草消耗
    :param conn: 
    :param group: 
    :param heroes: 
    :param ranker: 
    :return: group
    """
    g_rations = group.get('g_rations')
    g_ranker = ranker.get(group.get('g_corps'))
    new_group = dict()
    ranker_eat = round(group.get('g_ranker') * g_ranker.get('r_force') * 0.3 + 1)
    hero_eat = 0
    for h_id in Conn.get_group_hero(conn, group.get('g_id')):
        hero_eat += round(heroes.get(h_id).get('h_force') / 20 + 1)
    g_eat = hero_eat + ranker_eat
    g_rations -= g_eat
    new_group['g_rations'] = g_rations
    group['g_rations'] = g_rations
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本月{0}消耗粮草{1}石'.format(group.get('g_name'), g_eat))
    return group


def pay_provisions(conn, group, heroes, ranker):
    """
    势力军饷发放
    :param conn: 
    :param group: 
    :param heroes: 
    :param ranker: 
    :return: group
    """
    g_gold = group.get('g_gold')
    g_ranker = ranker.get(group.get('g_corps'))
    new_group = dict()
    pay_ranker = round(group.get('g_ranker') * (g_ranker.get('r_force') + g_ranker.get('r_defense')) / 10)
    pay_hero = 0
    for h_id in Conn.get_group_hero(conn, group.get('g_id')):
        pay_hero += round((heroes.get(h_id).get('h_lead') * 1.1 + heroes.get(h_id).get('h_force') * 1.2
                           + heroes.get(h_id).get('h_brain') * 1.1 + heroes.get(h_id).get('h_politics') * 1.1
                           + heroes.get(h_id).get('h_charm') * 0.8) / 10)
    g_pay = pay_hero + pay_ranker
    g_gold -= g_pay
    new_group['g_gold'] = g_gold
    group['g_gold'] = g_gold
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本季度{0}发放军饷黄金{1}两'.format(group.get('g_name'), g_pay))
    return group


def check_group(conn, group, heroes, gems):
    """
    势力现状评定，有几率触发特殊事件
    :param gems: 
    :param conn: 
    :param group: 
    :param heroes: 
    :return: group
    """
    g_morale = group.get('g_morale')
    g_gold = group.get('g_gold')
    g_rations = group.get('g_rations')
    g_ranker = group.get('g_ranker')
    g_populace = group.get('g_populace')
    group_hero = Conn.get_group_hero(conn, group.get('g_id'))
    # 下野英雄信息字典
    retire = dict()
    # 势力变更信息字典
    new_group = dict()
    # 势力变更开关
    check_g = False
    # 英雄变更开关
    check_h = False
    # 黄金小于0
    if g_gold < 0:
        k = random.random()
        if 0.2 < k < 0.7:
            # 兵力哗变叛逃
            deserter = random.randint(round(g_ranker * 0.05), round(g_ranker * 0.1))
            g_ranker -= deserter
            group['g_ranker'] = g_ranker
            new_group['g_ranker'] = g_ranker
            print('因{0}军饷不足，{1}名士兵哗变叛逃了！'.format(group.get('g_name'), deserter))
            check_g = True
        if 0.5 < k < 0.55:
            # 英雄辞官下野
            h_id = random.choice(group_hero)
            group_hero.remove(h_id)
            retire[h_id] = {
                'h_group': 0,
                'h_status': 1
            }
            print('因{0}军饷不足，{1}辞官下野了！'.format(group.get('g_name'), heroes.get(h_id).get('h_name')))
            check_h = True
    # 粮草小于0
    if g_rations < 0:
        k = random.random()
        if 0.2 < k < 0.8:
            # 兵力哗变叛逃
            deserter = random.randint(round(g_ranker * 0.08), round(g_ranker * 0.15))
            g_ranker -= deserter
            group['g_ranker'] = g_ranker
            new_group['g_ranker'] = g_ranker
            print('因{0}粮草不足，{1}名士兵哗变叛逃了！'.format(group.get('g_name'), deserter))
        if 0.53 < k < 0.55:
            # 英雄辞官下野
            h_id = random.choice(group_hero)
            group_hero.remove(h_id)
            retire[h_id] = {
                'h_group': 0,
                'h_status': 1
            }
            print('因{0}粮草不足，{1}辞官下野了！'.format(group.get('g_name'), heroes.get(h_id).get('h_name')))
            check_h = True
        g_ranker = round(g_ranker * 0.6)
        g_populace += round(g_ranker * 0.4)
        g_gold += round(g_ranker * 0.4 / 100)
        new_group['g_ranker'] = g_ranker
        new_group['g_gold'] = g_gold
        new_group['g_populace'] = g_populace
        group['g_ranker'] = g_ranker
        group['g_gold'] = g_gold
        group['g_populace'] = g_populace
        check_g = True
    # 民心大于600
    if g_morale > 600:
        k = random.random()
        if 0.3 < k < 0.7:
            # 人口迁入
            follower = random.randint(round(g_populace * 0.05), round(g_populace * 0.08))
            g_populace += follower
            group['g_populace'] = g_populace
            new_group['g_populace'] = g_populace
            print('因{0}民心所向，人口迁入了{1}人！'.format(group.get('g_name'), follower))
            check_g = True
        if 0.4 < k < 0.6:
            # 钱粮捐献
            gold = random.randint(round(g_populace / 500), round(g_populace / 200))
            rations = random.randint(round(g_populace / 80), round(g_populace / 30))
            g_gold += gold
            g_rations += rations
            group['g_gold'] = g_gold
            group['g_rations'] = g_rations
            new_group['g_gold'] = g_gold
            new_group['g_rations'] = g_rations
            print('因{0}民心所向，民众发起粮草捐赠，粮草增加{1}石，黄金增加{2}两！'.format(group.get('g_name'), rations, gold))
            check_g = True
        if 0.5 < k < 0.55:
            # 志愿参军
            volunteer = random.randint(round(g_populace * 0.003), round(g_populace * 0.08))
            g_ranker += volunteer
            g_populace -= volunteer
            group['g_ranker'] = g_ranker
            group['g_populace'] = g_populace
            new_group['g_ranker'] = g_ranker
            new_group['g_populace'] = g_populace
            print('因{0}民心所向，民众发起志愿参军，兵力增加{1}名！'.format(group.get('g_name'), volunteer))
            check_g = True
        if 0.52 < k < 0.53:
            # 进贡宝物
            new_gems = dict()
            treasure = Conn.find_treasure(conn)
            t_id = random.choice(treasure)
            new_gems['t_group'] = group.get('g_id')
            condition_t = 't_id = {}'.format(t_id)
            print('因{0}民心所向，民众进贡传家宝物，{0}获得宝物{1}！'.format(group.get('g_name'), gems.get(t_id).get('t_name')))
            Conn.update_data(conn, 'gems', new_gems, condition_t)
    # 民心大于300
    elif g_morale > 300:
        k = random.random()
        if 0.5 < k < 0.6:
            # 人口迁入
            follower = random.randint(round(g_populace * 0.03), round(g_populace * 0.06))
            g_populace += follower
            group['g_populace'] = g_populace
            new_group['g_populace'] = g_populace
            print('因{0}民心所向，人口迁入了{1}人！'.format(group.get('g_name'), follower))
            check_g = True
        if 0.55 < k < 0.6:
            # 钱粮捐献
            gold = random.randint(round(g_populace / 500), round(g_populace / 200))
            rations = random.randint(round(g_populace / 80), round(g_populace / 30))
            g_gold += gold
            g_rations += rations
            group['g_gold'] = g_gold
            group['g_rations'] = g_rations
            new_group['g_gold'] = g_gold
            new_group['g_rations'] = g_rations
            print('因{0}民心所向，民众发起粮草捐赠，粮草增加{1}石，黄金增加{2}两！'.format(group.get('g_name'), rations, gold))
            check_g = True
    # 民心大于100
    elif g_morale > 100:
        k = random.random()
        if 0.5 < k < 0.6:
            # 人口迁入
            follower = random.randint(round(g_populace * 0.01), round(g_populace * 0.03))
            g_populace += follower
            group['g_populace'] = g_populace
            new_group['g_populace'] = g_populace
            print('因{0}民心所向，人口迁入了{1}人！'.format(group.get('g_name'), follower))
            check_g = True
    # 民心小于30
    if 10 < g_morale < 30:
        k = random.random()
        if 0.5 < k < 0.7:
            # 人口流失
            refugee = random.randint(round(g_populace * 0.03), round(g_populace * 0.05))
            g_populace -= refugee
            group['g_populace'] = g_populace
            new_group['g_populace'] = g_populace
            print('因{0}民心不足，人口流失了{1}人！'.format(group.get('g_name'), refugee))
            check_g = True
    # 民心小于10
    elif g_morale < 10:
        # 人口流失
        refugee = random.randint(round(g_populace * 0.05), round(g_populace * 0.08))
        g_populace -= refugee
        # 士兵哗变叛逃
        deserter = random.randint(round(g_ranker * 0.05), round(g_ranker * 0.08))
        g_ranker -= deserter
        group['g_ranker'] = g_ranker
        new_group['g_ranker'] = g_ranker
        group['g_populace'] = g_populace
        new_group['g_populace'] = g_populace
        print('因{0}民心不足，人口流失了{1}人，{2}名士兵哗变叛逃了！'.format(group.get('g_name'), refugee, deserter))
        check_g = True
    if check_g:
        condition_g = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition_g)
    if check_h:
        for hid in retire.keys():
            condition_h = 'h_id = {}'.format(hid)
            Conn.update_data(conn, 'heroes', retire.get(hid), condition_h)
    return group


def find_recluse_treasure(conn, group, heroes, hero_id, gems):
    """
    寻访，概率寻访到在野英雄、在野宝物、黄金、粮草
    :param hero_id: 
    :param conn: 
    :param group: 
    :param heroes: 
    :param gems: 
    :return: group
    """
    # 在野英雄ID列表
    recluse = Conn.find_recluse(conn)
    # 在野宝物ID列表
    treasure = Conn.find_treasure(conn)
    # 势力变更信息及开关
    new_group = dict()
    check_g = False
    # 英雄变更信息
    new_hero = dict()
    # 宝物变更信息
    new_gem = dict()
    # 获取势力钱粮信息
    g_rations = group.get('g_rations')
    g_gold = group.get('g_gold')
    for h_id in hero_id:
        # 概率参数
        # [0, 0.3) 30%概率寻访没有收获
        # [0.3, 0.5) 20%概率寻访发现粮草
        # [0.5, 0.7) 20%概率寻访发现黄金
        # [0.7, 0.9) 20%概率寻访发现英雄
        # [0.9, 1] 10%概率寻访发现宝物
        k = random.random() * (1 - random.random())
        if len(treasure) < 1 and len(recluse) > 0:
            k -= 0.11
        elif len(recluse) < 1 and len(treasure) > 0:
            k = 0.99
        elif len(recluse) + len(treasure) < 1:
            k -= 0.31
        hero = heroes.get(h_id)
        if 0.2 <= k < 0.45:
            rations = random.randint(hero.get('h_brain') + hero.get('h_charm'),
                                     (hero.get('h_brain') + hero.get('h_charm')) * 2)
            g_rations += rations
            group['g_rations'] = g_rations
            new_group['g_rations'] = g_rations
            if group.get('g_status') == 1:
                print('{0}发现粮草，{1}粮草增加{2}'.format(hero.get('h_name'), group.get('g_name'), rations))
            check_g = True
        elif 0.45 <= k < 0.7:
            gold = random.randint(hero.get('h_brain') + hero.get('h_charm'),
                                  (hero.get('h_brain') + hero.get('h_charm')) * 3)
            g_gold += gold
            group['g_gold'] = g_gold
            new_group['g_gold'] = g_gold
            if group.get('g_status') == 1:
                print('{0}发现黄金，{1}黄金增加{2}'.format(hero.get('h_name'), group.get('g_name'), gold))
            check_g = True
        elif 0.7 <= k < 0.9:
            # 发现英雄ID
            try:
                re_id = random.choice(recluse)
            except Exception as e:
                print(e)
                print('{}本次寻访未发现任何事物'.format(hero.get('h_name')))
                continue
            # 英雄投奔概率
            # 受寻访英雄的智力和魅力值影响
            hero_1 = (hero.get('h_brain') + hero.get('h_charm')) / 2
            hero_2 = (heroes.get(re_id).get('h_brain') + heroes.get(re_id).get('h_charm')) / 2
            if group.get('g_status') == 1:
                print('{0}发现在野英雄{1}！是否选择招揽！'.format(hero.get('h_name'), heroes.get(re_id).get('h_name')))
                print('姓名：{0}\n性别：{1}\n年龄：{2}\n身份：{3}\n统率：{4}\n武力：{5}\n智力：{6}\n政治：{7}\n魅力：{8}'.format(
                    heroes.get(re_id).get('h_name'), heroes.get(re_id).get('h_gender'), heroes.get(re_id).get('h_age'),
                    heroes.get(re_id).get('h_identity'), heroes.get(re_id).get('h_lead'), heroes.get(re_id).get('h_force'),
                    heroes.get(re_id).get('h_brain'), heroes.get(re_id).get('h_politics'), heroes.get(re_id).get('h_charm'))
                )
                is_get = int(input('1 招揽  2 放弃\n'))
                if is_get == 1:
                    choice = hero_1 / hero_2 - random.random()
                    print('{}：阁下慢走，方才见阁下举止不凡，一表人才，想来阁下绝非常人，何不投效我军，谋一个出路？'.format(hero.get('h_name')))
                    if choice > 0.6:
                        print('{0}：久闻{1}大名，承蒙不弃，{0}愿效死力！'.format(heroes.get(re_id).get('h_name'), group.get('g_name')))
                        print('{0}：哈哈，我军得{1}相助，何愁天下不平？'.format(hero.get('h_name'), heroes.get(re_id).get('h_name')))
                    else:
                        print('{0}：多谢大人好意，然{0}并无意出仕，还望大人恕罪。'.format(heroes.get(re_id).get('h_name')))
                        print('{0}：唉，既如此，{0}也不好再为难阁下，告辞。'.format(hero.get('h_name')))
                    if choice > 0.6:
                        new_hero['h_group'] = group.get('g_id')
                        new_hero['h_status'] = 2
                        recluse.remove(re_id)
                        print('{0}成功招揽到英雄{1}！'.format(group.get('g_name'), heroes.get(re_id).get('h_name')))
                        condition_h = 'h_id = {}'.format(re_id)
                        Conn.update_data(conn, 'heroes', new_hero, condition_h)
        elif 0.9 <= k <= 1:
            # 发现宝物ID
            # 受势力民心影响
            treasure = [t_id for t_id in treasure if gems.get(t_id).get('t_level') < (
                2 if group.get('g_morale') < 100 else 3 if group.get('g_morale') < 500 else 4)]
            tr_id = random.choice(treasure)
            new_gem['t_group'] = group.get('g_id')
            condition_t = 't_id = {}'.format(tr_id)
            if group.get('g_status') == 1:
                print('{0}成功寻获到宝物{1}！'.format(hero.get('h_name'), gems.get(tr_id).get('t_name')))
            Conn.update_data(conn, 'gems', new_gem, condition_t)
        else:
            if group.get('g_status') == 1:
                print('{}本次寻访未发现任何事物'.format(hero.get('h_name')))
    if check_g:
        condition_g = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, condition_g)
    return group


def rewards_hero(conn, group, gems, t_id, heroes, h_id, check):
    """
    对势力英雄进行宝物赏赐与罚没
    :param h_id: 
    :param group: 
    :param check: 
    :param conn: 
    :param gems: 
    :param t_id: 
    :param heroes: 
    :return: heroes
    """
    new_gem = dict()
    new_hero = dict()
    gem = gems.get(t_id)
    hero = heroes.get(h_id)
    # 赏赐
    if check == 1:
        new_gem['t_hero'] = h_id
        new_hero['h_lead'] = hero.get('h_lead') + gem.get('t_lead')
        new_hero['h_force'] = hero.get('h_force') + gem.get('t_force')
        new_hero['h_brain'] = hero.get('h_brain') + gem.get('t_brain')
        new_hero['h_politics'] = hero.get('h_politics') + gem.get('t_politics')
        new_hero['h_charm'] = hero.get('h_charm') + gem.get('t_charm')
        condition_t = 't_id = {}'.format(t_id)
        condition_h = 'h_id = {}'.format(h_id)
        Conn.update_data(conn, 'gems', new_gem, condition_t)
        Conn.update_data(conn, 'heroes', new_hero, condition_h)
        if group.get('g_status') == 1:
            print('{0}获得赏赐宝物{1},属性提升！'.format(hero.get('h_name'), gem.get('t_name')))
            print('{}:臣叩谢圣恩，必鞠躬尽瘁，死而后已！'.format(hero.get('h_name')))
    # 收回
    else:
        new_gem['t_hero'] = 0
        new_hero['h_lead'] = hero.get('h_lead') - gem.get('t_lead')
        new_hero['h_force'] = hero.get('h_force') - gem.get('t_force')
        new_hero['h_brain'] = hero.get('h_brain') - gem.get('t_brain')
        new_hero['h_politics'] = hero.get('h_politics') - gem.get('t_politics')
        new_hero['h_charm'] = hero.get('h_charm') - gem.get('t_charm')
        condition_t = 't_id = {}'.format(t_id)
        condition_h = 'h_id = {}'.format(h_id)
        Conn.update_data(conn, 'gems', new_gem, condition_t)
        Conn.update_data(conn, 'heroes', new_hero, condition_h)
        if group.get('g_status') == 1:
            print('{0}失去宝物{1},属性下降！'.format(hero.get('h_name'), gem.get('t_name')))
            print('{}:臣有负圣望，甘受惩罚，绝无怨言！'.format(hero.get('h_name')))
    heroes = Conn.get_heroes(conn)
    return heroes


def change_corps(conn, group, ranker, choice):
    """
    变更势力兵种，会依据变更的兵种消耗不同数量的黄金
    :param choice: 
    :param conn: 
    :param group: 
    :param ranker: 
    :return: group
    """
    g_gold = group.get('g_gold')
    g_corps = group.get('g_corps')
    o_gold = round(group.get('g_ranker')*(ranker.get(g_corps).get('r_force')+ranker.get(g_corps).get('r_defense'))/40)
    u_gold = round(group.get('g_ranker')*(ranker.get(choice).get('r_force')+ranker.get(choice).get('r_defense'))/20)
    new_gold = g_gold - (u_gold-o_gold)
    new_group = dict()
    if g_gold >= u_gold:
        new_group['g_corps'] = choice
        new_group['g_gold'] = new_gold
        group['g_gold'] = new_gold
        condition = 'g_id = {}'.format(group.get('g_id'))
        if group.get('g_status') == 1:
            print('{0}兵种变更为{1}，共花费黄金{2}两！'.format(group.get('g_name'), ranker.get(choice).get('r_name'), u_gold))
        Conn.update_data(conn, 'hero_group', new_group, condition)
        return group


def train_corps(conn, group, heroes, hero_id, t_type):
    """
    训练势力兵种，获得兵种经验。
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param t_type: 
    :return: 
    """
    new_group = dict()
    g_experience = group.get('g_experience')
    g_ranker = group.get('g_ranker')
    h_lead = 0
    h_force = 0
    name = ''
    for h_id in hero_id:
        h_lead += heroes.get(h_id).get('h_lead')
        h_force += heroes.get(h_id).get('h_force')
        name += '{},'.format(heroes.get(h_id).get('h_name'))
    if t_type == 1:
        exp = round(h_lead*10/g_ranker) if round(h_lead*10/g_ranker) > 0 else 1
    else:
        exp = round((h_lead+h_force)*10/g_ranker) if round(h_lead*10/g_ranker) > 0 else 1
    g_experience += exp
    group['g_experience'] = g_experience
    new_group['g_experience'] = g_experience
    condition = 'g_id={}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    if group.get('g_status') == 1:
        print('本月{0}完成训练，势力兵种经验提升{1}点'.format(name[:-1], exp))
        if g_experience >= 50 and group.get('g_corps') < 2:
            print('当前兵种可升级！')
        elif g_experience >= 200 and group.get('g_corps') < 3:
            print('当前兵种可升级！')
        elif g_experience >= 450 and group.get('g_corps') < 4:
            print('当前兵种可升级！')
        elif g_experience >= 950 and group.get('g_corps') < 5:
            print('当前兵种可升级！')
    return group


def find_spy(group):
    """
    生成贼寇探子
    贼寇探子：
        s_force 武力值
        s_gold 黄金
    :return: spy
    """
    spy = dict()
    num = random.randint(1, 3)
    if group.get('g_status') == 1:
        print('发现贼寇{}人，请派遣英雄前往剿灭！'.format(num))
        print('{0:<6}\t{1:<4}'.format('贼寇类型', '贼寇武力'))
    for i in range(num):
        s_name = random.choice(['山贼', '土匪', '强盗', '蛮夷', '流寇', '叛将'])
        s_force = random.randint(60, 90)
        s_gold = random.randint(round(s_force * 1.5), round(s_force * 2.5))
        spy[i+1] = {
            's_name': s_name,
            's_force': s_force,
            's_gold': s_gold
        }
        if group.get('g_status') == 1:
            print('{0:<6}\t{1:<4}'.format(s_name, s_force))
    return spy


def find_den(conn, group, ranker):
    """
    生成贼寇据点，可征讨
    :param ranker: 
    :param group: 
    :param conn: 
    :return: den
    """
    den = dict()
    den['d_group'] = group.get('g_id')
    den['d_name'] = random.choice(['山贼', '土匪', '强盗', '蛮夷', '流寇', '叛将'])
    den['d_corps'] = random.choice(Conn.get_level_ranker(conn, 6))
    den['d_ranker'] = random.randint(round(group.get('g_ranker')*0.3), round(group.get('g_ranker')*3.2))
    den['d_gold'] = random.randint(round(den.get('d_ranker')/10), round(den.get('d_ranker')/5))
    den['d_rations'] = random.randint(round(den.get('d_ranker')*1.5), round(den.get('d_ranker')*3.5))
    k = random.random()*random.random()
    den['d_gem'] = random.choice(Conn.find_treasure(conn)) if k > 0.8 else 0
    if group.get('g_status') == 1:
        print('发现{0}据点，拥有{1}共{2}人！请发兵镇压！'.format(den.get('d_name'),
                                                 ranker.get(den.get('d_corps')).get('r_name'),
                                                 den.get('d_ranker'))
              )
    Conn.insert_data(conn, 'den', den)


def patrol_group(conn, group, heroes, hero_id):
    """
    巡逻领地
    能提高势力民心
    有几率发现贼寇探子，成功击杀贼寇探子会获得更多民心
    有几率发现贼寇据点，需在征讨界面对据点进行摧毁，摧毁一定获得数量不等的粮草和黄金，有几率获得宝物
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :return: p_group [group, r_type]
    """
    k = random.random()
    h_force = 0
    name = ''
    new_group = dict()
    g_morale = group.get('g_morale')
    for h_id in hero_id:
        h_force += heroes.get(h_id).get('h_force')
        name += '{},'.format(heroes.get(h_id).get('h_name'))
    if k < 0.4:     # 无隐患
        r_type = 1
        morale = round(h_force/20)
        g_morale += morale
        print('巡逻完成，未发现隐患，{0}民心上升{1}点！'.format(group.get('g_name'), morale))
        group['g_morale'] = g_morale
        new_group['g_morale'] = g_morale
        con = 'g_id = {}'.format(group.get('g_id'))
        Conn.update_data(conn, 'hero_group', new_group, con)
    elif k < 0.8:   # 讨贼
        r_type = 2
    else:
        r_type = 3  # 据点
    p_group = [group, r_type]
    return p_group


def fight_enemy(conn, group, heroes, hero_id, spy):
    """
    讨贼
    :param conn: 
    :param group: 
    :param heroes: 
    :param hero_id: 
    :param spy: 
    :return: group
    """
    new_group = dict()
    que = queue.Queue()
    que.put(True)
    print('*'*20)
    print('{0:<4}\t{1:<10}\t{2:<4}'.format('ID', '姓名', '武力'))
    for h_id in hero_id:
        print('{0:<4}\t{1:<10}\t{2:<4}'.format(h_id, heroes.get(h_id).get('h_name'), heroes.get(h_id).get('h_force')))
    choice = input('请选择出战的英雄ID，可多选：\n').strip().split()
    h_num = len(choice)
    enemies = list(spy.keys())
    result = kumite(que, heroes, choice, spy, enemies)
    g_gold = group.get('g_gold')
    g_morale = group.get('g_morale')
    if result == 1:     # 讨贼胜利，获得民心、金钱、宝物
        morale = round(sum([spy.get(i).get('s_force') for i in list(spy.keys())])/10/h_num)
        gold = sum([spy.get(i).get('s_gold') for i in list(spy.keys())])
        print('讨贼胜利，获得民心{0}点，黄金{1}两！'.format(morale, gold))
        g_morale += morale
        g_gold += gold
        group['g_morale'] = g_morale
        new_group['g_morale'] = g_morale
        group['g_gold'] = g_gold
        new_group['g_gold'] = g_gold
    else:       # 讨贼失败，损失民心、金钱、宝物
        morale = round(sum([spy.get(i).get('s_force') for i in list(spy.keys())])/10/h_num)
        gold = random.randint(
            sum([spy.get(i).get('s_force') for i in list(spy.keys())])*5,
            sum([spy.get(i).get('s_force') for i in list(spy.keys())])*10
        )
        print('讨贼失败，损失民心{0}点，黄金{1}两！'.format(morale, gold if g_gold > gold else g_gold))
        g_morale -= morale
        g_gold -= gold if g_gold > gold else g_gold
        group['g_morale'] = g_morale
        new_group['g_morale'] = g_morale
        group['g_gold'] = g_gold
        new_group['g_gold'] = g_gold
    condition = 'g_id = {}'.format(group.get('g_id'))
    Conn.update_data(conn, 'hero_group', new_group, condition)
    return group


class Attack(threading.Thread):
    """
    讨贼算法，返回战斗结果
    """
    def __init__(self, que, h_hp, s_hp):
        threading.Thread.__init__(self)
        self.que = que  # 线程通信控制
        self.result = 0  # 战斗结果参数，1为英雄胜利，2为贼寇胜利
        self.h_hp = h_hp  # 参战英雄HP
        self.s_hp = s_hp  # 参战贼寇HP

    def h_attack(self, h_force, s_force):
        """
        英雄攻击贼寇
        :param h_force: 
        :param s_force: 
        :return: 
        """
        while self.que:
            h_att = random.randint(round(h_force * 0.6), round(h_force * 0.8))
            s_def = random.randint(round(s_force * 0.3), round(s_force * 0.5))
            h_speed = (h_force - (h_force - s_force)) * 0.02
            hurt = h_att - s_def if h_att - s_def > 0 else 1
            if h_force-s_force < 0:
                hurt = round(hurt*0.8)
            elif h_force-s_force in range(11):
                hurt = hurt
            elif h_force-s_force in range(21):
                hurt = round(hurt*1.5)
            elif h_force-s_force in range(31):
                hurt = hurt*2
            else:
                hurt * 3
            self.s_hp -= hurt
            print('*' * 20)
            print('英雄对贼将造成了{}点伤害，'.format(hurt))
            if self.s_hp < 0:
                self.s_hp = 0
                print('贼将被英雄击杀！'.format(self.s_hp))
                self.que = False
                self.result = 1
            print('贼将HP余{}点。'.format(self.s_hp))
            time.sleep(h_speed)

    def s_attack(self, h_force, s_force):
        """
        贼寇攻击英雄
        :param h_force: 
        :param s_force: 
        :return: 
        """
        while self.que:
            s_att = random.randint(round(s_force * 0.6), round(s_force * 0.8))
            h_def = random.randint(round(h_force * 0.3), round(h_force * 0.5))
            s_speed = (s_force - (s_force - h_force)) * 0.02
            hurt = s_att - h_def if s_att - h_def > 0 else 1
            if s_force-h_force < 0:
                hurt = round(hurt*0.8)
            elif s_force-h_force in range(11):
                hurt = hurt
            elif s_force-h_force in range(21):
                hurt = round(hurt*1.5)
            elif s_force-h_force in range(31):
                hurt = hurt*2
            else:
                hurt * 3
            self.h_hp -= hurt
            print('*' * 20)
            print('贼将对英雄造成了{}点伤害，'.format(hurt))
            if self.h_hp < 0:
                self.h_hp = 0
                print('英雄被贼将击败！'.format(self.h_hp))
                self.que = False
                self.result = 2
            print('英雄HP余{}点。'.format(self.h_hp))
            time.sleep(s_speed)

    def attack(self, h_force, s_force):
        """
        线程控制战斗，依据不同的武力值拥有不同的出招速度
        :param h_force: 
        :param s_force: 
        :return: [战斗结果， 英雄剩余血量， 贼寇剩余血量]
        """
        t1 = threading.Thread(target=Attack.h_attack, args=(self, h_force, s_force))
        t2 = threading.Thread(target=Attack.s_attack, args=(self, h_force, s_force))
        threads = [t1, t2]
        threads[0].setDaemon(True)
        threads[1].setDaemon(True)
        threads[0].start()
        threads[1].start()
        threads[0].join()
        threads[1].join()
        if self.result == 1:
            return [self.result, h_force, self.h_hp]
        else:
            return [self.result, s_force, self.s_hp]


def kumite(que, heroes, choice, spy, enemies):
    if len(enemies) > 0:
        s_force = spy.get(enemies.pop()).get('s_force')
    else:
        return 1    # 无贼寇，讨贼胜利
    if len(choice) > 0:
        k = int(choice.pop())
        print('*'*50)
        print('{}开始迎战！'.format(heroes.get(k).get('h_name')))
        h_force = heroes.get(k).get('h_force')
    else:
        return 2    # 无英雄迎战，讨贼失败
    h_hp = h_force * 10
    s_hp = s_force * 10
    result = Attack(que, h_hp, s_hp).attack(h_force, s_force)
    while True:
        # result [
        #   战斗结果：1为英雄胜利，2为贼寇胜利，
        #   胜者武力
        #   胜者剩余血量
        # ]     继续下一次战斗
        if result[0] == 1:
            h_force = result[1]
            h_hp = result[2]
            if len(enemies) > 0:
                print('*'*50)
                print('{}获得胜利，继续迎战！'.format(heroes.get(k).get('h_name')))
                s_force = spy.get(enemies.pop()).get('s_force')
                s_hp = s_force * 10
                result = Attack(que, h_hp, s_hp).attack(h_force, s_force)
            else:
                print('*'*50)
                print('成功剿灭所有贼寇，讨贼胜利！')
                return 1    # 代表贼寇被全灭，讨贼胜利
        else:
            s_force = result[1]
            s_hp = result[2]
            if len(choice) > 0:
                print('*'*50)
                print('{}被击败,'.format(heroes.get(k).get('h_name')))
                k = int(choice.pop())
                print('{}开始迎战！'.format(heroes.get(k).get('h_name')))
                h_force = heroes.get(k).get('h_force')
                h_hp = h_force * 10
                result = Attack(que, h_hp, s_hp).attack(h_force, s_force)
            else:
                print('*'*50)
                print('全将败退，贼寇成功逃窜！')
                return 2    # 代表英雄全败，讨贼失败
