

def configure_helpers(app):
    @app.context_processor
    def utility_processor():
        def get_category_class(category):
            category_map = {'error': 'alert-danger', 'success': 'alert-success'}
            return category_map.get(category, 'alert-info')
        return dict(get_category_class=get_category_class)
