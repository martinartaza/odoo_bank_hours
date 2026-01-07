# -*- coding: utf-8 -*-

def post_init_hook(env):
    """
    Post initialization hook to ensure the tour is available for all users.
    This ensures the tour will be shown automatically when the module is installed.
    """
    # Remove any existing consumption of the bank_hours_menu_tour
    # This ensures the tour will be shown automatically when the module is installed
    tour_model = env['web_tour.tour']
    consumed_tours = tour_model.search([('name', '=', 'bank_hours_menu_tour')])
    if consumed_tours:
        consumed_tours.unlink()
