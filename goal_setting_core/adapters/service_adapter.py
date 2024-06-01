class ServiceAdapter:
    @property
    def sales_crm_service(self):
        from goal_setting_core.adapters.account_service import AccountService

        return AccountService()
