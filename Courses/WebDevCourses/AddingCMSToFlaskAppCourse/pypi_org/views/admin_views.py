import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase
from pypi_org.viewmodels.admin.redirectlist_viewmodel import RedirectListViewModel
from pypi_org.viewmodels.admin.editredirect_viewmodel import EditRedirectViewModel
from pypi_org.viewmodels.admin.pagelist_viewmodel import PageListViewModel
from pypi_org.viewmodels.admin.editpage_viewmodel import EditPageViewModel
from pypi_org.infrastructure import permissions

blueprint = flask.Blueprint('admin', __name__, template_folder='templates')


@blueprint.route('/admin')
@response(template_file='admin/index.html')
@permissions.admin
def index():
    vm = ViewModelBase()
    return vm.to_dict()


@blueprint.route('/admin/redirects')
@response(template_file='admin/redirects.html')
@permissions.admin
def redirects():
    vm = RedirectListViewModel()
    return vm.to_dict()


@blueprint.route('/admin/pages')
@response(template_file='admin/pages.html')
@permissions.admin
def pages():
    vm = PageListViewModel()
    return vm.to_dict()


######################## ADD REDIRECT VIEWS ################################


@blueprint.route('/admin/add_redirect', methods=['GET'])
@response(template_file='admin/edit_redirect.html')
@permissions.admin
def add_redirect_get():
    vm = EditRedirectViewModel()
    return vm.to_dict()


@blueprint.route('/admin/add_redirect', methods=['POST'])
@response(template_file='admin/edit_redirect.html')
@permissions.admin
def add_redirect_post():
    vm = EditRedirectViewModel()
    vm.process_form()
    
    if not vm.validate():
        return vm.to_dict()
    
    cms_service.create_redirect(vm.name, vm.short_url, vm.url)

    return flask.redirect('/admin/redirects')


######################## EDIT REDIRECT VIEWS ################################


@blueprint.route('/admin/edit_redirect/<int:redirect_id>', methods=['GET'])
@response(template_file='admin/edit_redirect.html')
@permissions.admin
def edit_redirect_get(redirect_id: int):
    vm = EditRedirectViewModel(redirect_id)

    if not vm.redirect:
        return flask.abort(404)

    return vm.to_dict()


@blueprint.route('/admin/edit_redirect/<int:redirect_id>', methods=['POST'])
@response(template_file='admin/edit_redirect.html')
@permissions.admin
def edit_redirect_post(redirect_id: int):
    vm = EditRedirectViewModel(redirect_id)
    vm.process_form()
    
    if not vm.validate():
        return vm.to_dict()
    
    cms_service.update_redirect(vm.redirect_id, vm.name, vm.short_url, vm.url)

    return flask.redirect('/admin/redirects')


######################## ADD PAGE VIEWS ################################


@blueprint.route('/admin/add_page', methods=['GET'])
@response(template_file='admin/edit_page.html')
@permissions.admin
def add_page_get():
    vm = EditPageViewModel()
    return vm.to_dict()


@blueprint.route('/admin/add_page', methods=['POST'])
@response(template_file='admin/edit_page.html')
@permissions.admin
def add_page_post():
    vm = EditPageViewModel()
    vm.process_form()
    
    if not vm.validate():
        return vm.to_dict()
    
    cms_service.create_page(vm.title, vm.contents, vm.contents)

    return flask.redirect('/admin/pages')


######################## EDIT PAGE VIEWS ################################


@blueprint.route('/admin/edit_page/<int:page_id>', methods=['GET'])
@response(template_file='admin/edit_page.html')
@permissions.admin
def edit_page_get(page_id: int):
    vm = EditPageViewModel(page_id)

    if not vm.page:
        return flask.abort(404)

    return vm.to_dict()


@blueprint.route('/admin/edit_page/<int:page_id>', methods=['POST'])
@response(template_file='admin/edit_page.html')
@permissions.admin
def edit_page_post(page_id: int):
    vm = EditPageViewModel(page_id)
    vm.process_form()
    
    if not vm.validate():
        return vm.to_dict()
    
    cms_service.update_page(vm.page_id, vm.title, vm.contents, vm.contents)

    return flask.redirect('/admin/pages')
