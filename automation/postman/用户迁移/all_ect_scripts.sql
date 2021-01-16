SET SERVEROUTPUT ON
SET TIMING ON
SET SCAN OFF
SET DEFINE OFF
set sqlblanklines on

-- Cutover
SPOOL new_11_company.log

@ECT/scripts/inital_file_system.sql
@ECT/scripts/sales_domain_id_supplement.sql
@ECT/scripts/user_phone_mail.sql

@ECT/scripts/company.sql
@ECT/scripts/company_account.sql
@ECT/scripts/company_primary_user.sql
@ECT/scripts/company_sales.sql
@ECT/scripts/company_sales_update_domainid.sql


@ECT/scripts/company_level.sql
@ECT/scripts/company_saling_level.sql


@ECT/scripts/user_company_aso.sql
@ECT/scripts/user_promission.sql

@ECT/scripts/company_user_info_update.sql
@ECT/scripts/revoke_missing_file_set_up.sql
@ECT/scripts/cmn_free_dnd_party_cfg.sql



show errors;
SPOOL OFF

SET TIMING OFF
EXIT


