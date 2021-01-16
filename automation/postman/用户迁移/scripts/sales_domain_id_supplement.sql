INSERT INTO SALES_REP_CONFIG
  (SALES_CDE, EMAIL_ID, FIRST_NME, LAST_NME, SALES_OFCE)
  SELECT DISTINCT SALES_CDE, EMAIL_ID, FIRST_NME, LAST_NME, SALES_OFCE
    FROM CPF_SALES_REP
   WHERE SALES_CDE IN
         ('A92', 'X55', 'VP7', 'A91', 'AK4', 'YX9', 'V73', 'WV1', 'W09',
          'FO3', 'VW2', 'FO4', 'IT2', 'HZ7', 'YL8', 'EA4', 'EC6', 'V43',
          'V67', 'X51', 'V75', 'V01', 'FA9', 'ET6', 'AL3');
COMMIT;