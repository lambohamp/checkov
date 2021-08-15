# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


# class resourceTagsCheck(BaseResourceCheck):
#     def __init__(self):
#         name = "Ensure resources have correct tags"
#         id = "CUSTOM_AZURE_1"
#         supported_resources = ['*']
#         categories = [CheckCategories.GENERAL_SECURITY]
#         super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

#     def scan_resource_conf(self, conf):
#         if conf.get("tags",[]):
#             env = conf["tags"][0].get("Environment",{})
#             if env in ["dev","prod","qa"]:
#                 return CheckResult.PASSED
#         return CheckResult.FAILED


# check = resourceTagsCheck()
