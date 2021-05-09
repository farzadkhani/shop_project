from datetime import datetime
from Products.models import Category

def shared_context(request):
    '''
    this is for share between all page
    '''
    all_categories = Category.objects.all()
    return {
        'year':datetime.today().year,
        'category_list_all':all_categories,
    }