
insert into company_sales(id, sales_region,sales_code, company_id) select  '7fa01f997b25430492d7c44a7d9be02f', 'SHA', 'V30' , id  from company where sapid ='1188968000';
insert into company_sales(id, sales_region,sales_code, company_id) select  '3514b86d61a941d2be7751e541161cab', '', 'X18' , id  from company where sapid ='1226015000';
insert into company_sales(id, sales_region,sales_code, company_id) select  '7b84be3e92e243deb8d9c9da18f566f4', 'SHA', 'V30' , id  from company where sapid ='6382131000';

--extra 1
insert into company_sales(id, sales_region,sales_code, company_id) select  '85d9df8d3ec7444a996f7b5f85c8ff45', 'NGB', 'V52' , id  from company where sapid ='6382131000';
insert into company_sales(id, sales_region,sales_code, company_id) select  'aed0e80711024688b974d46c7444c107', '', 'W11' , id  from company where sapid ='6419407000';
insert into company_sales(id, sales_region,sales_code, company_id) select  'c5b768c9864741138e8a0fc1160879f1', '', 'FP3' , id  from company where sapid ='6600006000';
insert into company_sales(id, sales_region,sales_code, company_id) select  '4d6457773fd04d37a7af7dec2cafbc69', '', 'YQ8' , id  from company where sapid ='7012015000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'a268d6a771e646e58ba4d22cb697df7e', 'SHA', 'V30' , id  from company where sapid ='7098968000';
insert into company_sales(id, sales_region,sales_code, company_id) select  'f906952c6c75475e9d4cacda5d594c7a', '', 'T09' , id  from company where sapid ='7098968000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'fb7defead47148b8942d181f60d07ef2', 'TSN', 'S08' , id  from company where sapid ='7165101000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'b8f1f0f836a34bc88a5e6a00be92ceab', 'TAO', 'U15' , id  from company where sapid ='7516491000';
--missing 2 sales
insert into company_sales(id, sales_region,sales_code, company_id) select  '7765fad1893548ae8bbbe55980bd2ae5', '', 'D06' , id  from company where sapid ='8178189000';

insert into company_sales(id, sales_region,sales_code, company_id) select  '35a5b11ebc534d68bd4557141633ff93', 'TSN', 'TO7' , id  from company where sapid ='7763214000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'e1ae296eb3a64340bf79c020d79d7a82', 'HUA', 'X14' , id  from company where sapid ='7569987000';

insert into company_sales(id, sales_region,sales_code, company_id) select  '66cbc7d4242d4e018c8ef5c92472fe25', '', 'V32' , id  from company where sapid ='7569987000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'e240f79c5a7c4a5d9604b88a8019b8c9', 'NGB', 'VA9' , id  from company where sapid ='7280482000';

insert into company_sales(id, sales_region,sales_code, company_id) select  '2f97742d898d439ea1ed07ac8d094543', 'SHA', 'V16' , id  from company where sapid ='1087171000';

insert into company_sales(id, sales_region,sales_code, company_id) select  'cadb97d8b7574867a037ae535fc771a6', '', 'AO6' , id  from company where sapid ='6223489000';


COMMIT;