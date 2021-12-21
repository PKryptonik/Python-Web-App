

def get_category_class(category):
    category_map = {'': 'alert-info', 'error': 'alert-danger'}
    return category_map[category]


def configure_helpers(app):
    @app.context_processor
    #def inject_user():
     #   return dict(category=get_category_class)