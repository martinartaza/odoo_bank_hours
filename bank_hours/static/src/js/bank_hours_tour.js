/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { stepUtils } from "@web_tour/tour_service/tour_utils";
import { markup } from "@odoo/owl";

registry.category("web_tour.tours").add('bank_hours_menu_tour', {
    url: '/web',
    sequence: 220,
    steps: () => [
        stepUtils.showAppsMenuItem(),
        {
            trigger: '.o_app[data-menu-xmlid="bank_hours.menu_bank_hours_root"]',
            content: markup(_t('Módulo para gestionar el banco de horas según las nuevas regulaciones laborales de Argentina.')),
            position: 'right',
        },
    ],
});

