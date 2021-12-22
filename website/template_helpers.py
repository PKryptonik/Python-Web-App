
#not needed anymore i think
#def get_category_class(category):
#    category_map = {'': 'alert-info', 'error': 'alert-danger'}
#    return category_map[category]


def configure_helpers(app):
    @app.context_processor
    def utility_processor():
        def get_category_class(category):
            category_map = {'': 'alert-info', 'error': 'alert-danger', 'success': 'alert-success'}
            return category_map[category]
        return dict(get_category_class=get_category_class)
     
     