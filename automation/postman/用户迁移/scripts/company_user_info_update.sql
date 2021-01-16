
--Phone Info
update company set Phone='021-51028225' where sapid='1133320000';
update company set Phone='0592-2385101' where sapid='6713816000';
update company set Phone='0571-56927840' where sapid='7411892000';
update company set Phone='0574-27906333' where sapid='6538206000';
update company set Phone='0573-87807885' where sapid='7081974000';
update company set Phone='0532-85830077' where sapid='6855145000';
update company set Phone='021-60529418' where sapid='7279576000';


--name_en
update company set name_en='Lianyungang Zhanhang International Transport Company Limited' where sapid='7280405000';
update company set name_en='Huanji Supply Chain Management Company Limited ' where sapid='6388860000';
update company set name_en='Worldwide Logistics Company Limited Ningbo Branch' where sapid='6538206000';
update company set name_en='Hebei Yongtuo International Company Limited' where sapid='8016197000';
update company set name_en='Shenzhen Well Link Supply Chain Limited' where sapid='7347389000';
COMMIT;


update user2 set phone='13869862682', email='johnsen@dawuchain.com' where username=lower('shenzhen_dawu');
update user2 set phone='15900691702', email='cherry@yuexinlogistics.com' where username=lower('上海巴士悦信物流发展有限公司');
update user2 set phone='15842463500', email='1095367270@qq.com' where username=lower('先达国际货运（上海）有限公司大连分公司');
update user2 set phone='13585223501', email='QIANG@WKH99.COM' where username=lower('南通万凯华国际货运代理有限公司');
update user2 set phone='13950189266', email='jason@srilogistics.com' where username=lower('厦门立道物流');
update user2 set phone='13758372968', email='247379964@qq.com' where username=lower('嘉兴市捷诚物流');
update user2 set phone='18604118877', email='liujun@isewandl.com' where username=lower('大连欣万通国际物流有限公司');
update user2 set phone='18952730011', email='1254096542@qq.com' where username=lower('扬州集运物流');
update user2 set phone='13328067610', email='545562729@qq.com' where username=lower('江苏中基国际');
update user2 set phone='13247395221', email='shenzhen@bushjet.com' where username=lower('深圳市宝行健国际');
update user2 set phone='13842689534', email='karen.liu@jhj.com.cn' where username=lower('锦海捷亚国际货运大连');


COMMIT;

update company_primary_user set  phone='13842689534', email='karen.liu@jhj.com.cn' where user_id='8aaa34476b91fdf0016b9298dafa02f9';
update company_primary_user set  phone='18952730011', email='1254096542@qq.com' where user_id='8aaa34476b91fdf0016b9298b3e202a3';
update company_primary_user set  phone='13328067610', email='545562729@qq.com' where user_id='8aaa34476b91fdf0016b9298ba3902b0';
update company_primary_user set  phone='13585223501', email='QIANG@WKH99.COM' where user_id='8aaa34476b91fdf0016b929897000263';
update company_primary_user set  phone='13869862682', email='johnsen@dawuchain.com' where user_id='8aaa34476b91fdf0016b92982768017c';
update company_primary_user set  phone='13247395221', email='shenzhen@bushjet.com' where user_id='8aaa34476b91fdf0016b9298c96402d1';
update company_primary_user set  phone='13758372968', email='247379964@qq.com' where user_id='8aaa34476b91fdf0016b92989f140275';
update company_primary_user set  phone='13950189266', email='jason@srilogistics.com' where user_id='8aaa34476b91fdf0016b92989ab1026b';
update company_primary_user set  phone='15842463500', email='1095367270@qq.com' where user_id='8aaa34476b91fdf0016b9298910c025b';
update company_primary_user set  phone='18604118877', email='liujun@isewandl.com' where user_id='8aaa34476b91fdf0016b9298a153027a';
update company_primary_user set  phone='15900691702', email='cherry@yuexinlogistics.com' where user_id='8aaa34476b91fdf0016b929883cd023f';
COMMIT;


update company_primary_user set id_number='220822198210050081' where company_id='42f33136c66a44348bd18450fb07736a';

update company_primary_user set id_number='320723198702283919' where company_id='5e290e2b16564a3fb130f7e72a89af29';
update company_primary_user set id_number='331022198505081670' where company_id='b63d2a980e4f4f9f986ee16571eacf15';
update company_primary_user set id_number='120101197012212520' where company_id='104ace161e4648e6bb96b11a1654ceb5';
update company_primary_user set id_number='440306198108121326' where company_id='77d7138480ce41059f192f34aed64d57';
COMMIT;