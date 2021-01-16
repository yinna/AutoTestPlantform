# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\China\T03Company\T02clientPrimaryUserPassSubuser.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.China.T01setUp.T01cnClientLogin_test import (
    TestCaseT01Cnclientlogin as T01Cnclientlogin,
)


class TestCaseT02Clientprimaryuserpasssubuser(HttpRunner):

    config = (
        Config("request methods testcase with functions")
        .variables(
            **{
                "companyId": "${getCompanyId(中国测试企业)}",
                "subUserId": "${getUserId(cn_subuser)}",
            }
        )
        .base_url("http://mall.ectpp.opsmart.cn")
        .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("login")
            .call(T01Cnclientlogin)
            .export(*["cnPrimaryUserToken", "cnSubUserToken"])
        ),
        Step(
            RunRequest("submit associate to exist company application")
            .post("/api/admin/company/apply-for-company-affiliate")
            .with_headers(
                **{
                    "X-Auth-Token": "$cnSubUserToken",
                    "Content-Type": "application/json;charset=UTF-8",
                }
            )
            .with_json(
                {
                    "name": "cn_subuser",
                    "companyNo": "20201202001",
                    "companyID": "$companyId",
                    "companyNameZh": "中国测试企业",
                    "companyNameEn": "chinaTestCompany",
                    "countryCode": "CN",
                }
            )
            .teardown_hook("${sleepTime(2)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("primary user search subuser associate task id")
            .get("/api/workflow/company/task/pending")
            .with_headers(
                **{
                    "X-Auth-Token": "$cnPrimaryUserToken",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .extract()
            .with_jmespath("body[0].taskId", "userTaskId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].businessKey", "$subUserId")
        ),
        Step(
            RunRequest("primary user reject subuser associate")
            .post("/api/workflow/company/task/reject")
            .with_headers(
                **{
                    "X-Auth-Token": "$cnPrimaryUserToken",
                    "Content-Type": "application/json;charset=UTF-8",
                }
            )
            .with_json(["$userTaskId"])
            .teardown_hook("${sleepTime(2)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseT02Clientprimaryuserpasssubuser().test_start()
