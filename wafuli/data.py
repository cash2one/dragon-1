#coding:utf-8
'''
Created on 20160325

@author: lch
'''
PERIOD_NUM = (
    ('1', u'第一期'),
    ('2', u'第二期'),
    ('3', u'第三期'),
    ('4', u'第四期'),
    ('5', u'第五期'),
    ('6', u'第六期'),
    ('7', u'第七期'),
    ('8', u'第八期'),
    ('9', u'第九期'),
)


STATE = (
    ('0', u'即将开始'),
    ('1', u'正在进行'),
    ('2', u'已结束'),
    ('3', u'已删除'),
)
FILTER = (    
    ('1', u'上市系'),
    ('2', u'国资系'),
    ('3', u'民营系'),
    ('4', u'其他'),
)

FINANCE_TYPE = (    
    ('1', u'新手投资'),
    ('2', u'稳健投资'),
    ('3', u'稳健投资'),
)

CATEGORY = (
    ('1', u'数码产品'),
    ('2', u'游戏相关'),
    ('3', u'虚拟充值'),
    ('4', u'居家生活'),
)
ITEM = (
    ('1', u'手机'),
    ('2', u'电脑'),
    ('3', u'外设'),
    ('4', u'周边'),
    ('5', u'话费'),
    ('6', u'Q币'),
    ('7', u'骏网卡'),
    ('8', u'书籍'),
    ('9', u'厨房用品'),
    ('10', u'生活用品'),
)

AUDIT_STATE = (
    ('0', u'审核通过'),
    ('1', u'待审核'),
    ('2', u'审核未通过'),
    ('3', u'其他'),
)

TRANS_TYPE = (
    ('0', u'增加'),
    ('1', u'减少'),
    ('2', u'其他'),
)
ZERO_TYPE = (
    ('1', u'购物'),
    ('2', u'体验金'),
    ('3', u'流量'),
    ('4', u'话费'),
    ('5', u'其他'),
)
WELFARE_TYPE = (
    ('hongbao', u'红包'),
    ('baoyou', u'9.9包邮'),
    ('youhuiquan', u'优惠券'),
    ('qita', u'其他'),
)
TASK_TYPE = (
    ('junior', u'新手入门'),
    ('middle', u'进阶体验'),
    ('senior', u'高手专区'),
    ('qita', u'其他'),
)
NEWS_TYPE = (
    ('1', u'公告'),
    ('2', u'福利攻略'),
    ('3', u'新闻'),
    ('4', u'横幅广告'),
    ('5', u'兑奖帮助'),
)
ADLOCATION = (
    ('0', u'全部'),
    ('1', u'首页'),
    ('2', u'免费福利'),
    ('3', u'体验福利'),
    ('4', u'理财福利'),
    ('5', u'积分商城'),
    ('6', u'关于我们'),
    ('7', u'默认内容页'),
    ('8', u'福利推荐活动'),
    ('9', u'积分抽奖活动'),
    ('10', u'资讯列表页'),
)
MADLOCATION = (
    ('1', u'今日推荐1'),
    ('2', u'今日推荐2'),
    ('3', u'今日推荐3'),
)
USER_EVENT_TYPE = (
    ('1', u'福利审核'),
    ('2', u'提现审核'),
    ('3', u'商品兑换审核'),
    ('4', u'优惠券兑换审核'),
    ('5', u'邀请奖励转余额'),
    ('6', u'福利推荐审核'),
    ('7', u'积分抽奖'),
)
ADMIN_EVENT_TYPE = (
    ('1', u'返现审核'),
    ('2', u'提现审核'),
    ('3', u'优惠券审核'),
    ('4', u'更改现金余额'),
    ('5', u'更改积分余额'),
    ('6', u'更改用户状态'),
    ('7', u'发放优惠券'),
    ('8', u'积分兑换审核'),
    ('9', u'福利推荐审核'),
    ('10', u'其他'),
)
COUPON_TYPE = (
    ('0', u'现金券'),
    ('1', u'加息券'),
    ('2', u'使用券'),
)
AwardTable = {
    1:'Nothing',
    2:u'10积分',
    3:u'50积分',
    4:u'0.8元现金',
    5:u'2元现金',
    6:'iphone',
}
INFORMATION_TYPE = (
    ('wahangqing', u'挖行情'),
    ('wagushi', u'挖故事'),
    ('washuju', u'挖数据'),
    ('wahuodong', u'挖活动'),
)
