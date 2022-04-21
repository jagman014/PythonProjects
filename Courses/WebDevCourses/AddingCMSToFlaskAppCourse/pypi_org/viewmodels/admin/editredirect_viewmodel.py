from pypi_org.services import cms_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class EditRedirectViewModel(ViewModelBase):
    def __init__(self, redirect_id: int = 0):
        super().__init__()

        self.redirect_id = redirect_id
        self.redirect = None
        self.name = ''
        self.short_url = ''
        self.url = ''
        
        if self.redirect_id:
            self.redirect = cms_service.get_redirect_by_id(self.redirect_id)
        
        if self.redirect:
            self.name = self.redirect.get('name')
            self.short_url = self.redirect.get('short_url')
            self.url = self.redirect.get('url')
    
    def process_form(self):
        self.name = self.request_dict.get('name', '').strip()
        self.short_url = self.request_dict.get('short_url', '').strip().lower()
        self.url = self.request_dict.get('url', '').strip().lower()

    def validate(self) -> bool:
        if not (self.name and self.name.strip()):
            self.error = 'You must specify a name'
            return False
        
        if not (self.url and self.url.strip()):
            self.error = 'You must specify a url'
            return False
        
        if not (self.short_url and self.short_url.strip()):
            self.error = 'You must specify a short_url'
            return False
        
        if self.redirect_id and not self.redirect:
            self.error = f"The redirect with ID: {self.redirect_id} doesn't exist"
            return False

        if not self.redirect_id and cms_service.get_redirect(self.short_url):
            self.error = f"The redirect with URL: /{self.short_url} already exists"
            return False
        
        return True
