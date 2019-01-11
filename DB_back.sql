/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.3-rc-log : Database - hero_era
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hero_era` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `hero_era`;

/*Table structure for table `den` */

DROP TABLE IF EXISTS `den`;

CREATE TABLE `den` (
  `d_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '据点ID',
  `d_group` int(10) DEFAULT NULL COMMENT '所属势力ID',
  `d_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '据点名称',
  `d_corps` int(10) NOT NULL COMMENT '据点兵种',
  `d_ranker` int(100) NOT NULL COMMENT '据点兵力',
  `d_gold` int(100) NOT NULL COMMENT '据点黄金',
  `d_rations` int(100) NOT NULL COMMENT '据点粮草',
  `d_gem` int(10) NOT NULL COMMENT '据点宝物',
  PRIMARY KEY (`d_id`),
  KEY `d_group` (`d_group`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `den` */

insert  into `den`(`d_id`,`d_group`,`d_name`,`d_corps`,`d_ranker`,`d_gold`,`d_rations`,`d_gem`) values (1,1,'山贼',33,1098,54,1079,0);
insert  into `den`(`d_id`,`d_group`,`d_name`,`d_corps`,`d_ranker`,`d_gold`,`d_rations`,`d_gem`) values (2,1,'流寇',33,2415,88,2218,0);
insert  into `den`(`d_id`,`d_group`,`d_name`,`d_corps`,`d_ranker`,`d_gold`,`d_rations`,`d_gem`) values (3,1,'叛将',32,1624,223,6824,0);
insert  into `den`(`d_id`,`d_group`,`d_name`,`d_corps`,`d_ranker`,`d_gold`,`d_rations`,`d_gem`) values (4,1,'强盗',31,5294,600,16272,0);

/*Table structure for table `dens` */

DROP TABLE IF EXISTS `dens`;

CREATE TABLE `dens` (
  `d_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '据点ID',
  `d_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '据点名称',
  `d_corps` int(10) DEFAULT NULL COMMENT '据点兵种',
  `d_ranker` int(10) DEFAULT NULL COMMENT '据点兵力',
  `d_gold` int(10) DEFAULT NULL COMMENT '据点黄金',
  `d_rations` int(10) DEFAULT NULL COMMENT '据点粮草',
  `d_gem` int(10) DEFAULT NULL COMMENT '据点宝物',
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `dens` */

/*Table structure for table `gems` */

DROP TABLE IF EXISTS `gems`;

CREATE TABLE `gems` (
  `t_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '宝物ID',
  `t_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '宝物名称',
  `t_lead` int(10) DEFAULT '0' COMMENT '对英雄统率增益',
  `t_force` int(10) DEFAULT '0' COMMENT '对英雄武力增益',
  `t_brain` int(10) DEFAULT '0' COMMENT '对英雄智力增益',
  `t_politics` int(10) DEFAULT '0' COMMENT '对英雄政治增益',
  `t_charm` int(10) DEFAULT '0' COMMENT '对英雄魅力增益',
  `t_group` int(10) DEFAULT '0' COMMENT '所属势力ID',
  `t_hero` int(10) DEFAULT '0' COMMENT '所属英雄ID',
  `t_level` int(10) DEFAULT NULL COMMENT '宝物等阶',
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `gems` */

insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (1,'白马',0,0,0,0,1,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (2,'乌丸马',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (3,'匈奴马',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (4,'大宛马',0,1,0,0,1,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (5,'凉州马',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (6,'绝影',0,3,0,0,4,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (7,'的卢',0,2,0,0,2,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (8,'爪黄飞电',0,3,0,0,3,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (9,'飞镰',0,2,0,0,1,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (10,'追风白凰',0,5,0,0,7,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (11,'赤兔',0,6,0,0,8,1,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (12,'汗血马',0,1,0,0,2,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (13,'沙里飞',0,3,0,0,3,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (14,'惊帆',0,2,0,0,2,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (15,'檀弓',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (16,'白桦弓',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (17,'破邪弓',0,3,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (18,'穿云弓',0,3,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (19,'神臂弓',0,4,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (20,'迅雷弓',0,5,0,0,1,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (21,'神鸢弓',0,5,0,0,2,1,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (22,'万里起云烟',0,7,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (23,'短锥枪',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (24,'点钢矛',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (25,'红缨枪',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (26,'九曲戟',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (27,'雁翎枪',0,3,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (28,'梨花枪',0,3,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (29,'白玉戟',0,5,0,0,2,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (30,'蛇矛',0,4,0,0,1,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (31,'紫龙戟',0,5,0,0,3,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (32,'青天钩镰枪',0,6,0,0,4,1,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (33,'万胜丈八矛',0,7,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (34,'神鬼方天戟',0,9,0,0,6,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (35,'铜长刀',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (36,'钩镰刀',0,3,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (37,'凤绫锤',0,5,0,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (38,'偃月刀',0,4,0,0,1,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (39,'云月刀',0,6,0,0,2,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (40,'天罡斧',0,7,0,0,2,1,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (41,'青龙偃月刀',0,9,0,0,4,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (42,'翔龙偃月刀',0,11,0,0,6,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (43,'白羽扇',0,0,0,0,2,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (44,'青玉扇',0,0,0,0,4,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (45,'鹤羽扇',0,0,0,0,5,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (46,'天罡劈水扇',0,3,0,0,7,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (47,'驭风剑翎扇',0,4,0,0,6,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (48,'真火朱雀扇',0,5,0,0,9,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (49,'长剑',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (50,'朴刀',0,1,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (51,'青铜剑',0,2,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (52,'宽刃剑',0,3,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (53,'弧月刀',0,3,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (54,'连环刀',0,4,0,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (55,'龙渊剑',0,6,0,0,3,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (56,'双股剑',0,5,0,0,2,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (57,'古锭刀',0,6,0,0,2,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (58,'青冥',0,7,0,0,4,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (59,'紫电',0,7,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (60,'白虹',0,7,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (61,'青釭',0,8,0,0,6,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (62,'七星刀',0,6,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (63,'倚天剑',0,8,0,0,6,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (64,'巨阙',0,9,0,0,7,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (65,'冰凤炎凰',0,10,0,0,7,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (66,'孙子兵法',10,0,8,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (67,'六韬',8,0,6,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (68,'三略',8,0,7,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (69,'司马法',6,0,5,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (70,'吴子',6,0,4,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (71,'孙膑兵法',5,0,4,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (72,'尉缭子',4,0,5,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (73,'孟德新书',3,0,3,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (74,'墨子',3,0,5,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (75,'韩非子',0,0,7,10,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (76,'管子',0,0,5,8,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (77,'商君书',0,0,4,6,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (78,'晏子春秋',0,0,2,2,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (79,'周书阴符',0,0,1,2,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (80,'四月民令',0,0,0,2,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (81,'左氏春秋',0,0,5,5,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (82,'战国策',0,0,3,4,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (83,'吴越春秋',0,0,2,3,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (84,'吴记',0,0,3,2,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (85,'汉书',0,0,2,3,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (86,'淮南子',0,0,2,1,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (87,'老子',0,0,10,3,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (88,'易经',0,0,6,2,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (89,'庄子',0,0,7,3,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (90,'论语',0,0,9,6,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (91,'诗经',0,0,6,2,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (92,'书经',0,0,4,2,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (93,'礼记',0,0,4,3,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (94,'孝经',0,0,2,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (95,'青囊书',0,0,4,0,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (96,'遁甲天书',0,0,8,0,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (97,'太平要术',0,0,9,7,0,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (98,'山海经',0,0,3,0,0,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (99,'浮屠经',0,0,4,3,0,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (100,'罗绮香囊',0,0,0,0,5,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (101,'白玉环',0,0,0,0,3,0,0,2);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (102,'珍珠',0,0,0,0,2,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (103,'玛瑙',0,0,0,0,2,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (104,'翡翠',0,0,0,0,2,0,0,1);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (105,'四灵文镜',0,0,0,0,7,0,0,3);
insert  into `gems`(`t_id`,`t_name`,`t_lead`,`t_force`,`t_brain`,`t_politics`,`t_charm`,`t_group`,`t_hero`,`t_level`) values (106,'貂裘',0,0,0,0,6,0,0,3);

/*Table structure for table `hero_group` */

DROP TABLE IF EXISTS `hero_group`;

CREATE TABLE `hero_group` (
  `g_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '势力ID',
  `g_lord` int(10) DEFAULT NULL COMMENT '势力主公ID',
  `g_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '势力名',
  `g_economy` int(10) NOT NULL DEFAULT '50' COMMENT '势力经济',
  `g_farming` int(10) NOT NULL DEFAULT '50' COMMENT '势力农业',
  `g_military` int(10) NOT NULL DEFAULT '50' COMMENT '势力军事',
  `g_science` int(10) NOT NULL DEFAULT '50' COMMENT '势力科技',
  `g_morale` int(10) NOT NULL DEFAULT '50' COMMENT '势力民心',
  `g_gold` int(100) NOT NULL DEFAULT '2000' COMMENT '势力黄金',
  `g_rations` int(100) NOT NULL DEFAULT '10000' COMMENT '势力粮草',
  `g_corps` int(10) NOT NULL DEFAULT '1' COMMENT '势力兵种',
  `g_experience` int(10) NOT NULL DEFAULT '10' COMMENT '势力兵种经验',
  `g_ranker` int(100) NOT NULL DEFAULT '1000' COMMENT '势力兵力',
  `g_populace` int(100) NOT NULL DEFAULT '50000' COMMENT '势力人口',
  `g_status` int(10) NOT NULL DEFAULT '0' COMMENT '势力状态',
  PRIMARY KEY (`g_id`),
  KEY `g_lord` (`g_lord`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `hero_group` */

insert  into `hero_group`(`g_id`,`g_lord`,`g_name`,`g_economy`,`g_farming`,`g_military`,`g_science`,`g_morale`,`g_gold`,`g_rations`,`g_corps`,`g_experience`,`g_ranker`,`g_populace`,`g_status`) values (1,4,'乐俊军',145,102,53,56,140,54048,78668,3,12,2000,60737,1);
insert  into `hero_group`(`g_id`,`g_lord`,`g_name`,`g_economy`,`g_farming`,`g_military`,`g_science`,`g_morale`,`g_gold`,`g_rations`,`g_corps`,`g_experience`,`g_ranker`,`g_populace`,`g_status`) values (2,35,'喻唯军',113,113,91,152,153,17738,17209,1,10,4717,53741,0);
insert  into `hero_group`(`g_id`,`g_lord`,`g_name`,`g_economy`,`g_farming`,`g_military`,`g_science`,`g_morale`,`g_gold`,`g_rations`,`g_corps`,`g_experience`,`g_ranker`,`g_populace`,`g_status`) values (3,27,'余岩军',99,110,96,92,44,16583,22486,1,10,5379,53437,0);
insert  into `hero_group`(`g_id`,`g_lord`,`g_name`,`g_economy`,`g_farming`,`g_military`,`g_science`,`g_morale`,`g_gold`,`g_rations`,`g_corps`,`g_experience`,`g_ranker`,`g_populace`,`g_status`) values (4,42,'蔺沐军',101,66,74,114,74,27637,40818,1,10,3133,56380,0);
insert  into `hero_group`(`g_id`,`g_lord`,`g_name`,`g_economy`,`g_farming`,`g_military`,`g_science`,`g_morale`,`g_gold`,`g_rations`,`g_corps`,`g_experience`,`g_ranker`,`g_populace`,`g_status`) values (5,28,'岑戈军',121,103,92,135,139,26327,33962,1,10,3716,56365,0);

/*Table structure for table `heroes` */

DROP TABLE IF EXISTS `heroes`;

CREATE TABLE `heroes` (
  `h_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '英雄ID',
  `h_group` int(10) DEFAULT '0' COMMENT '所属势力ID',
  `h_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄姓名',
  `h_gender` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄性别',
  `h_age` int(10) DEFAULT NULL COMMENT '英雄年龄',
  `h_identity` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '英雄身份',
  `h_lead` int(10) DEFAULT NULL COMMENT '英雄统率',
  `h_force` int(10) DEFAULT NULL COMMENT '英雄武力',
  `h_brain` int(10) DEFAULT NULL COMMENT '英雄智力',
  `h_politics` int(10) DEFAULT NULL COMMENT '英雄政治',
  `h_charm` int(10) DEFAULT NULL COMMENT '英雄魅力',
  `h_status` int(10) DEFAULT '1' COMMENT '英雄状态',
  PRIMARY KEY (`h_id`),
  KEY `h_group` (`h_group`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `heroes` */

insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (1,5,'蓝卓','女',50,'宰辅',50,50,91,94,63,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (2,5,'毋芳','女',55,'统帅',81,55,83,73,51,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (3,2,'宦西','女',41,'宰辅',56,54,71,86,70,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (4,1,'乐俊','男',50,'统帅',91,74,75,58,85,3);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (5,1,'呼延策','男',38,'军师',95,89,92,51,95,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (6,1,'谈绯','女',53,'军师',71,56,96,88,81,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (7,0,'暨叶','女',36,'军师',60,77,82,58,71,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (8,0,'鲁夕','女',25,'武将',65,95,62,89,90,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (9,0,'虞异','男',55,'统帅',85,95,61,53,79,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (10,0,'顾维','男',23,'统帅',84,56,82,72,61,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (11,3,'酆双','女',55,'统帅',91,93,61,50,75,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (12,5,'殳杏','女',46,'统帅',92,68,57,67,54,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (13,0,'酆顾','女',52,'武将',64,93,60,51,60,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (14,4,'广瑶','女',46,'军师',59,53,83,75,69,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (15,0,'暨念','女',51,'统帅',92,67,63,90,95,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (16,0,'哈营','男',30,'统帅',96,58,79,60,89,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (17,1,'庞海','男',38,'军师',80,80,92,89,91,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (18,4,'续潮','男',18,'统帅',96,80,94,57,73,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (19,5,'田琨','男',45,'武将',88,87,88,75,80,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (20,3,'宫畅','男',17,'武将',59,98,91,76,59,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (21,0,'荣戈','女',43,'武将',57,89,67,56,62,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (22,5,'山燕','女',57,'宰辅',91,74,75,84,80,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (23,5,'鱼庚','男',54,'军师',91,63,89,84,79,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (24,2,'葛洪','男',22,'武将',91,81,55,51,57,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (25,2,'柴扬','女',42,'统帅',90,68,90,55,99,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (26,1,'赵慕','女',30,'武将',78,87,65,72,69,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (27,3,'余岩','男',57,'武将',76,102,66,76,87,3);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (28,5,'岑戈','女',38,'军师',64,76,88,99,78,3);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (29,5,'余丽','女',21,'统帅',84,81,57,77,76,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (30,2,'缪珊','女',43,'军师',81,85,91,84,95,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (31,2,'穆婷','女',47,'统帅',84,69,57,84,91,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (32,2,'桑攀','男',58,'武将',94,88,70,80,87,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (33,0,'温玥','男',41,'统帅',84,57,58,71,86,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (34,0,'阙辰','男',19,'统帅',98,85,75,81,73,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (35,2,'喻唯','女',36,'军师',71,64,98,76,91,3);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (36,0,'邴刚','男',44,'武将',87,91,57,83,57,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (37,1,'齐冀','女',22,'宰辅',85,78,85,91,95,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (38,0,'谭晓','女',57,'武将',57,94,63,91,70,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (39,2,'祖柏','男',47,'统帅',87,56,64,51,68,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (40,0,'计游','女',53,'宰辅',92,75,66,85,87,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (41,1,'费治','男',34,'武将',63,85,90,93,79,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (42,4,'蔺沐','女',45,'武将',98,85,68,59,88,3);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (43,4,'宗杰','男',54,'军师',86,62,96,93,97,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (44,1,'穆忱','男',18,'武将',58,93,91,61,57,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (45,0,'连昔','女',31,'武将',94,95,58,50,65,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (46,0,'严鲲','男',17,'武将',63,80,57,88,85,1);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (47,3,'时笙','女',31,'宰辅',76,85,72,99,67,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (48,3,'颜芳','女',30,'武将',80,92,55,71,89,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (49,1,'裘陶','男',44,'军师',91,74,87,74,90,2);
insert  into `heroes`(`h_id`,`h_group`,`h_name`,`h_gender`,`h_age`,`h_identity`,`h_lead`,`h_force`,`h_brain`,`h_politics`,`h_charm`,`h_status`) values (50,1,'蔚峰','男',54,'宰辅',80,65,58,95,58,2);

/*Table structure for table `ranker` */

DROP TABLE IF EXISTS `ranker`;

CREATE TABLE `ranker` (
  `r_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '兵种ID',
  `r_name` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '兵种名称',
  `r_force` int(10) DEFAULT NULL COMMENT '兵种武力',
  `r_defense` int(10) DEFAULT NULL COMMENT '兵种防御',
  `r_level` int(10) DEFAULT NULL COMMENT '兵种等阶',
  PRIMARY KEY (`r_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `ranker` */

insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (1,'轻步兵',3,2,1);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (2,'短枪兵',4,2,1);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (3,'刀盾兵',3,4,1);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (4,'短弓兵',4,1,1);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (5,'重步兵',5,4,2);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (6,'长弓兵',6,3,2);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (7,'轻骑兵',8,5,2);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (8,'长枪兵',6,4,2);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (9,'大刀兵',8,5,3);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (10,'重甲骑',11,10,3);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (11,'连弩兵',9,7,3);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (12,'铁甲兵',9,12,3);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (13,'精武士',15,11,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (14,'虎贲军',13,12,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (15,'羽林士',14,13,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (16,'龙骧骑',16,14,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (17,'玄甲兵',16,18,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (18,'白马义从',18,15,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (19,'先登死士',17,13,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (20,'虎豹骑',16,15,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (21,'陷阵营',18,18,4);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (22,'精武卫',20,20,5);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (23,'羽林卫',22,18,5);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (24,'龙骧卫',27,25,5);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (25,'神机卫',29,18,5);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (26,'玄甲卫',24,26,5);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (27,'喽啰',2,1,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (28,'喽啰精英',3,2,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (29,'巡山',3,3,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (30,'巡山精英',4,5,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (31,'先锋',6,5,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (32,'先锋精英',8,6,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (33,'逃兵',10,8,6);
insert  into `ranker`(`r_id`,`r_name`,`r_force`,`r_defense`,`r_level`) values (34,'逃兵精英',14,11,6);

/*Table structure for table `years` */

DROP TABLE IF EXISTS `years`;

CREATE TABLE `years` (
  `year` int(10) NOT NULL DEFAULT '184' COMMENT '年份',
  `month` int(10) NOT NULL DEFAULT '1' COMMENT '月份'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `years` */

insert  into `years`(`year`,`month`) values (185,12);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
